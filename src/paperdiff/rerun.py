"""Run one command under explicit limits and compare the numbers it prints with the paper (docs/design.md §7)."""

from __future__ import annotations

import json
import math
import os
import re
import signal
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import yaml

from .values import fmt

LOG_TAIL_LINES = 50


class RerunError(RuntimeError):
    pass


@dataclass
class Target:
    name: str
    paper_value: float
    paper_source: str
    regex: str
    file: str | None  # read from this file (relative to repo) instead of the command output
    pick: str  # "first" | "last"
    rel_tol: float | None
    abs_tol: float | None


@dataclass
class Spec:
    repo: Path
    command: list[str]
    timeout_s: float
    gpus: int
    tokens: int | None
    env: dict[str, str]
    targets: list[Target]


def load_spec(path: Path) -> Spec:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise RerunError(f"{path}: expected a mapping")
    budget = data.get("budget") or {}
    if "timeout_s" not in budget:
        raise RerunError(f"{path}: budget.timeout_s is required; paperdiff never runs without a time limit")
    cmd = data.get("command")
    if not isinstance(cmd, list) or not cmd or not all(isinstance(c, str) for c in cmd):
        raise RerunError(f"{path}: command must be a non-empty list of strings (it is run without a shell)")
    repo = (path.parent / Path(data["repo"]).expanduser()).resolve() if "repo" in data else None
    if repo is None or not repo.is_dir():
        raise RerunError(f"{path}: repo must point to an existing directory")
    targets = []
    for t in data.get("targets") or []:
        metric, tol = t.get("metric") or {}, t.get("tolerance") or {}
        if "regex" not in metric or "paper" not in t or "value" not in t["paper"]:
            raise RerunError(f"{path}: target {t.get('name')!r} needs paper.value and metric.regex")
        targets.append(Target(
            name=str(t.get("name", "target")), paper_value=float(t["paper"]["value"]),
            paper_source=str(t["paper"].get("source", "")), regex=metric["regex"], file=metric.get("file"),
            pick=metric.get("pick", "last"), rel_tol=tol.get("rel"), abs_tol=tol.get("abs"),
        ))
    if not targets:
        raise RerunError(f"{path}: at least one target is required")
    return Spec(repo, cmd, float(budget["timeout_s"]), int(budget.get("gpus", 0)), budget.get("tokens"),
                {str(k): str(v) for k, v in (data.get("env") or {}).items()}, targets)


def _within(measured: float, t: Target) -> bool:
    if t.abs_tol is not None and abs(measured - t.paper_value) <= t.abs_tol:
        return True
    if t.rel_tol is not None and t.paper_value != 0 and abs(measured - t.paper_value) / abs(t.paper_value) <= t.rel_tol:
        return True
    if t.abs_tol is None and t.rel_tol is None:
        return math.isclose(measured, t.paper_value, rel_tol=1e-6)
    return False


def run(spec: Spec, out_dir: Path, allow_run: bool) -> dict:
    if not allow_run:
        raise RerunError("refusing to execute: pass --allow-run to run the command in the spec on this machine")
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "rerun.log"
    env = dict(os.environ)
    env.setdefault("PYTHONUNBUFFERED", "1")  # keep partial output if the time budget kills the run
    env.update(spec.env)
    env["CUDA_VISIBLE_DEVICES"] = ",".join(str(i) for i in range(spec.gpus))

    start = time.monotonic()
    status = "finished"
    with log_path.open("w") as log:
        proc = subprocess.Popen(spec.command, cwd=spec.repo, env=env, stdout=log, stderr=subprocess.STDOUT,
                                start_new_session=True)
        try:
            code = proc.wait(timeout=spec.timeout_s)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            code = proc.wait()
            status = "timeout"
    elapsed = time.monotonic() - start
    if status != "timeout" and code != 0:
        status = "failed"
    output = log_path.read_text(errors="replace")

    results = []
    for t in spec.targets:
        text = output
        if t.file:
            f = spec.repo / t.file
            text = f.read_text(errors="replace") if f.is_file() else ""
        matches = re.findall(t.regex, text)
        if not matches:
            verdict = status if status != "finished" else "not_found"
            results.append({"name": t.name, "paper": t.paper_value, "paper_source": t.paper_source,
                            "measured": None, "verdict": verdict})
            continue
        raw = matches[0] if t.pick == "first" else matches[-1]
        raw = raw[0] if isinstance(raw, tuple) else raw
        measured = float(raw)
        rel = abs(measured - t.paper_value) / abs(t.paper_value) if t.paper_value else None
        verdict = "reproduced" if _within(measured, t) else "differs"
        if status == "timeout":
            verdict += " (partial: time budget hit)"
        results.append({"name": t.name, "paper": t.paper_value, "paper_source": t.paper_source,
                        "measured": measured, "rel_diff": rel, "verdict": verdict,
                        "tolerance": {"rel": t.rel_tol, "abs": t.abs_tol}})

    return {
        "command": spec.command, "cwd": str(spec.repo), "status": status, "exit_code": code,
        "elapsed_s": round(elapsed, 1),
        "budget": {"timeout_s": spec.timeout_s, "gpus": spec.gpus, "tokens": spec.tokens},
        "targets": results, "log": str(log_path),
        "log_tail": output.splitlines()[-LOG_TAIL_LINES:],
    }


def to_markdown(result: dict) -> str:
    b = result["budget"]
    out = ["# paperdiff rerun", "",
           f"- Command: `{' '.join(result['command'])}` (in `{result['cwd']}`)",
           f"- Budget: {b['timeout_s']:g} s, {b['gpus']} GPU(s)" + (f", {b['tokens']} agent tokens" if b["tokens"] else ""),
           f"- Status: {result['status']} (exit code {result['exit_code']}), {result['elapsed_s']} s", "",
           "| Target | Paper | Measured | Rel. diff | Verdict |", "|---|---|---|---|---|"]
    for t in result["targets"]:
        measured = fmt(t["measured"]) if t["measured"] is not None else "—"
        rel = f"{t['rel_diff']:.1%}" if t.get("rel_diff") is not None else "—"
        out.append(f"| {t['name']} | {fmt(t['paper'])} (`{t['paper_source']}`) | {measured} | {rel} | {t['verdict']} |")
    out += ["", "A single rerun that does not match is not evidence that a result is irreproducible: hardware, "
            "seeds and library versions all move numbers.", "", "<details><summary>Log tail</summary>", "", "```"]
    out += result["log_tail"]
    out += ["```", "", "</details>", ""]
    return "\n".join(out)


def write(result: dict, out_dir: Path) -> None:
    (out_dir / "rerun.json").write_text(json.dumps(result, indent=2) + "\n")
    (out_dir / "rerun.md").write_text(to_markdown(result))
