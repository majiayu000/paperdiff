"""Score paperdiff runs against SciCoQA gold items with the rules in README.md.

Writes eval/scicoqa/results.md and, on first use, eval/scicoqa/audit.json (the precision sample, to be judged by hand).
"""

from __future__ import annotations

import argparse
import json
import random
import re
from collections import Counter
from pathlib import Path

from download import data_path
from run import run_id

from paperdiff.fetch import cache_dir
from paperdiff.keys import KEYS_BY_NAME
from paperdiff.values import clean_latex, equal, find_numbers

HERE = Path(__file__).parent
ANY = {"conflict", "ambiguous", "missing_in_code", "missing_in_paper"}
AUDIT_SEED, AUDIT_SIZE = 20261025, 30


def gold_text(it: dict) -> str:
    return "\n".join(t for t in (it["origin_discrepancy_text"], it["discrepancy_description_gpt"],
                                 it["discrepancy_description_gemini"]) if t)


def gold_files(it: dict) -> set[str]:
    files = set(it["relevant_code_files_gpt"] or []) | set(it["relevant_code_files_gemini"] or [])
    files |= set((it["changed_code_files"] or {}).get("file_name") or [])
    return {f.strip("/") for f in files if f}


def _file(loc: str) -> str:
    return loc.rsplit(":", 1)[0]


def location_ok(f: dict, it: dict, text: str) -> bool:
    if f["code"]:
        files = gold_files(it)
        return any(_file(c["loc"]).endswith(g) or g.endswith(_file(c["loc"])) for c in f["code"] for g in files)
    return re.search(KEYS_BY_NAME[f["key"]].phrase, text, 0 if f["key"] == "optimizer" else re.I) is not None


def value_ok(f: dict, text: str) -> bool:
    values = [f["paper"]["value"]] if f["paper"] else []
    values += [c["value"] for c in f["code"]]
    nums = [n.value for n in find_numbers(clean_latex(text))]
    for v in values:
        if isinstance(v, (int, float)) and not isinstance(v, bool) and any(equal(float(v), n) for n in nums):
            return True
        if isinstance(v, str) and v.lower() in text.lower():
            return True
    return False


def matches(f: dict, it: dict) -> bool:
    text = gold_text(it)
    return location_ok(f, it, text) and value_ok(f, text)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true", help="draw the precision sample if audit.json does not exist")
    ap.add_argument("--out", default=str(HERE / "results.md"))
    args = ap.parse_args()
    items = [json.loads(line) for line in data_path().open()]
    labels = json.loads((HERE / "labels.json").read_text())
    runs_dir = cache_dir() / "scicoqa" / "runs"
    runs = {}
    for it in items:
        rid = run_id(it["paper_url_versioned"], it["code_url_versioned"])
        runs[rid] = json.loads((runs_dir / f"{rid}.json").read_text())

    rows = []
    for it in items:
        run = runs[run_id(it["paper_url_versioned"], it["code_url_versioned"])]
        findings = run.get("findings", [])
        strict = any(f["category"] == "conflict" and matches(f, it) for f in findings)
        loose = any(f["category"] in ANY and matches(f, it) for f in findings)
        rows.append({"id": it["discrepancy_id"], "tier": labels[it["discrepancy_id"]]["tier"],
                     "category": it["discrepancy_category"] or "none", "status": run["status"],
                     "kind": run.get("source_kind"), "strict": strict, "any": loose})

    conflicts = []
    for rid, run in sorted(runs.items(), key=lambda kv: kv[1]["paper_url"]):
        gold = [it for it in items if run_id(it["paper_url_versioned"], it["code_url_versioned"]) == rid]
        for f in run.get("findings", []):
            if f["category"] == "conflict":
                conflicts.append({"paper_url": run["paper_url"], "code_url": run["code_url"], "finding": f,
                                  "gold_match": any(matches(f, it) for it in gold)})
    conflicts.sort(key=lambda c: (c["paper_url"], c["finding"]["paper"]["loc"], c["finding"]["key"]))

    audit_path = HERE / "audit.json"
    if args.audit and not audit_path.exists():
        sample = random.Random(AUDIT_SEED).sample(conflicts, min(AUDIT_SIZE, len(conflicts)))
        audit_path.write_text(json.dumps([dict(c, verdict=None, reason="") for c in sample], indent=1) + "\n")
    audit = json.loads(audit_path.read_text()) if audit_path.exists() else []

    Path(args.out).write_text(render(rows, runs, conflicts, audit))
    print(Path(args.out).read_text())


