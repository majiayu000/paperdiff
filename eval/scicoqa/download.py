"""Fetch the SciCoQA real split (CC-BY 4.0) into the cache; it is never stored in this repository."""

from __future__ import annotations

import urllib.request
from pathlib import Path

from paperdiff.fetch import cache_dir

URL = "https://raw.githubusercontent.com/UKPLab/scicoqa/main/data/scicoqa-real-v1.1.jsonl"


def data_path() -> Path:
    return cache_dir() / "scicoqa" / "scicoqa-real-v1.1.jsonl"


def main() -> None:
    path = data_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(URL, timeout=60) as resp:
        path.write_bytes(resp.read())
    print(f"wrote {path} ({sum(1 for _ in path.open())} items)")


if __name__ == "__main__":
    main()
