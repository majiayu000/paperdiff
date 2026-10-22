# Examples

Static checks of four public papers against their official code, plus one CPU rerun. Regenerate the static
reports with `bash examples/run.sh` (each paper is fetched once from export.arxiv.org and cached).

| Paper | Code (commit) | Claims | Conflict | Ambiguous | Missing in code | Missing in paper | Match |
|---|---|---|---|---|---|---|---|
| [Grokfast](grokfast/report.md) (arXiv:2405.20233) | ironjr/grokfast `93b2248e351d` | 35 | 0 | 1 | 10 | 1 | 24 |
| [DPO](dpo/report.md) (arXiv:2305.18290) | eric-mitchell/direct-preference-optimization `f8b8c0f49dc9` | 6 | 2 | 1 | 0 | 1 | 3 |
| [BERT](bert/report.md) (arXiv:1810.04805) | google-research/bert `eedf5716ce12` | 31 | 7 | 13 | 5 | 1 | 6 |
| [LoRA](lora/report.md) (arXiv:2106.09685) | microsoft/LoRA `c4593f060e6a` | 411 | 36 | 209 | 22 | 1 | 144 |

LoRA was checked with `--exclude 'examples/NLU/src/*' --exclude 'examples/NLU/examples/*'` because that
directory vendors a full copy of Hugging Face transformers.

## What a person finds when checking the conflicts by hand

Every conflict below was opened on both sides and confirmed by reading the paper source and the code.
Confirmed means "the two really say different things", not "the paper is wrong".

- **LoRA, RoBERTa-base LoRA α**: the hyperparameter table says α = 8 (`iclr2022_conference.tex:662`); all eight
  `examples/NLU/roberta_base_*.sh` scripts pass `--lora_alpha 16`. A user reported exactly this in
  [microsoft/LoRA#37](https://github.com/microsoft/LoRA/issues/37) (opened 2022-11-22, still open, no maintainer
  answer). paperdiff found it without knowing about the issue.
- **LoRA, DeBERTa XXL LoRA α**: table says 8 (`:744`); `deberta_v2_xxlarge_*.sh` pass `--lora_alpha 32`. The
  same scripts pass `--lora_r 16` while the table says $r_q=r_v=8$ (`:743`), two settings packed into one cell.
- **LoRA, RoBERTa-large CoLA / STS-B learning rate**: table says 2E-04 (`:668`); `roberta_large_cola.sh` and
  `roberta_large_stsb.sh` pass `--learning_rate 3e-4`. Also batch size for SST-2 (4 vs 8) and STS-B (8 vs 4), and
  STS-B epochs (30 in the main block vs 10 in the script; the restricted-setup block of the same table says 10).
- **LoRA, DeBERTa CoLA / RTE learning rate**: table 1E-04 / 2E-04, scripts 1.3e-4 / 2.6e-4.
- **DPO learning rate**: the appendix says RMSprop with learning rate 1e-6 "by default" (`main.tex:583`);
  `config/config.yaml:51` sets `lr: 5e-7`, and no README command overrides it. The other DPO conflict (reward-model
  epochs, `main.tex:591`) describes a model trained outside this repository, so it is a false pairing.
- **BERT pre-training**: the paper's 1M steps, batch 256, lr 1e-4 differ from the README demo command (20 steps,
  batch 32, lr 2e-5) and from the flag defaults. The README itself says the demo is deliberately tiny and that its
  SQuAD settings are "slightly different than the paper". A documented, intentional difference: exactly the kind of
  item that needs a human to read before it is repeated anywhere.

Things the static check cannot see, found while preparing the rerun: Grokfast's README commands for MNIST, IMDb and
QM9 (`README.md:207,221,233`) pass `--alpha` and `--lamb` but not `--filter ema`, and `--filter` defaults to
`none`, so those commands train the baseline. Someone asked about this in
[ironjr/grokfast#16](https://github.com/ironjr/grokfast/issues/16) (open, unanswered). The rerun below measures
what that means.

## Known noise in these reports

- "Ambiguous" is large for LoRA because the paper sweeps ranks and learning rates in prose and tables, and the
  repo has several scripts per task. That is the intended bucket for "a person has to look".
- "Missing in code" mostly means the value is computed or hard-coded rather than exposed as a setting (Grokfast's
  QM9 runs `epochs = int(100 * 50000 / args.size)`), or that sklearn's default split (`train_test_split`, 75:25)
  provides it implicitly.
- Architecture claims from prose ("two-layer MLP" for a prediction head) are sometimes paired with the wrong model.

## Rerun: Grokfast MNIST on CPU

Paper setting: 91.0% final validation accuracy (paper 91.2%, 789 s on CPU). README command verbatim: 90.7%
(691 s). Details in [rerun-grokfast-mnist/](rerun-grokfast-mnist/README.md).

## PDF fallback

The same DPO check run on the arXiv PDF instead of the LaTeX source (`paperdiff check dpo.pdf ...`) gives the same
summary (2 conflicts, 1 ambiguous, 1 missing in paper, 3 matches), with locations such as `dpo.pdf:p20:L20`.
