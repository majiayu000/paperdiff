"""Extract settings from a code repository without executing it."""

from __future__ import annotations

import ast
import fnmatch
import warnings
import json
import re
import shlex
from dataclasses import dataclass
from pathlib import Path

import yaml

from .keys import key_for_code_name
from .values import parse_scalar

# Higher wins when guessing which value is in effect (docs/design.md §4).
PRIORITY = {"command": 4, "config": 3, "argparse_default": 2, "flag_default": 2, "code_default": 1, "code_literal": 1}

SKIP_DIRS = {".git", "node_modules", "venv", ".venv", "env", "site-packages", "__pycache__", "build", "dist",
             "third_party", "tests", "test", ".github", ".tox", ".mypy_cache"}
SKIP_FILES = {"environment.yml", "environment.yaml", ".pre-commit-config.yaml", "package.json",
              "package-lock.json", "tsconfig.json", "mkdocs.yml", "codecov.yml", ".readthedocs.yaml"}
MAX_FILE_BYTES = 1_000_000
OPTIMIZER_CLASSES = {"Adam", "AdamW", "SGD", "RMSprop", "Adagrad", "Adadelta", "Adafactor", "LAMB", "Lamb",
                     "Lion", "Adamax", "NAdam", "RAdam", "AdamWeightDecayOptimizer", "AdamOptimizer",
                     "GradientDescentOptimizer", "MomentumOptimizer", "Muon"}
OPTIMIZER_KWARGS = {"lr": "learning_rate", "learning_rate": "learning_rate", "weight_decay": "weight_decay",
                    "weight_decay_rate": "weight_decay", "momentum": "momentum", "eps": "adam_epsilon",
                    "epsilon": "adam_epsilon"}
SEED_CALLS = {"manual_seed", "manual_seed_all", "seed", "set_seed", "seed_everything", "set_random_seed"}
LAUNCHERS = re.compile(r"(?:^|\s|/)(?:python[\d.]*|torchrun|accelerate|deepspeed|horovodrun|mpirun|srun)\b")


@dataclass
class Setting:
    key: str
    name: str  # identifier as written in the code
    value: float | str | bool | None
    source: str  # one of PRIORITY
    file: str
    line: int
    text: str  # the source line, trimmed
    target: str | None = None  # for commands: the script they launch

    @property
    def loc(self) -> str:
        return f"{self.file}:{self.line}"

    @property
    def priority(self) -> int:
        return PRIORITY[self.source]

    def to_json(self) -> dict:
        d = {"key": self.key, "name": self.name, "value": self.value, "source": self.source, "loc": self.loc,
             "text": self.text}
        if self.target:
            d["target"] = self.target
        return d


def _mapped(name: str, value: object) -> tuple[str, float | str | bool | None] | None:
    key = key_for_code_name(name)
    if key is None:
        return None
    v = parse_scalar(value)
    leaf = name.strip("-").rsplit(".", 1)[-1].replace("-", "_").lower()
    if isinstance(v, float) and leaf in key.code_transforms:
        v = key.code_transforms[leaf](v)
    if key.kind in ("int", "float") and not isinstance(v, float):
        return None
    if key.kind == "str" and not isinstance(v, str):
        return None
    return key.name, v


# ---------------------------------------------------------------- Python


def _literal(node: ast.AST) -> object:
    """Evaluate constants and simple numeric expressions such as 1e-3, -1, 2**10, 3 * 10**-4."""
    try:
        return ast.literal_eval(node)
    except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
        pass
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Mult, ast.Pow, ast.Div, ast.Add, ast.Sub)):
        left, right = _literal(node.left), _literal(node.right)
        if isinstance(left, (int, float)) and isinstance(right, (int, float)) and not isinstance(left, bool):
            try:
                if isinstance(node.op, ast.Pow):
                    return left ** right if abs(right) < 64 else None
                return {ast.Mult: left * right, ast.Add: left + right, ast.Sub: left - right,
                        ast.Div: left / right if right else None}[type(node.op)]
            except (OverflowError, ZeroDivisionError):
                return None
    return _NOT_LITERAL


_NOT_LITERAL = object()


def _call_name(func: ast.AST) -> str:
    if isinstance(func, ast.Attribute):
        return func.attr
    if isinstance(func, ast.Name):
        return func.id
    return ""


