"""Fetch papers and repositories, with a local cache.

arXiv rules followed here (see docs/design.md §3.1):
- programmatic access goes to export.arxiv.org, never to arxiv.org/e-print or /src;
- at most one request every 3 seconds, one connection at a time;
- results are cached so a paper is downloaded once.
"""

from __future__ import annotations

import gzip
import io
import os
import re
import subprocess
import tarfile
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from . import __version__

ARXIV_BASE = "https://export.arxiv.org"
USER_AGENT = f"paperdiff/{__version__} (single-paper fetch; https://github.com/majiayu000/paperdiff)"
MIN_INTERVAL_S = 3.0
ARXIV_ID_RE = re.compile(r"^(?:arxiv:)?(\d{4}\.\d{4,5}(?:v\d+)?|[a-z\-]+(?:\.[A-Z]{2})?/\d{7}(?:v\d+)?)$", re.I)

_last_request = 0.0


class FetchError(RuntimeError):
    pass


def cache_dir() -> Path:
    return Path(os.environ.get("PAPERDIFF_CACHE", Path.home() / ".cache" / "paperdiff"))


def parse_arxiv_id(text: str) -> str | None:
    text = text.strip()
    m = re.match(r"^https?://(?:export\.)?arxiv\.org/(?:abs|pdf)/([^?#]+?)(?:\.pdf)?/?$", text)
    if m:
        text = m.group(1)
    m = ARXIV_ID_RE.match(text)
    return m.group(1) if m else None


def _get(url: str) -> bytes:
    global _last_request
    wait = MIN_INTERVAL_S - (time.monotonic() - _last_request)
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        raise FetchError(f"GET {url} failed: HTTP {e.code}") from e
    except urllib.error.URLError as e:
        raise FetchError(f"GET {url} failed: {e.reason}") from e
    finally:
        _last_request = time.monotonic()


@dataclass
class PaperSource:
    """Either a directory of LaTeX files or a single PDF."""

    kind: str  # "latex" | "pdf"
    path: Path
    label: str  # what the report shows as the paper identity


def _unpack_source(blob: bytes, dest: Path) -> None:
    """arXiv /src returns a gzipped tar, a gzipped single .tex, or a PDF."""
    dest.mkdir(parents=True, exist_ok=True)
    if blob[:4] == b"%PDF":
        (dest / "paper.pdf").write_bytes(blob)
        return
    data = gzip.decompress(blob) if blob[:2] == b"\x1f\x8b" else blob
    try:
        with tarfile.open(fileobj=io.BytesIO(data)) as tar:
            tar.extractall(dest, filter="data")
        return
    except tarfile.ReadError:
        pass
    (dest / "main.tex").write_bytes(data)


def fetch_arxiv(arxiv_id: str) -> PaperSource:
    root = cache_dir() / "arxiv" / arxiv_id.replace("/", "_")
    src = root / "src"
    if not src.exists():
        try:
            blob = _get(f"{ARXIV_BASE}/src/{arxiv_id}")
            _unpack_source(blob, src)
        except FetchError:
            # Some submissions have no source; fall back to the PDF.
            pdf = _get(f"{ARXIV_BASE}/pdf/{arxiv_id}")
            src.mkdir(parents=True, exist_ok=True)
            (src / "paper.pdf").write_bytes(pdf)
    if any(src.rglob("*.tex")):
        return PaperSource("latex", src, f"arXiv:{arxiv_id}")
    pdfs = list(src.rglob("*.pdf"))
    if len(pdfs) == 1 and pdfs[0].name == "paper.pdf":
        return PaperSource("pdf", pdfs[0], f"arXiv:{arxiv_id}")
    raise FetchError(f"arXiv:{arxiv_id}: no .tex files and no PDF in {src}")


def resolve_paper(spec: str) -> PaperSource:
    p = Path(spec).expanduser()
    if p.exists():
        if p.is_dir():
            return PaperSource("latex", p, p.name)
        if p.suffix.lower() == ".pdf":
            return PaperSource("pdf", p, p.name)
        if p.suffix.lower() == ".tex":
            return PaperSource("latex", p.parent, p.name)
        if p.name.endswith((".tar.gz", ".tgz", ".gz")):
            dest = cache_dir() / "local" / p.name
            if not dest.exists():
                _unpack_source(p.read_bytes(), dest)
            return PaperSource("latex", dest, p.name)
        raise FetchError(f"unsupported paper file: {p}")
    arxiv_id = parse_arxiv_id(spec)
    if arxiv_id is None:
        raise FetchError(f"not a local path or arXiv ID: {spec}")
    return fetch_arxiv(arxiv_id)


@dataclass
class RepoSource:
    path: Path
    url: str | None  # remote URL, used for permalinks
    commit: str | None


def _git(args: list[str], cwd: Path | None = None) -> str:
    res = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        raise FetchError(f"git {' '.join(args)} failed: {res.stderr.strip()}")
    return res.stdout.strip()


def resolve_repo(spec: str) -> RepoSource:
    p = Path(spec).expanduser()
    if p.is_dir():
        try:
            commit = _git(["rev-parse", "HEAD"], cwd=p)
            url = _git(["config", "--get", "remote.origin.url"], cwd=p) or None
        except FetchError:
            commit, url = None, None
        return RepoSource(p, _normalize_github(url) if url else None, commit)
    if not re.match(r"^(https?://|git@)", spec):
        raise FetchError(f"not a local directory or git URL: {spec}")
    url = _normalize_github(spec)
    name = re.sub(r"[^A-Za-z0-9_.-]+", "_", url.split("://", 1)[-1])
    dest = cache_dir() / "repos" / name
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        _git(["clone", "--depth", "1", "--quiet", spec, str(dest)])
    return RepoSource(dest, url, _git(["rev-parse", "HEAD"], cwd=dest))


def _normalize_github(url: str) -> str:
    url = re.sub(r"^git@github\.com:", "https://github.com/", url)
    return re.sub(r"\.git$", "", url.rstrip("/"))
