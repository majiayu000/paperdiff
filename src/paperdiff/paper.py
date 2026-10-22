"""Extract experimental-setting claims from a paper (LaTeX source first, PDF as fallback)."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .keys import KEYS, KEYS_BY_NAME, PHRASES, Key
from .values import Num, clean_latex, find_numbers

COMMENT_RE = re.compile(r"(?<!\\)%.*$")
INPUT_RE = re.compile(r"\\(?:input|include|subfile)\s*\{([^}]+)\}")
TITLE_RE = re.compile(r"\\(?:icml)?title\*?\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
SECTION_RE = re.compile(r"\\(section|subsection|subsubsection)\*?\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
FIGURE_BEGIN = re.compile(r"\\begin\{(figure\*?|wrapfigure|tikzpicture)\}")
FIGURE_END = re.compile(r"\\end\{(figure\*?|wrapfigure|tikzpicture)\}")
TABULAR_BEGIN = re.compile(r"\\begin\{(tabular\*?|tabularx|longtable|tabulary)\}")
TABULAR_END = re.compile(r"\\end\{(tabular\*?|tabularx|longtable|tabulary)\}")
SENTENCE_SPLIT = re.compile(r"(?<=[.;:])\s+(?=[A-Z\\(])")
CMD_WITH_ARGS = re.compile(r"\\(?:multirow|multicolumn)\s*\{[^}]*\}\s*\{[^}]*\}\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
BARE_CMD = re.compile(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?")
CITE_RE = re.compile(r"\\(?:cite|citep|citet|ref|eqref|label|url|href)\w*\s*(?:\[[^\]]*\])?\s*\{[^}]*\}")

# Text between a setting name and its value that means the number is not the value itself.
BETWEEN_REJECT = re.compile(r"\b(?:factor|by|every|per|after|than|times|from|multipl\w*|divid\w*|up to|ratio)\b", re.I)
# A unit right after the number means it measures something other than the setting.
UNIT_AFTER = re.compile(r"^\s*(?:tokens|words|characters|GB|MB|hours?|days?|minutes?|seconds?|ms)\b", re.I)
DURATION_AFTER = re.compile(r"^\s*(?:training |gradient |optimization )?(?:steps|iterations|updates|epochs)\b", re.I)
STEPS_AFTER = re.compile(r"^\s*(?:training |gradient |optimization )?(?:steps|iterations|updates)\b", re.I)
RATIO_RE = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s*\\?%?\s*[:/]\s*(\d+(?:\.\d+)?)\s*\\?%?(?![\w.])")
WORD_NUMBER_KEYS = {"num_layers", "num_heads", "num_gpus", "epochs"}
COUNT_SKIP_BEFORE = re.compile(r"\b(?:every|each|per|after|last|within|of the)\s*$", re.I)
WINDOW_AFTER = 80
WINDOW_BEFORE = 40


@dataclass
class Line:
    file: str
    line: int
    text: str
    page: int | None = None

    @property
    def loc(self) -> str:
        if self.page is not None:
            return f"{self.file}:p{self.page}:L{self.line}"
        return f"{self.file}:{self.line}"


@dataclass
class Claim:
    key: str
    value: float | str
    raw: str
    loc: str
    file: str
    line: int
    section: str
    context: str
    origin: str  # "text" | "table"
    values: list[float | str] = field(default_factory=list)  # >1 when the paper lists several values
    column: str | None = None  # table row group and column header, "RoBERTa base LoRA / MNLI"

    def to_json(self) -> dict:
        d = {
            "key": self.key, "value": self.value, "raw": self.raw, "loc": self.loc,
            "section": self.section, "context": self.context, "origin": self.origin,
        }
        if len(self.values) > 1:
            d["values"] = self.values
        if self.column:
            d["column"] = self.column
        return d


@dataclass
class Paper:
    label: str
    kind: str  # "latex" | "pdf"
    claims: list[Claim]
    main_file: str | None
    text_blob: str  # cleaned full text, used to answer "does the paper mention X at all"
    title: str = ""


# ---------------------------------------------------------------- LaTeX loading


def _find_main(root: Path) -> Path:
    candidates = []
    for p in sorted(root.rglob("*.tex")):
        try:
            t = p.read_text(errors="replace")
        except OSError:
            continue
        if "\\documentclass" in t and "\\begin{document}" in t:
            candidates.append(p)
    if not candidates:
        raise ValueError(f"no main .tex (with \\documentclass and \\begin{{document}}) under {root}")
    for p in candidates:
        if p.name == "main.tex":
            return p
    return max(candidates, key=lambda p: p.stat().st_size)


def _resolve_input(root: Path, base: Path, name: str) -> Path | None:
    name = name.strip()
    for d in (base.parent, root):
        for cand in (d / name, d / f"{name}.tex"):
            if cand.is_file():
                return cand
    return None


class _EndOfDocument(Exception):
    pass


def load_latex(root: Path) -> tuple[list[Line], str]:
    main = _find_main(root)
    out: list[Line] = []
    seen: set[Path] = set()

    def expand(path: Path) -> None:
        if path in seen:
            return
        seen.add(path)
        rel = str(path.relative_to(root))
        for i, raw in enumerate(path.read_text(errors="replace").splitlines(), start=1):
            text = COMMENT_RE.sub("", raw)
            if "\\end{document}" in text:
                out.append(Line(rel, i, text.split("\\end{document}")[0]))
                raise _EndOfDocument
            inputs = INPUT_RE.findall(text)
            out.append(Line(rel, i, INPUT_RE.sub(" ", text)))
            for name in inputs:
                target = _resolve_input(root, path, name)
                if target is not None:
                    expand(target)

    try:
        expand(main)
    except _EndOfDocument:
        pass
    return out, str(main.relative_to(root))


def load_pdf(path: Path) -> list[Line]:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    out: list[Line] = []
    for pno, page in enumerate(reader.pages, start=1):
        for i, text in enumerate((page.extract_text() or "").splitlines(), start=1):
            out.append(Line(path.name, i, text, page=pno))
    return out


# ---------------------------------------------------------------- extraction helpers


class _Joined:
    """Several source lines joined into one string, with offsets back to lines."""

    def __init__(self, lines: list[Line], clean: bool = True):
        parts, self.starts, self.lines = [], [], []
        pos = 0
        for ln in lines:
            t = _clean(ln.text) if clean else ln.text
            self.starts.append(pos)
            self.lines.append(ln)
            parts.append(t)
            pos += len(t) + 1
        self.text = " ".join(parts)

    def line_at(self, offset: int) -> Line:
        idx = 0
        for i, s in enumerate(self.starts):
            if s <= offset:
                idx = i
            else:
                break
        return self.lines[idx]


def _clean(s: str) -> str:
    s = CITE_RE.sub("", s)
    return clean_latex(s)


RULES_RE = re.compile(r"\\(?:hline|toprule|midrule|bottomrule|cline\{[^}]*\}|cmidrule(?:\([^)]*\))?\{[^}]*\})")


def _strip_cell(s: str) -> str:
    s = CMD_WITH_ARGS.sub(r"\1", s)
    s = clean_latex(s)
    s = RULES_RE.sub(" ", s)
    s = BARE_CMD.sub(" ", s)
    s = s.replace("{", " ").replace("}", " ")
    return re.sub(r"\s+", " ", s).strip()


def _other_phrase_in(text: str, key: Key) -> bool:
    for k, rx in PHRASES:
        if k.name != key.name and rx.search(text):
            return True
    return False


BETA_PAIR = re.compile(
    r"\(\s*\\beta_?\{?1\}?\s*,\s*\\beta_?\{?2\}?\s*\)\s*=\s*\(\s*([^,()]+?)\s*,\s*([^,()]+?)\s*\)"
)


def _plausible(key: Key, n: Num, text: str) -> bool:
    if re.search(r"[A-Za-z]\($", text[:n.start]):  # m(0), f(1): a function argument, not a setting
        return False
    if re.search(r"\(\s*$", text[:n.start]) and re.match(r"\s*\)", text[n.end:]):  # "(2)": an equation number
        return False
    if key.kind == "int":
        return not n.pct and n.value >= 1 and n.value == int(n.value)
    return True


def _claims_from_sentence(sent: str, offset: int, joined: _Joined, section: str) -> list[Claim]:
    claims: list[Claim] = []
    context = re.sub(r"\s+", " ", sent).strip()
    if len(context) > 300:
        context = context[:297] + "..."

    def add(key: str, num_or_str: Num | str, pos: int, values: list | None = None, raw: str | None = None):
        ln = joined.line_at(offset + pos)
        if isinstance(num_or_str, Num):
            value, raw_v = num_or_str.value, raw or num_or_str.raw
        else:
            value, raw_v = num_or_str, raw or num_or_str
        claims.append(Claim(key, value, raw_v, ln.loc, ln.file, ln.line, section, context, "text",
                            values=values or [value]))

    beta_done = False
    for m in BETA_PAIR.finditer(sent):
        for key, grp in (("adam_beta1", 1), ("adam_beta2", 2)):
            nums = find_numbers(m.group(grp))
            if len(nums) == 1:
                add(key, nums[0], m.start(grp))
                beta_done = True

    for key, rx in PHRASES:
        if beta_done and key.name in ("adam_beta1", "adam_beta2"):
            continue
        if key.name == "train_fraction":
            # "split ... with 75:25 ratio", "a 90/10 train/validation split" -> 0.75, 0.9
            if rx.search(sent):
                for m in RATIO_RE.finditer(sent):
                    a, b = float(m.group(1)), float(m.group(2))
                    add(key.name, Num(a / (a + b), m.start(), m.end(), m.group(0)), m.start())
            continue
        if key.context and not re.search(key.context, sent):
            continue
        for m in rx.finditer(sent):
            if key.kind == "str":
                add(key.name, m.group(0), m.start())
                continue
            if key.number_before:
                lo = max(0, m.start() - WINDOW_BEFORE)
                window = sent[lo:m.start()]
                nums = find_numbers(window, words=key.name in WORD_NUMBER_KEYS)
                if not nums:
                    continue
                n = nums[-1]
                if not _plausible(key, n, window):
                    continue
                gap = window[n.end:]
                if not re.fullmatch(r"[\s\-]*(?:[\w\-]+[\s\-]+){0,2}", gap):
                    continue
                if n.raw.isalpha() and not re.fullmatch(r"[\s\-]*", gap):  # "two-layer", not "one extra layer"
                    continue
                if key.name in ("epochs", "train_steps") and COUNT_SKIP_BEFORE.search(window[:n.start]):
                    continue
                if key.name == "train_steps" and re.search(r"warm", sent[max(0, lo - 30):m.end()], re.I):
                    continue
                add(key.name, n, lo + n.start)
                continue
            window = sent[m.end():m.end() + WINDOW_AFTER]
            nums = [x for x in find_numbers(window) if not UNIT_AFTER.match(window[x.end:])
                    and (key.name == "warmup_steps" or not DURATION_AFTER.match(window[x.end:]))]
            if key.name == "warmup_steps":
                nums = [x for x in nums if STEPS_AFTER.match(window[x.end:])]
                if nums:
                    add(key.name, nums[0], m.end() + nums[0].start)
                continue
            if not nums:
                continue
            n = nums[0]
            if not _plausible(key, n, window):
                continue
            between = window[:n.start]
            if len(between) > 60 or BETWEEN_REJECT.search(between) or _other_phrase_in(between, key):
                continue
            if re.search(r"\{\s*$|\bin\s*\{", between):
                close = window.find("}", n.start)
                grid = [x for x in nums if close == -1 or x.start < close]
                add(key.name, n, m.end() + n.start, values=[x.value for x in grid],
                    raw=window[between.rfind("{"):close + 1 if close != -1 else None].strip())
                continue
            add(key.name, n, m.end() + n.start)
    # A sentence giving several values for one setting ("r = 8 and r = 64") compares them; it does not state one.
    for key_name in {c.key for c in claims}:
        group = [c for c in claims if c.key == key_name]
        distinct = list(dict.fromkeys(c.value for c in group))
        if len(distinct) > 1:
            for c in group:
                c.values = distinct
    return claims


MAKECELL_RE = re.compile(r"\\(?:makecell|shortstack)(?:\[[^\]]*\])?\{[^{}]*\}")
MULTICOL_RE = re.compile(r"\\multicolumn\s*\{(\d+)\}")


def _is_number_cell(text: str) -> bool:
    nums = find_numbers(text)
    return len(nums) == 1 and nums[0].start == 0 and nums[0].end == len(text)


def _param_key(cell_raw: str) -> Key | None:
    """The setting a row is about, if this cell names one ("Batch Size", "# Epochs", "LoRA $\\alpha$")."""
    text = clean_latex(RULES_RE.sub(" ", cell_raw)).strip()
    if not text or len(_strip_cell(cell_raw)) > 40 or re.search(r"ratio|proportion|fraction", text, re.I):
        return None
    if find_numbers(text):  # "LoRA r = 8" labels a configuration in a results table, not a setting row
        return None
    best: tuple[int, int, Key] | None = None
    for key, rx in PHRASES:
        m = rx.search(text)
        if m and (best is None or (m.start(), -len(m.group(0))) < (best[0], -best[1])):
            best = (m.start(), len(m.group(0)), key)
    if best is None:
        return None
    key = best[2]
    if key.number_before and not re.match(
        r"^\W*(?:#\s*|num(?:ber)?\.? (?:of )?|total )?(?:training )?(?:" + key.phrase + r")", text, re.I
    ):
        return None
    return key


def _table_claims(rows_joined: _Joined, section: str) -> list[Claim]:
    # Line breaks inside \makecell{a \\ b} are not row ends; blank them without shifting offsets.
    text = MAKECELL_RE.sub(lambda m: m.group(0).replace("\\\\", "  "), rows_joined.text)
    rows: list[list[tuple[int, str, str]]] = []  # (offset, raw, stripped) per cell
    pos = 0
    for row in re.split(r"\\\\", text):
        cells, cpos = [], pos
        for cell in re.split(r"(?<!\\)&", row):
            span = MULTICOL_RE.search(cell)
            for _ in range(int(span.group(1)) if span else 1):
                cells.append((cpos, cell, _strip_cell(cell)))
            cpos += len(cell) + 1
        rows.append(cells)
        pos += len(row) + 2

    header: list[str] | None = None
    group = ""
    claims: list[Claim] = []
    for cells in rows:
        texts = [c[2] for c in cells]
        if len(texts) < 2:
            continue
        idx = next((i for i in (0, 1) if i < len(cells) and _param_key(cells[i][1])), None)
        if idx is None:
            if header is None and not any(_is_number_cell(t) for t in texts if t):
                header = texts
            continue
        key = _param_key(cells[idx][1])
        if idx == 1 and texts[0]:
            group = texts[0]
        row_group = group if idx == 1 else ""
        for j in range(idx + 1, len(cells)):
            cpos, _, cell = cells[j]
            if not cell:
                continue
            col = header[j] if header and j < len(header) and header[j] else None
            col = " / ".join(x for x in (row_group, col) if x) or None
            ln = rows_joined.line_at(cpos)
            context = " | ".join(t for t in texts if t)
            if key.kind == "str":
                vals = [mm.group(0) for mm in re.finditer(key.phrase, cell)]
                if vals:
                    claims.append(Claim(key.name, vals[0], cell, ln.loc, ln.file, ln.line, section,
                                        context, "table", values=vals, column=col))
                continue
            nums = find_numbers(cell)
            if not nums:
                continue
            claims.append(Claim(key.name, nums[0].value, cell, ln.loc, ln.file, ln.line, section,
                                context, "table", values=[n.value for n in nums], column=col))
    return claims


def _section_title(s: str) -> str:
    return re.sub(r"\s+", " ", _strip_cell(s)).strip()


def extract(lines: list[Line]) -> list[Claim]:
    claims: list[Claim] = []
    sections = {"section": "", "subsection": "", "subsubsection": ""}
    in_appendix = False
    para: list[Line] = []
    table: list[Line] | None = None

    def section_path() -> str:
        parts = [sections[k] for k in ("section", "subsection", "subsubsection") if sections[k]]
        path = " > ".join(parts)
        return f"Appendix: {path}" if in_appendix else path

    def flush_para() -> None:
        if not para:
            return
        joined = _Joined(para)
        offset = 0
        for sent in SENTENCE_SPLIT.split(joined.text):
            start = joined.text.find(sent, offset)
            claims.extend(_claims_from_sentence(sent, start, joined, section_path()))
            offset = start + len(sent)
        para.clear()

    in_figure = False
    for ln in lines:
        text = ln.text
        # Figures hold plotting details (smoothing, colours), not training settings.
        if in_figure or FIGURE_BEGIN.search(text):
            in_figure = not FIGURE_END.search(text)
            flush_para()
            continue
        if table is not None:
            table.append(ln)
            if TABULAR_END.search(text):
                claims.extend(_table_claims(_Joined(table, clean=False), section_path()))
                table = None
            continue
        if TABULAR_BEGIN.search(text):
            flush_para()
            table = [ln]
            if TABULAR_END.search(text):
                claims.extend(_table_claims(_Joined(table, clean=False), section_path()))
                table = None
            continue
        if "\\appendix" in text:
            in_appendix = True
        m = SECTION_RE.search(text)
        if m:
            flush_para()
            level = m.group(1)
            sections[level] = _section_title(m.group(2))
            if level == "section":
                sections["subsection"] = ""
                sections["subsubsection"] = ""
            elif level == "subsection":
                sections["subsubsection"] = ""
            continue
        if not text.strip():
            flush_para()
            continue
        para.append(ln)
    flush_para()

    seen, unique = set(), []
    for c in claims:
        sig = (c.key, str(c.value), c.loc, c.column)
        if sig not in seen:
            seen.add(sig)
            unique.append(c)
    return unique


def load_paper(kind: str, path: Path, label: str) -> Paper:
    if kind == "latex":
        lines, main = load_latex(path)
    else:
        lines, main = load_pdf(path), None
    claims = extract(lines)
    blob = " ".join(_clean(ln.text) for ln in lines)
    m = TITLE_RE.search(" ".join(ln.text for ln in lines)) if kind == "latex" else None
    title = _section_title(m.group(1)) if m else ""
    return Paper(label, kind, claims, main, blob, title)


def mentions(paper: Paper, key_name: str) -> bool:
    """Whether the paper mentions a setting at all, even without a value we could parse."""
    key = KEYS_BY_NAME[key_name]
    flags = 0 if key.name == "optimizer" else re.I
    return re.search(key.phrase, paper.text_blob, flags) is not None


__all__ = ["Claim", "Paper", "Line", "KEYS", "load_paper", "extract", "mentions"]
