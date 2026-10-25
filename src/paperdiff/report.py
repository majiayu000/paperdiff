"""Render findings as Markdown and JSON."""

from __future__ import annotations

import datetime as dt
from collections import Counter

from . import __version__
from .align import CATEGORIES, Finding
from .code import Setting
from .fetch import RepoSource
from .paper import Paper
from .values import equal, fmt

SCHEMA_VERSION = 1
MAX_CANDIDATES = 5

DISCLAIMER = (
    "paperdiff reports differences between what a paper states and what its code configures. "
    "A difference can come from a typo, a later code change, a setting defined elsewhere, a reasonable "
    "implementation choice, or an extraction error by this tool. It is not a judgement about whether the "
    "paper is correct, and it is not an accusation of misconduct. Check each item by hand before citing it."
)

TITLES = {
    "conflict": "Conflicts — the code sets a different value",
    "ambiguous": "Ambiguous — several values, or the paper value is overridden",
    "missing_in_code": "Missing in code — stated in the paper, not found in the code",
    "missing_in_paper": "Missing in paper — set in the code, never mentioned in the paper",
    "match": "Matches",
}


def _permalink(repo: RepoSource, s: Setting) -> str:
    if repo.url and repo.commit and repo.url.startswith("https://github.com/"):
        return f"[{s.loc}]({repo.url}/blob/{repo.commit}/{s.file}#L{s.line})"
    return f"`{s.loc}`"


def _esc(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def to_json(paper: Paper, repo: RepoSource, findings: list[Finding], generated: str,
            excludes: list[str] | None = None, llm: dict | None = None) -> dict:
    out = {
        "schema_version": SCHEMA_VERSION,
        "paperdiff_version": __version__,
        "generated": generated,
        "paper": {"label": paper.label, "title": paper.title, "source_kind": paper.kind, "main_file": paper.main_file,
                  "claims": len(paper.claims)},
        "repo": {"path": str(repo.path), "url": repo.url, "commit": repo.commit, "excludes": excludes or []},
        "summary": dict(Counter(f.category for f in findings)),
        "findings": [f.to_json() for f in findings],
        "disclaimer": DISCLAIMER,
    }
    if llm is not None:
        out["llm"] = llm
    return out


LLM_NOTE = (
    "Found by a language model (`--llm`), not by paperdiff's deterministic comparison. Each item's paper and code "
    "quotes were checked to exist at the cited lines; whether the difference is real was not. Read both sides."
)


def _llm_markdown(repo: RepoSource, llm: dict) -> list[str]:
    st = llm["stats"]
    out = [f"## Method-level differences (LLM, {st['model']}) ({len(llm['findings'])})", "", f"> {LLM_NOTE}", "",
           f"- Chunks sent: {st['chunks']}, calls: {st['calls']}, cache hits: {st['cache_hits']}, "
           f"cost: ${st['cost_usd']:.4f}",
           f"- Proposed {st['proposed']}, kept {st['kept']}, dropped {st['dropped']} (citation check failed)"]
    if st.get("stopped"):
        out.append(f"- Stopped early: {st['stopped']}")
    out.append("")
    for i, f in enumerate(llm["findings"], 1):
        code_loc = f["code"]["loc"]
        file, _, line = code_loc.rpartition(":")
        link = (f"[{code_loc}]({repo.url}/blob/{repo.commit}/{file}#L{line})"
                if repo.url and repo.commit and repo.url.startswith("https://github.com/") else f"`{code_loc}`")
        out += [f"### L{i}. {_esc(f['summary'])}", "",
                f"- **Paper** `{f['paper']['loc']}`: \"{_esc(f['paper']['quote'])}\"",
                f"- **Code** {link}: `{_esc(f['code']['quote'])}`",
                f"- Confidence: {f['confidence']}. {_esc(f['reason'])}", ""]
    return out


def to_markdown(paper: Paper, repo: RepoSource, findings: list[Finding], generated: str,
                excludes: list[str] | None = None, llm: dict | None = None) -> str:
    counts = Counter(f.category for f in findings)
    out = [f"# paperdiff report: {paper.label}", ""]
    out.append(f"- Paper: {paper.label} ({'LaTeX source' if paper.kind == 'latex' else 'PDF'}"
               + (f", main file `{paper.main_file}`" if paper.main_file else "") + ")")
    repo_label = repo.url or str(repo.path)
    if paper.title:
        out.append(f"- Title: {paper.title}")
    out.append(f"- Code: {repo_label}" + (f" @ `{repo.commit[:12]}`" if repo.commit else ""))
    if excludes:
        out.append(f"- Excluded paths: {', '.join(f'`{e}`' for e in excludes)}")
    out.append(f"- Generated: {generated} by paperdiff {__version__}")
    if paper.kind == "pdf":
        out.append("- Note: the paper was read from PDF; table extraction from PDF is unreliable.")
    out += ["", "| Category | Count |", "|---|---|"]
    for c in CATEGORIES:
        out.append(f"| {c} | {counts.get(c, 0)} |")
    out += ["", f"> {DISCLAIMER}", ""]

    for cat in CATEGORIES:
        items = [f for f in findings if f.category == cat]
        if not items:
            continue
        out += [f"## {TITLES[cat]} ({len(items)})", ""]
        if cat == "match":
            out += ["| Setting | Paper | Paper location | Code | Code location |", "|---|---|---|---|---|"]
            for f in items:
                c = f.candidates[0] if f.candidates else None
                match = next((s for s in f.candidates if equal(s.value, f.claim.value)), c)
                out.append(f"| {f.key} | {_esc(f.claim.raw)} | `{f.claim.loc}` | {fmt(match.value)} "
                           f"({match.source}) | {_permalink(repo, match)} |")
            out.append("")
            continue
        for i, f in enumerate(items, 1):
            out.append(f"### {cat[:1].upper()}{i}. `{f.key}`")
            out.append("")
            if f.claim:
                col = f" (column: {f.claim.column})" if f.claim.column else ""
                out.append(f"- **Paper**: `{_esc(f.claim.raw)}` → {fmt(f.claim.value)} at `{f.claim.loc}`{col}")
                if f.claim.section:
                    out.append(f"  - Section: {f.claim.section}")
                out.append(f"  - Context: \"{_esc(f.claim.context)}\"")
            if f.candidates:
                out.append(f"- **Code** (highest precedence first; likely effective: "
                           f"{', '.join(fmt(v) for v in f.effective)}):")
                for s in f.candidates[:MAX_CANDIDATES]:
                    out.append(f"  - {fmt(s.value)} — {s.source} `{s.name}` at {_permalink(repo, s)}: "
                               f"`{_esc(s.text)}`")
                if len(f.candidates) > MAX_CANDIDATES:
                    out.append(f"  - … {len(f.candidates) - MAX_CANDIDATES} more in report.json")
            if f.scope:
                out.append(f"- Scope: compared only with files matching \"{f.scope}\"")
            if f.note:
                out.append(f"- Note: {f.note}")
            out.append("")
    if llm is not None:
        out += _llm_markdown(repo, llm)
    return "\n".join(out).rstrip() + "\n"


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
