# SciCoQA real split: results

- Runs: 74 (paper version, commit) pairs, 62 completed (41 from LaTeX source, 21 from PDF), 12 failed to fetch or parse.
- Items: 92; items whose run failed count as not detected.

## Recall

| Subset | Items | Detected (strict: conflict) | Detected (any non-match finding) |
|---|---|---|---|
| All items | 92 | 0/92 (0.0%) | 12/92 (13.0%) |
| Coverable (`keys`) | 3 | 0/3 (0.0%) | 0/3 (0.0%) |
| Other setting values | 11 | 0/11 (0.0%) | 3/11 (27.3%) |
| Method-level | 78 | 0/78 (0.0%) | 9/78 (11.5%) |

By SciCoQA category:

| Category | Items | Strict | Any |
|---|---|---|---|
| Algorithm | 22 | 0 | 4 |
| Data | 10 | 0 | 0 |
| Evaluation | 9 | 0 | 0 |
| Loss | 22 | 0 | 3 |
| Model | 10 | 0 | 1 |
| Training | 16 | 0 | 4 |
| none | 3 | 0 | 0 |

Coverable items:

- `f2b47a1a`: run ok, source pdf, strict=False, any=False
- `f9a805be`: run error, source None, strict=False, any=False
- `66841ab0`: run ok, source pdf, strict=False, any=False

Items detected by any rule: `9a6bc557`, `c9a26055`, `0b8b9b43`, `96d7973b`, `a17a3073`, `47339aed`, `c5dec3b3`, `dfccf929`, `a950db48`, `3bdc7c6f`, `84acd23b`, `417ffbee`

## Precision

- Conflict findings over all completed runs: 87
- Precision vs gold (lower bound, gold is incomplete): 0/87 (0.0%)
- Audited precision (random sample, seed 20261025): 20/30 (66.7%) judged (0 of 30 not yet judged)

