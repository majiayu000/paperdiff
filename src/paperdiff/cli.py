from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from . import __version__
from .align import CATEGORIES, align
from .code import extract_repo
from .fetch import FetchError, resolve_paper, resolve_repo
from .paper import load_paper
from .report import now, to_json, to_markdown
from .rerun import RerunError, load_spec, run, write


def cmd_check(args: argparse.Namespace) -> int:
    src = resolve_paper(args.paper)
    repo = resolve_repo(args.repo)
    paper = load_paper(src.kind, src.path, src.label)
    settings = extract_repo(repo.path, args.exclude)
    findings = align(paper, settings)
    generated = now()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "report.md").write_text(to_markdown(paper, repo, findings, generated, args.exclude))
    report = to_json(paper, repo, findings, generated, args.exclude)
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    counts = Counter(f.category for f in findings)
    summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    print(f"{paper.label}: {len(paper.claims)} claims, {len(settings)} code settings -> {summary}")
    print(f"wrote {out / 'report.md'} and {out / 'report.json'}")
    failing = [c for c in args.fail_on if counts.get(c)]
    if failing:
        print(f"failing because of: {', '.join(f'{c}={counts[c]}' for c in failing)}", file=sys.stderr)
        return 1
    return 0


def cmd_rerun(args: argparse.Namespace) -> int:
    spec = load_spec(Path(args.spec))
    out = Path(args.out)
    result = run(spec, out, args.allow_run)
    write(result, out)
    for t in result["targets"]:
        print(f"{t['name']}: paper={t['paper']} measured={t['measured']} -> {t['verdict']}")
    print(f"status={result['status']} elapsed={result['elapsed_s']}s; wrote {out / 'rerun.md'}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="paperdiff", description="Report differences between a paper's stated "
                                "experimental setup and its code. Reports differences; draws no conclusions.")
    p.add_argument("--version", action="version", version=f"paperdiff {__version__}")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check", help="static comparison of paper and code (never runs the code)")
    c.add_argument("paper", help="arXiv ID/URL, a .pdf, a .tex file, a LaTeX directory or a source .tar.gz")
    c.add_argument("repo", help="git URL or local directory")
    c.add_argument("-o", "--out", default="paperdiff-out", help="output directory (default: paperdiff-out)")
    c.add_argument("--exclude", action="append", default=[], metavar="GLOB",
                   help="skip repository paths matching this glob (repeatable), e.g. 'vendor/*'")
    c.add_argument("--fail-on", action="append", default=[], choices=list(CATEGORIES)[:-1], metavar="CATEGORY",
                   help="exit 1 if any finding has this category (repeatable), e.g. for a pre-submission CI check")
    c.set_defaults(func=cmd_check)

    r = sub.add_parser("rerun", help="run one command under a time/GPU budget and compare its numbers")
    r.add_argument("spec", help="rerun spec (YAML), see docs/design.md §7.2")
    r.add_argument("--allow-run", action="store_true", help="required: actually execute the command")
    r.add_argument("-o", "--out", default="paperdiff-out", help="output directory (default: paperdiff-out)")
    r.set_defaults(func=cmd_rerun)

    args = p.parse_args(argv)
    try:
        return args.func(args)
    except (FetchError, RerunError, ValueError) as e:
        print(f"paperdiff: error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