def _python_settings(rel: str, src: str) -> list[Setting]:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)  # warnings about the target repo's code, not ours
            tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return []
    lines = src.splitlines()
    out: list[Setting] = []

    def add(name: str, value: object, source: str, node: ast.AST, key: str | None = None) -> None:
        if value is _NOT_LITERAL:
            return
        if key is None:
            mapped = _mapped(name, value)
            if mapped is None:
                return
            key, v = mapped
        else:
            v = parse_scalar(value)
            if v is None:
                return
        ln = getattr(node, "lineno", 1)
        out.append(Setting(key, name, v, source, rel, ln, lines[ln - 1].strip()[:200] if ln <= len(lines) else ""))

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fname = _call_name(node.func)
            if fname == "add_argument":
                opts = [a.value for a in node.args if isinstance(a, ast.Constant) and isinstance(a.value, str)]
                longs = [o for o in opts if o.startswith("--")] or opts
                default = next((k.value for k in node.keywords if k.arg == "default"), None)
                if longs and default is not None:
                    add(longs[0], _literal(default), "argparse_default", node)
            elif fname.startswith("DEFINE_") and node.args:
                first = node.args[0]
                if isinstance(first, ast.Constant) and isinstance(first.value, str):
                    default = node.args[1] if len(node.args) > 1 else next(
                        (k.value for k in node.keywords if k.arg == "default"), None)
                    if default is not None:
                        add(first.value, _literal(default), "flag_default", node)
            elif fname in OPTIMIZER_CLASSES:
                add("optimizer", fname, "code_literal", node, key="optimizer")
                for kw in node.keywords:
                    if kw.arg in OPTIMIZER_KWARGS:
                        add(kw.arg, _literal(kw.value), "code_literal", node, key=OPTIMIZER_KWARGS[kw.arg])
                    elif kw.arg == "betas":
                        betas = _literal(kw.value)
                        if isinstance(betas, (tuple, list)) and len(betas) == 2:
                            add("betas[0]", betas[0], "code_literal", node, key="adam_beta1")
                            add("betas[1]", betas[1], "code_literal", node, key="adam_beta2")
            elif fname in SEED_CALLS and node.args:
                add(fname, _literal(node.args[0]), "code_literal", node, key="seed")
            else:
                for kw in node.keywords:
                    if kw.arg:
                        add(kw.arg, _literal(kw.value), "code_literal", node)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = node.args
            pos = args.posonlyargs + args.args
            for a, d in zip(pos[len(pos) - len(args.defaults):], args.defaults):
                add(a.arg, _literal(d), "code_default", d)
            for a, d in zip(args.kwonlyargs, args.kw_defaults):
                if d is not None:
                    add(a.arg, _literal(d), "code_default", d)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.value is not None:
            add(node.target.id, _literal(node.value), "code_default", node)
    # Plain `name = value` only at module or class level: inside functions these are mostly counters.
    for scope in [tree, *(n for n in tree.body if isinstance(n, ast.ClassDef))]:
        for node in scope.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                add(node.targets[0].id, _literal(node.value), "code_literal", node)
    return out


# ---------------------------------------------------------------- YAML / JSON


def _yaml_settings(rel: str, src: str) -> list[Setting]:
    try:
        docs = list(yaml.compose_all(src, Loader=yaml.SafeLoader))
    except yaml.YAMLError:
        return []
    lines = src.splitlines()
    out: list[Setting] = []

    def walk(node: yaml.Node, path: str) -> None:
        if isinstance(node, yaml.MappingNode):
            for k, v in node.value:
                if isinstance(k, yaml.ScalarNode):
                    walk(v, f"{path}.{k.value}" if path else str(k.value))
        elif isinstance(node, yaml.ScalarNode) and path:
            mapped = _mapped(path, node.value)
            if mapped:
                ln = node.start_mark.line + 1
                out.append(Setting(mapped[0], path, mapped[1], "config", rel, ln, lines[ln - 1].strip()[:200]))

    for doc in docs:
        if doc is not None:
            walk(doc, "")
    return out


def _json_settings(rel: str, src: str) -> list[Setting]:
    try:
        data = json.loads(src)
    except (json.JSONDecodeError, ValueError):
        return []
    lines = src.splitlines()
    out: list[Setting] = []

    def walk(obj: object, path: str) -> None:
        if isinstance(obj, dict):
            for k, v in obj.items():
                walk(v, f"{path}.{k}" if path else str(k))
        elif path and not isinstance(obj, (list, dict)):
            mapped = _mapped(path, obj)
            if mapped:
                leaf = path.rsplit(".", 1)[-1]
                ln = next((i for i, t in enumerate(lines, 1) if f'"{leaf}"' in t), 1)
                out.append(Setting(mapped[0], path, mapped[1], "config", rel, ln, lines[ln - 1].strip()[:200]))

    walk(data, "")
    return out