| # | Paper | Setting | Paper value | Code value | Verdict | Reason |
|---|---|---|---|---|---|---|
| 1 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_alpha | `8` (iclr2022_conference.tex:744) | 32.0 (examples/NLU/deberta_v2_xxlarge_mrpc.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 2 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_rank | `r_q=r_v=8` (iclr2022_conference.tex:743) | 16.0 (examples/NLU/deberta_v2_xxlarge_qnli.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 3 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_alpha | `8` (iclr2022_conference.tex:662) | 16.0 (examples/NLU/roberta_base_cola.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 4 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_alpha | `8` (iclr2022_conference.tex:662) | 16.0 (examples/NLU/roberta_base_mnli.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 5 | https://arxiv.org/pdf/2310.02391v4.pdf | learning_rate | `10^{-4}` (appendix.tex:755) | 0.0 (ProteinMPNN/training/model_utils.py:661) | false | lr=0 is a placeholder; NoamOpt sets the learning rate (vendored ProteinMPNN code) |
| 6 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_alpha | `8` (iclr2022_conference.tex:744) | 32.0 (examples/NLU/deberta_v2_xxlarge_qnli.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 7 | https://arxiv.org/pdf/1904.00152v2.pdf | learning_rate | `0.00025` (iclr2020_conference.tex:259) | 0.01 (rsr_layer_pytorch.py:175) | real | paper Adam lr 0.00025; this PyTorch reimplementation sets peak lr 0.01 with OneCycleLR |
| 8 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_alpha | `8` (iclr2022_conference.tex:744) | 32.0 (examples/NLU/deberta_v2_xxlarge_mnli.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 9 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_rank | `r_q=r_v=8` (iclr2022_conference.tex:743) | 16.0 (examples/NLU/deberta_v2_xxlarge_mrpc.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 10 | https://arxiv.org/pdf/2004.09297v2.pdf | batch_size | `256` (main.tex:497) | 40.0 (pretraining/examples/speech_recognition/README.md:25) | false | paired with fairseq example scripts unrelated to the pre-training run |
| 11 | https://arxiv.org/pdf/2004.09297v2.pdf | batch_size | `16, 32` (main.tex:432) | 40.0 (pretraining/examples/speech_recognition/README.md:25) | false | paired with fairseq example scripts unrelated to fine-tuning |
| 12 | https://arxiv.org/pdf/1904.00152v2.pdf | epochs | `200` (iclr2020_conference.tex:1302) | 150.0 (rsr_layer_pytorch.py:175) | real | paper 200 epochs; reimplementation hparams epochs=150 |
| 13 | https://arxiv.org/pdf/2106.09685v2.pdf | learning_rate | `2E-04` (iclr2022_conference.tex:740) | 0.00026 (examples/NLU/deberta_v2_xxlarge_rte.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 14 | https://proceedings.mlr.press/v162/crabbe22a/crabbe22a.pdf | weight_decay | `10` (3b78a470666576b7.pdf:p19:L6) | 1e-06 (simclr_config.yaml:33) | false | PDF text lost the minus sign: "10−5" read as 10 |
| 15 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_rank | `r_q=r_v=8` (iclr2022_conference.tex:743) | 16.0 (examples/NLU/deberta_v2_xxlarge_qqp.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 16 | https://proceedings.mlr.press/v162/crabbe22a/crabbe22a.pdf | weight_decay | `10` (3b78a470666576b7.pdf:p19:L21) | 1e-06 (simclr_config.yaml:33) | false | PDF text lost the minus sign: "10−6" read as 10 |
| 17 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_rank | `r_q=r_v=8` (iclr2022_conference.tex:743) | 16.0 (examples/NLU/deberta_v2_xxlarge_sst2.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 18 | https://arxiv.org/pdf/1904.00152v2.pdf | optimizer | `Adam` (iclr2020_conference.tex:259) | AdamW (rsr_layer_pytorch.py:160) | real | paper Adam; reimplementation uses AdamW |
| 19 | https://arxiv.org/pdf/2106.09685v2.pdf | num_train_samples | `10k` (iclr2022_conference.tex:984) | 500.0 (examples/NLU/examples/seq2seq/README.md:42) | false | paired with a vendored HF seq2seq README example |
| 20 | https://arxiv.org/pdf/1904.00152v2.pdf | learning_rate | `0.0001` (iclr2020_conference.tex:1165) | 0.01 (rsr_layer_pytorch.py:175) | false | sentence lists a sweep of learning rates; only the first value was taken |
| 21 | https://arxiv.org/pdf/1904.00152v2.pdf | batch_size | `128` (iclr2020_conference.tex:259) | 64.0 (rsr_layer_pytorch.py:173) | real | paper batch 128; reimplementation DataLoader batch_size=64 |
| 22 | https://arxiv.org/pdf/1904.00152v2.pdf | optimizer | `Adam` (iclr2020_conference.tex:638) | AdamW (rsr_layer_pytorch.py:160) | false | artificial-data demo in the paper; the code has no such experiment |
| 23 | https://arxiv.org/pdf/1904.00152v2.pdf | learning_rate | `0.00025` (iclr2020_conference.tex:1164) | 0.01 (rsr_layer_pytorch.py:175) | real | paper fixes lr 0.00025; reimplementation peak lr 0.01 |
| 24 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_alpha | `8` (iclr2022_conference.tex:662) | 16.0 (examples/NLU/roberta_base_stsb.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 25 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_alpha | `8` (iclr2022_conference.tex:662) | 16.0 (examples/NLU/roberta_base_sst2.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 26 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_alpha | `8` (iclr2022_conference.tex:662) | 16.0 (examples/NLU/roberta_base_qqp.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 27 | https://arxiv.org/pdf/2004.09297v2.pdf | batch_size | `8192` (main.tex:228) | 40.0 (pretraining/examples/speech_recognition/README.md:25) | false | paired with fairseq example scripts unrelated to pre-training |
| 28 | https://arxiv.org/pdf/2106.09685v2.pdf | lora_alpha | `8` (iclr2022_conference.tex:662) | 16.0 (examples/NLU/roberta_base_rte.sh:5) | real | paper table and the per-task script really give different values (checked in both files) |
| 29 | https://arxiv.org/pdf/1902.09513v2.pdf | batch_size | `3` (paper.tex:246) | 7.0 (feelvos/train.py:17) | real | paper 3 videos per GPU; argparse default --batch_size 7 |
| 30 | https://arxiv.org/pdf/1902.03642v1.pdf | batch_size | `64` (method.tex:2) | 100.0 (src/qpwgan.py:206) | false | batch_size=100 is a plotting sample size, not the training batch |