def _rate(hit: int, n: int) -> str:
    return f"{hit}/{n} ({hit / n:.1%})" if n else "0/0"


def render(rows, runs, conflicts, audit) -> str:
    ok_runs = sum(1 for r in runs.values() if r["status"] == "ok")
    kinds = Counter(r.get("source_kind") for r in runs.values() if r["status"] == "ok")
    out = ["# SciCoQA real split: results", "",
           f"- Runs: {len(runs)} (paper version, commit) pairs, {ok_runs} completed "
           f"({kinds.get('latex', 0)} from LaTeX source, {kinds.get('pdf', 0)} from PDF), "
           f"{len(runs) - ok_runs} failed to fetch or parse.",
           f"- Items: {len(rows)}; items whose run failed count as not detected.", "",
           "## Recall", "", "| Subset | Items | Detected (strict: conflict) | Detected (any non-match finding) |",
           "|---|---|---|---|"]
    subsets = [("All items", rows), ("Coverable (`keys`)", [r for r in rows if r["tier"] == "keys"]),
               ("Other setting values", [r for r in rows if r["tier"] == "other_setting"]),
               ("Method-level", [r for r in rows if r["tier"] == "method"])]
    for name, rs in subsets:
        out.append(f"| {name} | {len(rs)} | {_rate(sum(r['strict'] for r in rs), len(rs))} | "
                   f"{_rate(sum(r['any'] for r in rs), len(rs))} |")
    out += ["", "By SciCoQA category:", "", "| Category | Items | Strict | Any |", "|---|---|---|---|"]
    for cat in sorted({r["category"] for r in rows}):
        rs = [r for r in rows if r["category"] == cat]
        out.append(f"| {cat} | {len(rs)} | {sum(r['strict'] for r in rs)} | {sum(r['any'] for r in rs)} |")
    out += ["", "Coverable items:", ""]
    for r in rows:
        if r["tier"] == "keys":
            out.append(f"- `{r['id']}`: run {r['status']}, source {r['kind']}, strict={r['strict']}, any={r['any']}")
    hits = [r["id"] for r in rows if r["any"]]
    out += ["", f"Items detected by any rule: {', '.join(f'`{h}`' for h in hits) or 'none'}", ""]

    matched = sum(c["gold_match"] for c in conflicts)
    judged = [a for a in audit if a["verdict"] in ("real", "false")]
    real = sum(a["verdict"] == "real" for a in judged)
    current = {(c["paper_url"], c["finding"]["key"], c["finding"]["paper"]["loc"], str(c["finding"]["paper"]["value"]),
                str(c["finding"]["code"][0]["loc"] if c["finding"]["code"] else "")) for c in conflicts}

    def still(a: dict) -> bool:
        f = a["finding"]
        return (a["paper_url"], f["key"], f["paper"]["loc"], str(f["paper"]["value"]),
                str(f["code"][0]["loc"] if f["code"] else "")) in current

    kept = [a for a in judged if still(a)]
    kept_real = sum(a["verdict"] == "real" for a in kept)
    out += ["## Precision", "",
            f"- Conflict findings over all completed runs: {len(conflicts)}",
            f"- Precision vs gold (lower bound, gold is incomplete): {_rate(matched, len(conflicts))}",
            f"- Audited precision (random sample, seed {AUDIT_SEED}): {_rate(real, len(judged))} judged "
            f"({len(audit) - len(judged)} of {len(audit)} not yet judged)",
            f"- Of the audited findings, still reported as conflicts by the current code: {len(kept)}; "
            f"real among them: {_rate(kept_real, len(kept))}", ""]
    if judged:
        out += ["| # | Paper | Setting | Paper value | Code value | Verdict | Still a conflict | Reason |",
                "|---|---|---|---|---|---|---|---|"]
        for i, a in enumerate(audit, 1):
            f = a["finding"]
            code = f["code"][0] if f["code"] else {}
            out.append(f"| {i} | {a['paper_url']} | {f['key']} | `{f['paper']['raw']}` ({f['paper']['loc']}) | "
                       f"{code.get('value')} ({code.get('loc')}) | {a['verdict']} | {'yes' if still(a) else 'no'} | {a['reason']} |")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    main()
