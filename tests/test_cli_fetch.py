import gzip
import json

import pytest

from paperdiff.cli import main
from paperdiff.fetch import FetchError, parse_arxiv_id, resolve_paper

from fixtures import paper_dir, repo_dir  # noqa: F401  (pytest fixtures)


@pytest.mark.parametrize(
    "text, expected",
    [("2405.20233", "2405.20233"), ("arXiv:2106.09685v2", "2106.09685v2"),
     ("https://arxiv.org/abs/1810.04805", "1810.04805"), ("https://arxiv.org/pdf/2305.18290v3", "2305.18290v3"),
     ("hep-th/9901001", "hep-th/9901001"), ("not-a-paper", None)],
)
def test_parse_arxiv_id(text, expected):
    assert parse_arxiv_id(text) == expected


def test_local_gzipped_single_tex(tmp_path, monkeypatch):
    monkeypatch.setenv("PAPERDIFF_CACHE", str(tmp_path / "cache"))
    src = tmp_path / "paper.gz"
    src.write_bytes(gzip.compress(rb"\documentclass{article}\begin{document}x\end{document}"))
    p = resolve_paper(str(src))
    assert p.kind == "latex" and (p.path / "main.tex").is_file()


def test_unknown_input_fails_clearly():
    with pytest.raises(FetchError, match="not a local path or arXiv ID"):
        resolve_paper("definitely not a paper")


def test_check_end_to_end(paper_dir, repo_dir, tmp_path, capsys):
    out = tmp_path / "out"
    assert main(["check", str(paper_dir), str(repo_dir), "-o", str(out)]) == 0
    report = json.loads((out / "report.json").read_text())
    assert report["schema_version"] == 1 and report["paper"]["title"].startswith("Toyformer")
    assert report["summary"]["conflict"] >= 1
    md = (out / "report.md").read_text()
    assert "not an accusation of misconduct" in md
    assert "`sections/setup.tex:3`" in md
    assert "claims" in capsys.readouterr().out


def test_rerun_without_allow_run_exits_nonzero(tmp_path, capsys):
    (tmp_path / "repo").mkdir()
    spec = tmp_path / "s.yaml"
    spec.write_text('repo: repo\ncommand: ["true"]\nbudget: {timeout_s: 5}\n'
                    'targets: [{name: x, paper: {value: 1}, metric: {regex: "(1)"}}]\n')
    assert main(["rerun", str(spec), "-o", str(tmp_path / "o")]) == 2
    assert "--allow-run" in capsys.readouterr().err


def test_fail_on_conflict(paper_dir, repo_dir, tmp_path, capsys):
    args = ["check", str(paper_dir), str(repo_dir), "-o", str(tmp_path / "o")]
    assert main(args + ["--fail-on", "missing_in_paper"]) == 0
    assert main(args + ["--fail-on", "conflict"]) == 1
    assert "conflict=" in capsys.readouterr().err


def test_get_retries_rate_limits_and_truncated_downloads(monkeypatch):
    import http.client
    import io
    import urllib.error

    from paperdiff import fetch

    calls = []

    class Resp(io.BytesIO):
        status = 206

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    def fake_urlopen(req, timeout):
        calls.append(req.full_url)
        if len(calls) == 1:
            raise urllib.error.HTTPError(req.full_url, 429, "Too Many Requests", {"Retry-After": "1"}, None)
        if len(calls) == 2:
            raise http.client.IncompleteRead(b"who", 2)
        assert req.headers["Range"] == "bytes=3-"
        return Resp(b"le")

    monkeypatch.setattr(fetch.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(fetch.time, "sleep", lambda s: None)
    assert fetch._get("https://export.arxiv.org/src/x") == b"whole" and len(calls) == 3


def test_rate_limit_does_not_silently_switch_to_pdf(monkeypatch, tmp_path):
    from paperdiff import fetch

    monkeypatch.setenv("PAPERDIFF_CACHE", str(tmp_path))

    def always_429(url):
        raise fetch.FetchError(f"GET {url} failed: HTTP 429", status=429)

    monkeypatch.setattr(fetch, "_get", always_429)
    with pytest.raises(fetch.FetchError, match="429"):
        fetch.fetch_arxiv("2405.20233")
