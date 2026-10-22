"""Pair paper claims with code settings and classify the differences (docs/design.md §5)."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .code import Setting
from .keys import KEYS
from .paper import Claim, Paper, mentions
from .values import equal, fmt

UNOWNED = "files not tied to another section"
CATEGORIES = ("conflict", "ambiguous", "missing_in_code", "missing_in_paper", "match")

# Words in section titles that say nothing about which script an experiment uses.
SCOPE_STOPWORDS = {
    "appendix", "details", "detail", "implementation", "experiment", "experiments", "experimental", "setup",
    "settings", "setting", "training", "train", "hyperparameters", "hyperparameter", "additional", "results",
    "result", "data", "dataset", "datasets", "task", "tasks", "and", "the", "for", "with", "our", "method",
    "methods", "model", "models", "used", "using", "main", "more", "further", "study", "studies", "analysis",
    "evaluation", "baseline", "baselines", "empirical", "other", "all", "fine", "tuning", "pre",
}


@dataclass
class Finding:
    category: str
    key: str
    claim: Claim | None
    candidates: list[Setting] = field(default_factory=list)  # sorted by priority, highest first
    effective: list[object] = field(default_factory=list)  # distinct values at the highest priority level
    scope: str | None = None
    note: str = ""

    def to_json(self) -> dict:
        return {
            "category": self.category,
            "key": self.key,
            "paper": self.claim.to_json() if self.claim else None,
            "code": [c.to_json() for c in self.candidates],
            "effective": self.effective,
            "scope": self.scope,
            "note": self.note,
        }


def _tokens(text: str, stop: set[str] = SCOPE_STOPWORDS) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", text.lower().replace("-", "")) if len(t) >= 3 and
            t not in stop and not t.isdigit()]


def _unit(s: Setting) -> str:
    """The path text a setting is scoped by: the script a command launches plus the file it is in."""
    return re.sub(r"[^a-z0-9]", "", f"{s.target or ''} {s.file}".lower())


def _scope_units(claim: Claim, units: dict[str, bool], cand_units: set[str] | None = None,
                 stop: set[str] = SCOPE_STOPWORDS) -> tuple[set[str], list[str]]:
    """Narrow to the files an experiment probably uses, from general (section) to specific (table column).

    `units` maps each scoping unit to whether it is code (a .py file or a command launching one). A level
    that only points at non-code files (say, a config fragment named after the method) is applied only if
    those files actually set the key being checked.
    """
    allowed = set(units)
    levels = [p for p in claim.section.removeprefix("Appendix: ").split(" > ") if p]
    if claim.column:
        levels += claim.column.split(" / ")
    used: list[str] = []
    for level in levels:
        toks = _tokens(level, stop)
        if not toks:
            continue
        scored = [(sum(1 for t in toks if t in u), u) for u in allowed]
        best = max((h for h, _ in scored), default=0)
        if best == 0:
            # A specific level (say a table row group) points at no file: anything narrower would be a guess.
            break
        narrowed = {u for h, u in scored if h == best}
        if cand_units is not None and not narrowed & cand_units and not any(units[u] for u in narrowed):
            continue
        allowed = narrowed
        used.append(level)
    return allowed, used


def _scope(claim: Claim, cands: list[Setting], units: dict[str, bool], owned: set[str],
           stop: set[str]) -> tuple[list[Setting], str | None]:
    allowed, used = _scope_units(claim, units, {_unit(c) for c in cands}, stop)
    if used:
        return [c for c in cands if _unit(c) in allowed], " > ".join(used)
    # No section title points at a file: prefer files that no other section claims.
    unowned = [c for c in cands if _unit(c) not in owned]
    if unowned and len(unowned) < len(cands):
        return unowned, UNOWNED
    return cands, None


def _top(cands: list[Setting]) -> tuple[list[Setting], list[object]]:
    cands = sorted(cands, key=lambda s: -s.priority)
    if not cands:
        return cands, []
    top_p = cands[0].priority
    distinct: list[object] = []
    for c in cands:
        if c.priority == top_p and not any(equal(c.value, d) for d in distinct):
            distinct.append(c.value)
    return cands, distinct


def _units(settings: list[Setting]) -> dict[str, bool]:
    units: dict[str, bool] = {}
    for s in settings:
        code = s.file.endswith(".py") or bool(s.target and s.target.endswith(".py"))
        units[_unit(s)] = units.get(_unit(s), False) or code
    return units


def classify(claim: Claim, settings: list[Setting], units: dict[str, bool] | None = None,
             owned: set[str] | None = None, stop: set[str] = SCOPE_STOPWORDS) -> Finding:
    units = units if units is not None else _units(settings)
    cands = [s for s in settings if s.key == claim.key]
    if not cands:
        return Finding("missing_in_code", claim.key, claim, note="no setting with this name found in the code")
    cands, scope = _scope(claim, cands, units, owned or set(), stop)
    if not cands:
        return Finding("missing_in_code", claim.key, claim, scope=scope,
                       note="not set in the files this section points to")
    cands, effective = _top(cands)
    top_p = cands[0].priority
    in_top = any(equal(v, claim.value) for v in effective)
    in_any = [c for c in cands if equal(c.value, claim.value)]
    multi = len(claim.values) > 1

    if in_top and not multi and len(effective) == 1:
        return Finding("match", claim.key, claim, cands, effective, scope)
    if in_top and not multi:
        return Finding("ambiguous", claim.key, claim, cands, effective, scope,
                       f"{len(effective)} different values at the same precedence ({cands[0].source}); "
                       "one matches, and the tool cannot tell which one this experiment used")
    if in_top and multi:
        return Finding("ambiguous", claim.key, claim, cands, effective, scope,
                       f"the paper lists several values here ({', '.join(fmt(v) for v in claim.values)})")
    if in_any:
        lower = in_any[0]
        return Finding("ambiguous", claim.key, claim, cands, effective, scope,
                       f"paper value appears only as a {lower.source} ({lower.loc}), which a {cands[0].source} "
                       f"(precedence {top_p}) likely overrides")
    if multi and any(equal(v, e) for v in claim.values for e in effective):
        return Finding("ambiguous", claim.key, claim, cands, effective, scope,
                       "one of the several values the paper lists matches the code")
    if len(effective) > 1:
        return Finding("ambiguous", claim.key, claim, cands, effective, scope,
                       f"the code sets {len(effective)} different values at the same precedence and none equals "
                       "the paper; the tool cannot tell which one this experiment used")
    if cands[0].source == "code_default":
        return Finding("ambiguous", claim.key, claim, cands, effective, scope,
                       "the only value found is a function-signature default, which callers often override")
    if scope == UNOWNED:
        return Finding("ambiguous", claim.key, claim, cands, effective, scope,
                       "no section or table title points at a specific file, so the code compared here may "
                       "belong to a different experiment")
    return Finding("conflict", claim.key, claim, cands, effective, scope)


CORE_GROUPS = [("learning_rate",), ("batch_size",), ("epochs", "train_steps"), ("seed",), ("optimizer",)]


def align(paper: Paper, settings: list[Setting]) -> list[Finding]:
    units = _units(settings)
    # The method's own name ("LoRA: ...") shows up in most paths and says nothing about which script.
    name = paper.title.split(":", 1)[0] if ":" in paper.title else ""
    stop = SCOPE_STOPWORDS | set(_tokens(name))
    owned: set[str] = set()
    for c in paper.claims:
        allowed, used = _scope_units(c, units, stop=stop)
        if used:
            owned |= allowed
    findings = [classify(c, settings, units, owned, stop) for c in paper.claims]
    claimed = {c.key for c in paper.claims}
    for group in CORE_GROUPS:
        if any(k in claimed or mentions(paper, k) for k in group):
            continue
        for k in group:
            cands, effective = _top([s for s in settings if s.key == k])
            if cands:
                findings.append(Finding("missing_in_paper", k, None, cands, effective,
                                        note="the code sets this but the paper never mentions it"))
                break
    order = {c: i for i, c in enumerate(CATEGORIES)}
    key_order = {k.name: i for i, k in enumerate(KEYS)}
    findings.sort(key=lambda f: (order[f.category], key_order.get(f.key, 99), f.claim.loc if f.claim else ""))
    return findings
