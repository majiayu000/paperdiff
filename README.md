# paperdiff — paper vs code consistency checker for ML research

[![CI](https://github.com/majiayu000/paperdiff/actions/workflows/ci.yml/badge.svg)](https://github.com/majiayu000/paperdiff/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](pyproject.toml)

**paperdiff is a reproducibility tool for ML research: give it an arXiv paper and its GitHub repository, and it
lists every place where the hyperparameters, data split, random seeds and training length stated in the paper differ
from the code's configs, argparse defaults and README commands, with the paper `file:line` and the code `file:line`
side by side.** If you allow it, it then reruns one or two key numbers on your own machine under a hard time and
GPU budget.

> **paperdiff only reports differences. It does not judge whether a paper is correct and it never draws
> conclusions about authors.** A difference can be a typo, a later code change, a setting defined somewhere the
> tool cannot see, a documented choice (BERT's README says its demo settings differ from the paper), or an
> extraction error by this tool. Read both sides before repeating anything it says.

Use it to check a paper before you spend a week reproducing it, to check your own camera-ready code before
submission (`--fail-on conflict` in CI), or to check the code a submission links to while reviewing.

## Install

Python 3.12+ and [uv](https://docs.astral.sh/uv/):

```bash
uv tool install git+https://github.com/majiayu000/paperdiff
```

## What it found in well-known papers

Checked against the official repositories ([examples/](examples/)); each item was confirmed by hand on both sides.

- **LoRA** (arXiv:2106.09685): the RoBERTa-base hyperparameter table says LoRA α = 8; all eight
  `examples/NLU/roberta_base_*.sh` scripts pass `--lora_alpha 16`, the question asked in
  [microsoft/LoRA#37](https://github.com/microsoft/LoRA/issues/37). DeBERTa XXL: table r = 8, α = 8; scripts
  `--lora_r 16 --lora_alpha 32`.
- **DPO** (arXiv:2305.18290): the appendix gives a default learning rate of 1e-6; `config/config.yaml` sets 5e-7.
- **Grokfast** (arXiv:2405.20233): the README's MNIST command omits `--filter ema` (default `none`), so it trains
  without the method; the rerun demo measures it.

## Use

```bash
paperdiff check 2305.18290 https://github.com/eric-mitchell/direct-preference-optimization -o out/
```

Inputs: an arXiv ID or URL, a `.pdf`, a `.tex` file, a LaTeX directory or a source `.tar.gz`; a git URL or a local
directory. `--exclude 'vendor/*'` skips vendored code; `--fail-on conflict` exits 1 when there is a conflict.
Output: `out/report.md` and `out/report.json`.

Part of the DPO report it produces:

```markdown
### C1. `learning_rate`

- **Paper**: `1e-6` → 1e-06 at `main.tex:583`
  - Section: Appendix: DPO Implementation Details and Hyperparameters
  - Context: "Unless noted otherwise, we use a \beta = 0.1, batch size of 64 and the RMSprop optimizer with a learning rate of 1e-6 by default."
- **Code** (highest precedence first; likely effective: 5e-07):
  - 5e-07 — config `lr` at [config/config.yaml:51](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/config/config.yaml#L51): `lr: 5e-7`
```

Every finding is one of:

| Category | Meaning |
|---|---|
| conflict | the code's likely-effective value is unique and differs from the paper |
| ambiguous | several code values, the paper value is overridden (e.g. an argparse default replaced by a README command), or the paper lists several values |
| missing_in_code | stated in the paper, no matching setting in the files that experiment uses |
| missing_in_paper | the code fixes a seed / learning rate / batch size / training length / optimizer the paper never mentions |
| match | same value |

## How it compares

| | paperdiff | [SciCoQA](https://github.com/UKPLab/scicoqa) | [claimcheck](https://github.com/asech109/claimcheck) | [Paper2Code](https://github.com/going-doer/Paper2Code) | [PaperBench](https://github.com/openai/frontier-evals) |
|---|---|---|---|---|---|
| Checks a paper against its existing code | ✅ | ✅ (dataset + LLM eval) | own paper only | ✗ generates new code | ✗ scores agents |
| arXiv ID in, LaTeX source preferred | ✅ | ✗ | ✗ | ✅ | — |
| argparse / YAML / hydra / README commands | ✅ | via LLM | YAML/logs | — | — |
| `file:line` on both sides | ✅ | ✗ | ✅ | — | — |
| Reruns numbers under a budget | opt-in | ✗ | ✗ | ✗ | ✅ |
| Needs an LLM API key | no | yes | no | yes | yes |

Full matrix with sources: [docs/comparison.md](docs/comparison.md).

## Rerun a number (off by default)

`paperdiff check` never executes the target code. `paperdiff rerun` runs one command from a spec, and refuses to
start without `--allow-run` and a `budget.timeout_s`:

```yaml
repo: ~/.cache/paperdiff/repos/github.com_ironjr_grokfast
command: [uv, run, --no-project, --python, "3.12", --with, torch, --with, torchvision, --with, matplotlib,
          --with, tqdm, python, main_mnist.py, --filter, ema, --alpha, "0.8", --lamb, "0.1", --weight_decay, "2.0"]
budget: {timeout_s: 1500, gpus: 0, tokens: null}
targets:
  - name: final_val_acc_percent
    paper: {value: 91.2, source: "sections/4_experiment.tex:41"}
    metric: {regex: "A: [0-9.]+%\\|([0-9.]+)%", pick: last}
    tolerance: {abs: 1.0}
```

```bash
paperdiff rerun spec.yaml --allow-run -o out/rerun
```

The command runs as an argument list (no shell), on your machine only, with `CUDA_VISIBLE_DEVICES` limited to
`gpus` and the whole process group killed at the time limit. `tokens` records the budget given to whichever agent
wrote the spec; paperdiff itself calls no LLM. [`skills/paperdiff/SKILL.md`](skills/paperdiff/SKILL.md) tells a
coding agent how to choose numbers, write the spec and ask before running.

## Results on real papers

Four papers, checked against their official repositories on 2026-10-22 ([examples/](examples/)):

| Paper | Claims | Conflict | Ambiguous | Missing in code | Missing in paper | Match |
|---|---|---|---|---|---|---|
| Grokfast (2405.20233) | 35 | 0 | 1 | 10 | 1 | 24 |
| DPO (2305.18290) | 6 | 2 | 1 | 0 | 1 | 3 |
| BERT (1810.04805) | 31 | 7 | 13 | 5 | 1 | 6 |
| LoRA (2106.09685) | 411 | 36 | 209 | 22 | 1 | 144 |

Conflicts confirmed by hand include LoRA's RoBERTa-base α (table 8, every `roberta_base_*.sh` passes 16, the same
thing a user asked about in [microsoft/LoRA#37](https://github.com/microsoft/LoRA/issues/37)), RoBERTa-large
CoLA/STS-B learning rates, and DPO's default learning rate (1e-6 in the appendix, `lr: 5e-7` in
`config/config.yaml`). One of DPO's two conflicts is a false pairing; details and known noise are in
[examples/README.md](examples/README.md).

Rerun demo ([examples/rerun-grokfast-mnist/](examples/rerun-grokfast-mnist/)): Grokfast's MNIST experiment on a
laptop CPU, 100k steps, 1500 s budget. The paper's setting reached 91.0% final validation accuracy (paper: 91.2%)
in 789 s. The repo's README command, which omits `--filter ema` and so trains without the method, reached 90.7% in
691 s and hit 80% and 85% at the same logged steps as the filtered run.

## How it works

- **Paper side**: prefers the LaTeX source from `export.arxiv.org` (one request at a time, at least 3 s apart,
  cached; never the `/e-print` or `/src` paths that `arxiv.org/robots.txt` disallows), follows `\input`, skips
  comments and figures, and reads both sentences ("a learning rate of $3\times10^{-4}$") and hyperparameter tables
  (row groups, `\multicolumn` spans). PDF is the fallback, with weaker table handling.
- **Code side**: Python `ast` for argparse and absl flags, optimizer and seed calls, keyword arguments and
  module-level constants; YAML/JSON configs (hydra included) with line numbers; launch commands in README code
  blocks and shell scripts, with simple `$VAR` substitution. Nothing is imported or executed.
- **Alignment**: each claim is matched to the files its section or table row/column points at (MNIST section →
  `main_mnist.py`, "RoBERTa large LoRA / CoLA" → `roberta_large_cola.sh`), then values are compared with
  command > config > argparse/flag default > code default precedence.

Design and limits: [docs/design.md](docs/design.md). Prior art and real reviewer complaints:
[docs/research.md](docs/research.md). Feature comparison: [docs/comparison.md](docs/comparison.md).

## Limits

- Only the settings in [`keys.py`](src/paperdiff/keys.py) are compared. Method-level differences (a loss term, the
  order of two layers) are out of scope, and they are about half of the real cases in docs/research.md.
- The "effective" code value is inferred from precedence, not observed at runtime.
- One rerun that does not match is not evidence that a result is irreproducible.
- If you publish anything based on a report, publish aggregates or talk to the authors first.

## Development

```bash
uv sync
uv run pytest
bash examples/run.sh   # regenerates examples/*/report.*
```

MIT licensed.
