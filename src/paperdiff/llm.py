"""Optional LLM pass for method-level differences (`paperdiff check --llm`).

Off by default. When enabled, paper sections and the code files that share the most vocabulary with them are sent to
the configured provider, which is asked for differences between what the paper describes and what the code does.
Every reported difference must cite a paper line and a code line, each with a verbatim quote; both are checked
locally and anything that does not check out is dropped. Responses are cached by a hash of the request.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import time
import urllib.error
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from .code import MAX_FILE_BYTES, _skipped
from .fetch import cache_dir
from .paper import SECTION_RE, Line

# USD per million tokens (input, output), from Anthropic's published price list. Other models need --llm-price.
PRICES = {"claude-sonnet-5-5": (2.0, 10.0), "claude-opus-5-5": (4.0, 20.0), "claude-haiku-5-5": (0.10, 0.50)}
DEFAULT_MODELS = {"anthropic": "claude-sonnet-5-5"}
DEFAULT_KEY_ENV = {"anthropic": "ANTHROPIC_API_KEY", "openai": "OPENAI_API_KEY"}
MAX_OUTPUT_TOKENS = 8000
CHARS_PER_TOKEN = 3.5  # conservative estimate used only to stay under the spending cap before a call
SKIP_SECTIONS = re.compile(r"introduction|related work|conclusion|acknowledg|references|bibliography|broader impact|"
                           r"limitations|ethics|reproducibility statement|author contributions", re.I)
WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9]{3,}")

SYSTEM = """You compare a section of a research paper with the code that implements it.
Report only concrete differences between what the paper states and what the code does: a different formula, loss
term, normalisation, layer order, data processing step, sampling rule, evaluation rule or default value. Do not
report style, missing comments, or things the paper does not describe.
Every difference must cite one paper line and one code line using the location labels exactly as they appear before
the "|" in the input, and quote a short verbatim fragment (5-120 characters) copied from that exact line.
If you find no clear difference, return an empty list. Do not guess."""

SCHEMA = {
    "type": "object",
    "properties": {
        "differences": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"},
                    "paper_loc": {"type": "string"},
                    "paper_quote": {"type": "string"},
                    "code_loc": {"type": "string"},
                    "code_quote": {"type": "string"},
                    "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                    "reason": {"type": "string"},
                },
                "required": ["summary", "paper_loc", "paper_quote", "code_loc", "code_quote", "confidence", "reason"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["differences"],
    "additionalProperties": False,
}


class LLMError(RuntimeError):
    pass


class BudgetExceeded(LLMError):
    pass


@dataclass
class LLMConfig:
    provider: str = "anthropic"  # "anthropic" | "openai" (any OpenAI-compatible endpoint)
    model: str | None = None
    base_url: str | None = None
    api_key_env: str | None = None
    timeout_s: float = 180.0
    retries: int = 2
    max_usd: float = 2.0
    max_chunks: int = 6
    chunk_chars: int = 40_000
    price: tuple[float, float] | None = None  # USD per million input/output tokens; overrides PRICES

    def resolved(self) -> "LLMConfig":
        model = self.model or DEFAULT_MODELS.get(self.provider)
        if not model:
            raise LLMError(f"--llm-model is required for provider {self.provider!r}")
        key_env = self.api_key_env or DEFAULT_KEY_ENV.get(self.provider)
        if not key_env:
            raise LLMError(f"--llm-api-key-env is required for provider {self.provider!r}")
        price = self.price or PRICES.get(model)
        if price is None:
            raise LLMError(f"no price known for {model!r}; pass --llm-price INPUT,OUTPUT (USD per million tokens)")
        return LLMConfig(self.provider, model, self.base_url, key_env, self.timeout_s, self.retries, self.max_usd,
                         self.max_chunks, self.chunk_chars, price)


@dataclass
class Chunk:
    section: str
    paper_lines: list[Line]
    code_files: list[str]
    score: float


@dataclass
class LLMResult:
    findings: list[dict] = field(default_factory=list)
    dropped: list[dict] = field(default_factory=list)
    stats: dict = field(default_factory=dict)

    def to_json(self) -> dict:
        return {"findings": self.findings, "dropped": self.dropped, "stats": self.stats}


# ---------------------------------------------------------------- chunking


def _paper_sections(lines: list[Line]) -> list[tuple[str, list[Line]]]:
    """Group paper lines by section (LaTeX) or by page pair (PDF)."""
    groups: list[tuple[str, list[Line]]] = []
    for ln in lines:
        if ln.page is not None:
            title = f"pages {ln.page - (ln.page - 1) % 2}-{ln.page - (ln.page - 1) % 2 + 1}"
        else:
            m = SECTION_RE.search(ln.text)
            title = re.sub(r"\s+", " ", m.group(2)).strip() if m and m.group(1) != "subsubsection" else None
        if title is not None and (not groups or groups[-1][0] != title):
            groups.append((title, []))
        elif not groups:
            groups.append(("front matter", []))
        if ln.text.strip():
            groups[-1][1].append(ln)
    return [(t, ls) for t, ls in groups if ls and not SKIP_SECTIONS.search(t)]


def _code_files(root: Path, excludes: list[str]) -> dict[str, str]:
    files = {}
    for path in sorted(root.rglob("*.py")):
        rel = path.relative_to(root)
        if path.is_file() and not path.is_symlink() and not _skipped(rel, excludes) \
                and path.stat().st_size <= MAX_FILE_BYTES:
            files[str(rel)] = path.read_text(errors="replace")
    return files


def _words(text: str) -> Counter:
    return Counter(w.lower() for w in WORD_RE.findall(text))


def build_chunks(lines: list[Line], code: dict[str, str], cfg: LLMConfig) -> list[Chunk]:
    """Pair each paper section with the code files that share the most distinctive words, best pairs first."""
    file_words = {f: set(_words(src)) for f, src in code.items()}
    df = Counter(w for ws in file_words.values() for w in ws)
    n = max(len(code), 1)
    chunks = []
    for title, sec_lines in _paper_sections(lines):
        text = "\n".join(ln.text for ln in sec_lines)
        words = set(_words(text))
        scored = []
        for f, ws in file_words.items():
            s = sum(math.log(1 + n / df[w]) for w in words & ws)
            if s > 0:
                scored.append((s, f))
        scored.sort(reverse=True)
        budget = cfg.chunk_chars - len(text)
        chosen, total = [], 0.0
        for s, f in scored[:5]:
            if len(code[f]) <= budget and len(chosen) < 2:
                chosen.append(f)
                budget -= len(code[f])
                total += s
        if chosen and len(text) < cfg.chunk_chars:
            chunks.append(Chunk(title, sec_lines, chosen, total))
    chunks.sort(key=lambda c: -c.score)
    return chunks[: cfg.max_chunks]


def render_chunk(chunk: Chunk, code: dict[str, str]) -> str:
    out = [f"PAPER SECTION: {chunk.section}"]
    out += [f"{ln.loc}| {ln.text}" for ln in chunk.paper_lines]
    for f in chunk.code_files:
        out.append(f"\nCODE FILE: {f}")
        out += [f"{f}:{i}| {t}" for i, t in enumerate(code[f].splitlines(), 1)]
    return "\n".join(out)


# ---------------------------------------------------------------- provider calls


def _norm(s: str) -> str:
    s = re.sub(r"\\[a-zA-Z]+\s*", " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def _api_key(cfg: LLMConfig) -> str:
    key = os.environ.get(cfg.api_key_env or "")
    if not key:
        raise LLMError(f"environment variable {cfg.api_key_env} is not set; --llm needs an API key there")
    return key


def _call_anthropic(cfg: LLMConfig, user: str) -> tuple[str, dict]:
    try:
        import anthropic
    except ImportError as e:
        raise LLMError("the anthropic package is not installed; install paperdiff with the 'llm' extra") from e
    client = anthropic.Anthropic(api_key=_api_key(cfg), base_url=cfg.base_url, timeout=cfg.timeout_s,
                                 max_retries=cfg.retries)
    resp = client.beta.messages.create(
        model=cfg.model, max_tokens=MAX_OUTPUT_TOKENS, system=SYSTEM,
        messages=[{"role": "user", "content": user}],
        output_config={"effort": "medium", "format": {"type": "json_schema", "schema": SCHEMA}},
        betas=["server-side-fallback-2026-07-01"], fallbacks="default",
    )
    usage = {"input_tokens": resp.usage.input_tokens, "output_tokens": resp.usage.output_tokens}
    if resp.stop_reason == "refusal":
        return '{"differences": []}', dict(usage, refusal=True)
    text = next((b.text for b in resp.content if b.type == "text"), "")
    return text, usage


def _call_openai(cfg: LLMConfig, user: str) -> tuple[str, dict]:
    base = (cfg.base_url or "https://api.openai.com/v1").rstrip("/")
    body = json.dumps({
        "model": cfg.model, "max_tokens": MAX_OUTPUT_TOKENS,
        "messages": [{"role": "system", "content": SYSTEM + "\nAnswer with a JSON object: "
                      + json.dumps(SCHEMA)}, {"role": "user", "content": user}],
        "response_format": {"type": "json_object"},
    }).encode()
    last: Exception | None = None
    for attempt in range(cfg.retries + 1):
        req = urllib.request.Request(f"{base}/chat/completions", data=body, headers={
            "Content-Type": "application/json", "Authorization": f"Bearer {_api_key(cfg)}"})
        try:
            with urllib.request.urlopen(req, timeout=cfg.timeout_s) as resp:
                data = json.load(resp)
            usage = data.get("usage") or {}
            return data["choices"][0]["message"]["content"], {
                "input_tokens": usage.get("prompt_tokens", 0), "output_tokens": usage.get("completion_tokens", 0)}
        except urllib.error.HTTPError as e:
            last = e
            if e.code not in (408, 409, 429) and e.code < 500:
                raise LLMError(f"{base}/chat/completions returned HTTP {e.code}") from e
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
        time.sleep(2 ** attempt)
    raise LLMError(f"{base}/chat/completions failed after {cfg.retries + 1} attempts: {last}")


CALLERS = {"anthropic": _call_anthropic, "openai": _call_openai}


class Session:
    """Calls the provider with caching and a spending cap."""

    def __init__(self, cfg: LLMConfig, cache: Path | None = None, caller=None):
        self.cfg = cfg
        self.cache = cache or cache_dir() / "llm"
        self.caller = caller or CALLERS[cfg.provider]
        self.spent = 0.0
        self.calls = self.cache_hits = 0
        self.tokens = Counter()

    def _cost(self, usage: dict) -> float:
        pin, pout = self.cfg.price
        return usage.get("input_tokens", 0) * pin / 1e6 + usage.get("output_tokens", 0) * pout / 1e6

    def ask(self, user: str) -> dict:
        key = hashlib.sha256(json.dumps([self.cfg.provider, self.cfg.model, self.cfg.base_url, SYSTEM, SCHEMA, user],
                                        sort_keys=True).encode()).hexdigest()
        path = self.cache / f"{key}.json"
        if path.exists():
            self.cache_hits += 1
            return json.loads(path.read_text())
        pin, pout = self.cfg.price
        worst = len(user) / CHARS_PER_TOKEN * pin / 1e6 + MAX_OUTPUT_TOKENS * pout / 1e6
        if self.spent + worst > self.cfg.max_usd:
            raise BudgetExceeded(f"next call could cost up to ${worst:.2f}; ${self.spent:.2f} of the "
                                 f"${self.cfg.max_usd:.2f} cap already spent")
        text, usage = self.caller(self.cfg, user)
        self.calls += 1
        self.spent += self._cost(usage)
        self.tokens.update({k: v for k, v in usage.items() if isinstance(v, int)})
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError:
            parsed = {"differences": [], "unparseable": True}
        record = {"response": parsed, "usage": usage, "cost_usd": round(self._cost(usage), 6)}
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(record))
        return record


# ---------------------------------------------------------------- validation


def _window(index: dict[str, list[str]], loc: str, radius: int = 2) -> str | None:
    """Text of the cited line and its neighbours, or None if the location does not exist."""
    m = re.match(r"^(.*?):(?:p(\d+):L)?(\d+)$", loc.strip())
    if not m:
        return None
    file, page, line = m.group(1), m.group(2), int(m.group(3))
    key = f"{file}:p{page}" if page else file
    lines = index.get(key)
    if lines is None or not 1 <= line <= len(lines) or lines[line - 1] is None:
        return None
    return " ".join(t for t in lines[max(0, line - 1 - radius): line + radius] if t)


def validate(item: dict, paper_index: dict, code_index: dict) -> str | None:
    """Return why an LLM finding must be dropped, or None if both citations check out."""
    for side, index in (("paper", paper_index), ("code", code_index)):
        loc, quote = (item.get(f"{side}_loc") or "").strip(), (item.get(f"{side}_quote") or "").strip()
        if not loc or not quote:
            return f"missing {side} citation"
        window = _window(index, loc)
        if window is None:
            return f"{side} location {loc} does not exist"
        if len(_norm(quote)) < 3 or _norm(quote) not in _norm(window):
            return f"{side} quote not found at {loc}"
    return None


def _paper_index(lines: list[Line]) -> dict[str, list[str | None]]:
    index: dict[str, list[str | None]] = {}
    for ln in lines:
        key = f"{ln.file}:p{ln.page}" if ln.page is not None else ln.file
        rows = index.setdefault(key, [])
        while len(rows) < ln.line:
            rows.append(None)
        rows[ln.line - 1] = ln.text
    return index


def run(lines: list[Line], repo: Path, cfg: LLMConfig, excludes: list[str] | None = None,
        session: Session | None = None) -> LLMResult:
    cfg = cfg.resolved()
    session = session or Session(cfg)
    code = _code_files(repo, excludes or [])
    chunks = build_chunks(lines, code, cfg)
    paper_index = _paper_index(lines)
    code_index = {f: src.splitlines() for f, src in code.items()}
    result = LLMResult()
    seen: set[tuple] = set()
    stopped = None
    for chunk in chunks:
        try:
            record = session.ask(render_chunk(chunk, code))
        except BudgetExceeded as e:
            stopped = str(e)
            break
        for item in record["response"].get("differences", []):
            sig = (item.get("paper_loc"), item.get("code_loc"), item.get("summary"))
            if sig in seen:  # overlapping chunks can report the same difference twice
                continue
            seen.add(sig)
            reason = validate(item, paper_index, code_index)
            out = {"kind": "llm", "section": chunk.section, "summary": item.get("summary", ""),
                   "paper": {"loc": item.get("paper_loc"), "quote": item.get("paper_quote")},
                   "code": {"loc": item.get("code_loc"), "quote": item.get("code_quote")},
                   "confidence": item.get("confidence"), "reason": item.get("reason", "")}
            if reason:
                result.dropped.append(dict(out, dropped_because=reason))
            else:
                result.findings.append(out)
    result.stats = {"provider": cfg.provider, "model": cfg.model, "chunks": len(chunks), "calls": session.calls,
                    "cache_hits": session.cache_hits, "cost_usd": round(session.spent, 4),
                    "tokens": dict(session.tokens), "proposed": len(result.findings) + len(result.dropped),
                    "kept": len(result.findings), "dropped": len(result.dropped), "stopped": stopped}
    return result
