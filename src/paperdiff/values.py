"""Turn the many ways papers and code write numbers into comparable values."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

WORD_NUMBERS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "sixteen": 16, "twenty": 20, "thirty-two": 32, "sixty-four": 64,
}

_LATEX_WRAPPERS = re.compile(r"\\(?:texttt|mathrm|text|textbf|textit|mathbf|emph|num|si)\s*\{([^{}]*)\}")
_LATEX_SPACES = re.compile(r"\\[,;:! ]|~|\\quad|\\qquad")

# 3 x 10^{-4}, 10^{-4}, 1e-4, 5,000, 0.1, 50k, 1M, 10%
NUM_RE = re.compile(
    r"""
    (?<![\w.])
    (?:
        10\s*\^\s*\{?\s*(?P<exp3>[-+−]?\d+)\s*\}?
        |
        10\s*(?P<exp4>−\d+)  # PDF text flattens a superscript: 10⁻⁵ comes out as "10−5" (U+2212)
        |
        (?P<mant>(?:\d{1,3}(?:,\d{3})+(?!\d)|\d+(?:\.\d+)?|\.\d+))
        (?:\s*[eE]\s*(?P<exp>[-+−]?\d+))?
        (?:\s*(?:x|\*)\s*10\s*\^\s*\{?\s*(?P<exp2>[-+−]?\d+)\s*\}?)?
    )
    (?P<suffix>\s*[kKM](?![A-Za-z]))?
    (?P<pct>\s*\\?%)?
    (?![A-Za-z0-9_])
    """,
    re.X,
)

WORD_NUM_RE = re.compile(r"\b(" + "|".join(sorted(WORD_NUMBERS, key=len, reverse=True)) + r")\b", re.I)


def clean_latex(s: str) -> str:
    """Strip the LaTeX markup that sits around numbers, keep character content."""
    prev = None
    while prev != s:
        prev = s
        s = _LATEX_WRAPPERS.sub(r"\1", s)
    s = _LATEX_SPACES.sub(" ", s)
    s = s.replace("\\times", "x").replace("\\cdot", "x").replace("$", "")
    s = s.replace("\\{", "{").replace("\\}", "}")
    return s


@dataclass(frozen=True)
class Num:
    value: float
    start: int
    end: int
    raw: str
    pct: bool = False


def find_numbers(s: str, words: bool = False) -> list[Num]:
    """Find numbers in already-cleaned text, in order of appearance."""
    out: list[Num] = []
    for m in NUM_RE.finditer(s):
        if m.group("exp3") is not None or m.group("exp4") is not None:
            v = 10.0 ** int((m.group("exp3") or m.group("exp4")).replace("−", "-"))
        else:
            v = float(m.group("mant").replace(",", ""))
            if m.group("exp"):
                v *= 10.0 ** int(m.group("exp").replace("−", "-"))
            if m.group("exp2"):
                v *= 10.0 ** int(m.group("exp2").replace("−", "-"))
        suffix = (m.group("suffix") or "").strip()
        if suffix in ("k", "K"):
            v *= 1_000
        elif suffix == "M":
            v *= 1_000_000
        if m.group("pct"):
            v /= 100.0
        v = float(f"{v:.12g}")
        out.append(Num(v, m.start(), m.end(), m.group(0).strip(), bool(m.group("pct"))))
    if words:
        for m in WORD_NUM_RE.finditer(s):
            out.append(Num(float(WORD_NUMBERS[m.group(1).lower()]), m.start(), m.end(), m.group(1)))
        out.sort(key=lambda n: n.start)
    return out


def parse_scalar(raw: object) -> float | str | bool | None:
    """Normalize a value read from code/config into float, str, bool or None."""
    if raw is None or isinstance(raw, bool):
        return raw
    if isinstance(raw, (int, float)):
        return float(raw)
    s = str(raw).strip().strip("'\"")
    if s.lower() in ("true", "false"):
        return s.lower() == "true"
    if s.lower() in ("none", "null", "~", ""):
        return None
    s_num = s.replace("_", "")
    try:
        return float(s_num)
    except ValueError:
        pass
    nums = find_numbers(clean_latex(s))
    if len(nums) == 1 and nums[0].start == 0 and nums[0].end == len(clean_latex(s)):
        return nums[0].value
    return s


def norm_str(s: str) -> str:
    s = s.rsplit(".", 1)[-1] if re.match(r"^[\w.]+$", s) else s
    return re.sub(r"[^a-z0-9]", "", s.lower())


def equal(a: object, b: object) -> bool:
    if isinstance(a, float) and isinstance(b, float):
        return math.isclose(a, b, rel_tol=1e-6, abs_tol=1e-12)
    if isinstance(a, str) and isinstance(b, str):
        return norm_str(a) == norm_str(b)
    return False


def fmt(v: object) -> str:
    if isinstance(v, float):
        if v == int(v) and abs(v) < 1e15:
            return str(int(v))
        return f"{v:g}"
    return str(v)
