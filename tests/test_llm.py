import json
import socket

import pytest

from fixtures import paper_dir, repo_dir  # noqa: F401  (pytest fixtures)
from paperdiff import llm
from paperdiff.cli import main
from paperdiff.paper import load_paper


def recorded(differences):
    """A provider stand-in that returns a recorded response and counts calls."""
    calls = []

    def caller(cfg, user):
        calls.append(user)
        return json.dumps({"differences": differences}), {"input_tokens": 1000, "output_tokens": 200}

    caller.calls = calls
    return caller


GOOD = {"summary": "paper says 20 epochs, default is 10", "paper_loc": "sections/setup.tex:3",
        "paper_quote": "train for 20 epochs", "code_loc": "train_mnist.py:8",
        "code_quote": 'parser.add_argument("--epochs", type=int, default=10)', "confidence": "high", "reason": "r"}


def run_with(differences, paper_dir, repo_dir, tmp_path, **cfg):
    paper = load_paper("latex", paper_dir, "toy")
    caller = recorded(differences)
    config = llm.LLMConfig(**cfg).resolved()
    session = llm.Session(config, cache=tmp_path / "cache", caller=caller)
    return llm.run(paper.lines, repo_dir, config, session=session), caller


def test_citations_checked(paper_dir, repo_dir, tmp_path):
    bad_line = dict(GOOD, summary="b", code_loc="train_mnist.py:999")
    bad_quote = dict(GOOD, summary="c", paper_quote="trained for 300 epochs")
    no_code = dict(GOOD, summary="d", code_loc="", code_quote="")
    wrong_file = dict(GOOD, summary="e", paper_loc="sections/missing.tex:3")
    result, _ = run_with([GOOD, bad_line, bad_quote, no_code, wrong_file], paper_dir, repo_dir, tmp_path)
    assert [f["summary"] for f in result.findings] == [GOOD["summary"]]
    assert all(f["kind"] == "llm" for f in result.findings)
    reasons = [d["dropped_because"] for d in result.dropped]
    assert reasons == ["code location train_mnist.py:999 does not exist",
                       "paper quote not found at sections/setup.tex:3", "missing code citation",
                       "paper location sections/missing.tex:3 does not exist"]
    assert result.stats["proposed"] == 5 and result.stats["kept"] == 1


def test_cache_and_budget(paper_dir, repo_dir, tmp_path):
    first, caller = run_with([GOOD], paper_dir, repo_dir, tmp_path)
    assert caller.calls and first.stats["cost_usd"] > 0
    again, caller2 = run_with([GOOD], paper_dir, repo_dir, tmp_path)
    assert caller2.calls == [] and again.stats["cache_hits"] == first.stats["calls"]
    capped, caller3 = run_with([GOOD], paper_dir, repo_dir, tmp_path / "fresh", max_usd=0.0001)
    assert caller3.calls == [] and "cap" in capped.stats["stopped"]


def test_missing_key_is_a_clear_error(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    with pytest.raises(llm.LLMError, match="ANTHROPIC_API_KEY is not set"):
        llm._api_key(llm.LLMConfig().resolved())


def test_unknown_model_needs_a_price():
    with pytest.raises(llm.LLMError, match="--llm-price"):
        llm.LLMConfig(provider="openai", model="some-model").resolved()


def test_default_mode_makes_no_network_calls(paper_dir, repo_dir, tmp_path, monkeypatch):
    def no_network(*a, **k):
        raise AssertionError("network used")

    monkeypatch.setattr(socket, "socket", no_network)
    monkeypatch.setattr(llm, "CALLERS", {"anthropic": no_network, "openai": no_network})
    out = tmp_path / "o"
    assert main(["check", str(paper_dir), str(repo_dir), "-o", str(out)]) == 0
    assert "llm" not in json.loads((out / "report.json").read_text())
    assert "LLM" not in (out / "report.md").read_text()


def test_llm_findings_are_reported_separately(paper_dir, repo_dir, tmp_path, monkeypatch):
    monkeypatch.setenv("PAPERDIFF_CACHE", str(tmp_path / "cache"))
    monkeypatch.setitem(llm.CALLERS, "anthropic", recorded([GOOD]))
    out = tmp_path / "o"
    assert main(["check", str(paper_dir), str(repo_dir), "-o", str(out), "--llm"]) == 0
    report = json.loads((out / "report.json").read_text())
    assert report["llm"]["findings"][0]["kind"] == "llm"
    assert all(f["category"] != "llm" for f in report["findings"])
    assert "## Method-level differences (LLM" in (out / "report.md").read_text()
