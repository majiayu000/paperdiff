import sys
from pathlib import Path

import pytest

from paperdiff.rerun import RerunError, load_spec, run


def write_spec(tmp_path: Path, body: str) -> Path:
    (tmp_path / "repo").mkdir(exist_ok=True)
    p = tmp_path / "spec.yaml"
    p.write_text(body)
    return p


SPEC = f"""repo: repo
command: ["{sys.executable}", "-c", "import time; print('acc=91.0'); time.sleep({{sleep}}); print('acc=90.5')"]
budget: {{{{timeout_s: {{timeout}}, gpus: 0}}}}
targets:
  - name: acc
    paper: {{{{value: 91.2, source: "paper.tex:41"}}}}
    metric: {{{{regex: "acc=([0-9.]+)", pick: last}}}}
    tolerance: {{{{abs: 1.0}}}}
"""


def test_refuses_without_allow_run(tmp_path):
    spec = load_spec(write_spec(tmp_path, SPEC.format(sleep=0, timeout=30)))
    with pytest.raises(RerunError, match="--allow-run"):
        run(spec, tmp_path / "out", allow_run=False)
    assert not (tmp_path / "out").exists()


def test_requires_time_budget(tmp_path):
    with pytest.raises(RerunError, match="timeout_s"):
        load_spec(write_spec(tmp_path, SPEC.format(sleep=0, timeout=30).replace("timeout_s: 30, ", "")))


def test_runs_and_compares(tmp_path):
    spec = load_spec(write_spec(tmp_path, SPEC.format(sleep=0, timeout=30)))
    result = run(spec, tmp_path / "out", allow_run=True)
    assert result["status"] == "finished" and result["budget"]["gpus"] == 0
    t = result["targets"][0]
    assert t["measured"] == 90.5 and t["verdict"] == "reproduced"


def test_timeout_kills_and_reports_partial(tmp_path):
    spec = load_spec(write_spec(tmp_path, SPEC.format(sleep=30, timeout=1)))
    result = run(spec, tmp_path / "out", allow_run=True)
    assert result["status"] == "timeout" and result["elapsed_s"] < 10
    t = result["targets"][0]
    assert t["measured"] == 91.0 and t["verdict"].startswith("reproduced (partial")
