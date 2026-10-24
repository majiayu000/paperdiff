"""Run paperdiff on every (paper version, repo commit) pair in the SciCoQA real split.

Results go to ~/.cache/paperdiff/scicoqa/runs/<run-id>.json. Already finished runs are skipped, so the script can be
resumed. Pass --force to rerun everything (for example after changing paperdiff).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import traceback
from pathlib import Path

from download import data_path

from paperdiff import fetch
from paperdiff.align import align
from paperdiff.code import extract_repo
from paperdiff.fetch import FetchError, cache_dir
from paperdiff.paper import load_paper


def run_id(paper: str, code: str) -> str:
    return hashlib.sha1(f"{paper} {code}".encode()).hexdigest()[:12]


def load_items() -> list[dict]:
    return [json.loads(line) for line in data_path().open()]


def get_paper(url: str):
    arxiv = re.match(r"https?://arxiv\.org/(?:abs|pdf)/([^/?#]+?)(?:\.pdf)?$", url)
    if arxiv:
        return fetch.fetch_arxiv(arxiv.group(1))
    dest = cache_dir() / "scicoqa" / "pdfs" / (hashlib.sha1(url.encode()).hexdigest()[:16] + ".pdf")
    if not dest.exists():
        blob = fetch._get(url)  # same User-Agent and >= 3 s spacing as arXiv requests
        if blob[:4] != b"%PDF":
            raise FetchError(f"{url} did not return a PDF")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(blob)
    return fetch.PaperSource("pdf", dest, url)


def get_repo(versioned: str) -> fetch.RepoSource:
    m = re.match(r"(https://github\.com/[^/]+/[^/]+)/tree/([0-9a-f]{7,40})", versioned)
    if not m:
        raise FetchError(f"unexpected code URL {versioned}")
    url, sha = m.groups()
    dest = cache_dir() / "scicoqa" / "repos" / f"{url.split('/')[-2]}__{url.split('/')[-1]}__{sha[:12]}"
    if not (dest / ".git").exists():
        dest.mkdir(parents=True, exist_ok=True)
        for args in (["init", "-q"], ["remote", "add", "origin", url], ["fetch", "-q", "--depth", "1", "origin", sha],
                     ["checkout", "-q", "FETCH_HEAD"]):
            res = subprocess.run(["git", *args], cwd=dest, capture_output=True, text=True)
            if res.returncode != 0:
                raise FetchError(f"git {' '.join(args)} for {url}: {res.stderr.strip()[:300]}")
    return fetch.RepoSource(dest, url, sha)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    out_dir = cache_dir() / "scicoqa" / "runs"
    out_dir.mkdir(parents=True, exist_ok=True)
    pairs = {}
    for it in load_items():
        pairs.setdefault((it["paper_url_versioned"], it["code_url_versioned"]), []).append(it["discrepancy_id"])
    for n, ((paper_url, code_url), ids) in enumerate(sorted(pairs.items()), 1):
        out = out_dir / f"{run_id(paper_url, code_url)}.json"
        if out.exists() and not args.force:
            continue
        record = {"paper_url": paper_url, "code_url": code_url, "ids": ids}
        try:
            src = get_paper(paper_url)
            repo = get_repo(code_url)
            paper = load_paper(src.kind, src.path, src.label)
            settings = extract_repo(repo.path)
            findings = align(paper, settings)
            record.update(status="ok", source_kind=src.kind, claims=len(paper.claims), settings=len(settings),
                          findings=[f.to_json() for f in findings])
        except Exception as e:  # recorded per run so one bad paper does not stop the evaluation
            record.update(status="error", error=f"{type(e).__name__}: {e}", trace=traceback.format_exc()[-1500:])
        out.write_text(json.dumps(record, indent=1))
        print(f"[{n}/{len(pairs)}] {record['status']} {paper_url} {record.get('error', '')[:120]}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
