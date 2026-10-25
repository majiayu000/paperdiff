"""Run paperdiff's --llm pass on the SciCoQA pairs whose deterministic run completed (see README.md).

Uses the papers and repositories already fetched by run.py. Results go to ~/.cache/paperdiff/scicoqa/runs-llm/.
`--limit 3` runs the cost trial; the full run is resumable (finished pairs are skipped).
"""

from __future__ import annotations

import argparse
import json

from run import get_paper, get_repo, run_id

from paperdiff.fetch import cache_dir
from paperdiff.llm import LLMConfig, LLMError, run
from paperdiff.paper import load_paper

PER_PAPER_USD = 1.0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="only the first N pairs (cost trial)")
    ap.add_argument("--max-total-usd", type=float, required=True, help="stop once this much has been spent")
    args = ap.parse_args()
    runs = cache_dir() / "scicoqa" / "runs"
    out_dir = cache_dir() / "scicoqa" / "runs-llm"
    out_dir.mkdir(parents=True, exist_ok=True)
    done = sorted((json.loads(p.read_text()) for p in runs.glob("*.json")), key=lambda r: (r["paper_url"], r["code_url"]))
    done = [r for r in done if r["status"] == "ok"][: args.limit]
    total = sum(json.loads(p.read_text())["llm"]["stats"]["cost_usd"] for p in out_dir.glob("*.json")
                if "llm" in json.loads(p.read_text()))
    for n, r in enumerate(done, 1):
        out = out_dir / f"{run_id(r['paper_url'], r['code_url'])}.json"
        if out.exists():
            continue
        if total >= args.max_total_usd:
            print(f"stopping: ${total:.2f} spent, cap ${args.max_total_usd:.2f}")
            break
        src, repo = get_paper(r["paper_url"]), get_repo(r["code_url"])
        paper = load_paper(src.kind, src.path, src.label)
        cfg = LLMConfig(max_usd=min(PER_PAPER_USD, args.max_total_usd - total))
        record = {"paper_url": r["paper_url"], "code_url": r["code_url"], "ids": r["ids"]}
        try:
            record["llm"] = run(paper.lines, repo.path, cfg).to_json()
            total += record["llm"]["stats"]["cost_usd"]
        except LLMError as e:
            print(f"error: {e}")
            raise SystemExit(2) from e
        out.write_text(json.dumps(record, indent=1))
        st = record["llm"]["stats"]
        print(f"[{n}/{len(done)}] {r['paper_url']}: kept {st['kept']}, dropped {st['dropped']}, "
              f"${st['cost_usd']:.4f} (total ${total:.2f})", flush=True)


if __name__ == "__main__":
    main()