# ---------------------------------------------------------------- commands (README, shell scripts)


SHELL_ASSIGN = re.compile(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=(\S+)\s*$")


def _command_lines(rel: str, src: str) -> list[tuple[int, str]]:
    """(first line number, logical command) for each launcher command, joining backslash continuations."""
    is_md = rel.lower().endswith(".md")
    out: list[tuple[int, str]] = []
    in_code = not is_md
    buf, start = "", 0
    for i, raw in enumerate(src.splitlines(), start=1):
        line = raw.rstrip()
        if is_md and line.lstrip().startswith("```"):
            in_code = not in_code
            buf = ""
            continue
        if not in_code and not (is_md and raw.startswith("    ")):
            continue
        if not buf:
            start = i
        cont = line.endswith("\\")
        buf += " " + (line[:-1] if cont else line)
        if not cont:
            if LAUNCHERS.search(buf):
                out.append((start, buf.strip().lstrip("$ ").strip()))
            buf = ""
    return out


def _command_settings(rel: str, src: str) -> list[Setting]:
    variables: dict[str, str] = {}
    if not rel.lower().endswith(".md"):
        for raw in src.splitlines():
            m = SHELL_ASSIGN.match(raw)
            if m:
                variables[m.group(1)] = m.group(2).strip("'\"")
    lines = src.splitlines()
    out: list[Setting] = []
    for ln, cmd in _command_lines(rel, src):
        try:
            tokens = shlex.split(cmd, comments=True)
        except ValueError:
            tokens = cmd.split()
        target = next((t for t in tokens if t.endswith(".py")), None)
        if target is None and "-m" in tokens and tokens.index("-m") + 1 < len(tokens):
            target = tokens[tokens.index("-m") + 1]
        i = 0
        while i < len(tokens):
            tok = tokens[i]
            name = value = None
            if tok.startswith("-") and len(tok) > 1 and not re.match(r"^-\d", tok):
                if "=" in tok:
                    name, value = tok.split("=", 1)
                elif i + 1 < len(tokens) and not tokens[i + 1].startswith("-"):
                    name, value = tok, tokens[i + 1]
                    i += 1
            elif "=" in tok and re.match(r"^\+{0,2}[A-Za-z_][\w.]*=", tok):
                name, value = tok.lstrip("+").split("=", 1)
            i += 1
            if name is None or value is None:
                continue
            value = re.sub(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)\}?", lambda m: variables.get(m.group(1), m.group(0)), value)
            if "$" in value:
                continue
            mapped = _mapped(name, value)
            if mapped:
                out.append(Setting(mapped[0], name, mapped[1], "command", rel, ln, lines[ln - 1].strip()[:200],
                                   target=target))
    return out


# ---------------------------------------------------------------- repository walk


def _skipped(rel: Path, excludes: list[str]) -> bool:
    if any(part in SKIP_DIRS for part in rel.parts[:-1]) or rel.name in SKIP_FILES:
        return True
    return any(fnmatch.fnmatch(str(rel), pat) for pat in excludes)


def extract_repo(root: Path, excludes: list[str] | None = None) -> list[Setting]:
    excludes = excludes or []
    settings: list[Setting] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        rel = path.relative_to(root)
        if _skipped(rel, excludes):
            continue
        suffix = path.suffix.lower()
        if suffix not in (".py", ".yaml", ".yml", ".json", ".sh", ".md", ".bash"):
            continue
        if suffix == ".md" and not path.name.lower().startswith("readme"):
            continue  # other notes (issue logs, changelogs) are not instructions for running the code
        if path.stat().st_size > MAX_FILE_BYTES:
            continue
        src = path.read_text(errors="replace")
        r = str(rel)
        if suffix == ".py":
            settings.extend(_python_settings(r, src))
        elif suffix in (".yaml", ".yml"):
            settings.extend(_yaml_settings(r, src))
        elif suffix == ".json":
            settings.extend(_json_settings(r, src))
        else:
            settings.extend(_command_settings(r, src))
    return settings
