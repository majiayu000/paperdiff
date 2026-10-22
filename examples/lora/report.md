# paperdiff report: arXiv:2106.09685

- Paper: arXiv:2106.09685 (LaTeX source, main file `iclr2022_conference.tex`)
- Title: LoRA: Low-Rank Adaptation of Large Language Models
- Code: https://github.com/microsoft/LoRA @ `c4593f060e6a`
- Excluded paths: `examples/NLU/src/*`, `examples/NLU/examples/*`
- Generated: 2026-10-22T08:14:57Z by paperdiff 0.1.0

| Category | Count |
|---|---|
| conflict | 36 |
| ambiguous | 209 |
| missing_in_code | 22 |
| missing_in_paper | 1 |
| match | 144 |

> paperdiff reports differences between what a paper states and what its code configures. A difference can come from a typo, a later code change, a setting defined elsewhere, a reasonable implementation choice, or an extraction error by this tool. It is not a judgement about whether the paper is correct, and it is not an accusation of misconduct. Check each item by hand before citing it.

## Conflicts — the code sets a different value (36)

### C1. `learning_rate`

- **Paper**: `2E-04` → 0.0002 at `iclr2022_conference.tex:668` (column: RoBERTa large LoRA / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 4E-04 \| 3E-04 \| 2E-04 \| 2E-04 \| 3E-04 \| 4E-04 \| 2E-04"
- **Code** (highest precedence first; likely effective: 0.0003):
  - 0.0003 — command `--learning_rate` at [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > CoLA"

### C2. `learning_rate`

- **Paper**: `2E-04` → 0.0002 at `iclr2022_conference.tex:668` (column: RoBERTa large LoRA / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 4E-04 \| 3E-04 \| 2E-04 \| 2E-04 \| 3E-04 \| 4E-04 \| 2E-04"
- **Code** (highest precedence first; likely effective: 0.0003):
  - 0.0003 — command `--learning_rate` at [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > STS-B"

### C3. `learning_rate`

- **Paper**: `2E-04` → 0.0002 at `iclr2022_conference.tex:676` (column: RoBERTa large LoRA / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 4E-04 \| 3E-04 \| 2E-04 \| 2E-04 \| 3E-04 \| 4E-04 \| 2E-04"
- **Code** (highest precedence first; likely effective: 0.0003):
  - 0.0003 — command `--learning_rate` at [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > CoLA"

### C4. `learning_rate`

- **Paper**: `2E-04` → 0.0002 at `iclr2022_conference.tex:676` (column: RoBERTa large LoRA / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 4E-04 \| 3E-04 \| 2E-04 \| 2E-04 \| 3E-04 \| 4E-04 \| 2E-04"
- **Code** (highest precedence first; likely effective: 0.0003):
  - 0.0003 — command `--learning_rate` at [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > STS-B"

### C5. `learning_rate`

- **Paper**: `1E-04` → 0.0001 at `iclr2022_conference.tex:740` (column: DeBERTa XXL LoRA / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "Learning Rate \| 1E-04 \| 6E-05 \| 2E-04 \| 1E-04 \| 1E-04 \| 1E-04 \| 2E-04 \| 2E-04"
- **Code** (highest precedence first; likely effective: 0.00013):
  - 0.00013 — command `--learning_rate` at [examples/NLU/deberta_v2_xxlarge_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > CoLA"

### C6. `learning_rate`

- **Paper**: `2E-04` → 0.0002 at `iclr2022_conference.tex:740` (column: DeBERTa XXL LoRA / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "Learning Rate \| 1E-04 \| 6E-05 \| 2E-04 \| 1E-04 \| 1E-04 \| 1E-04 \| 2E-04 \| 2E-04"
- **Code** (highest precedence first; likely effective: 0.00026):
  - 0.00026 — command `--learning_rate` at [examples/NLU/deberta_v2_xxlarge_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_rte.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > RTE"

### C7. `batch_size`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:666` (column: RoBERTa large LoRA / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "RoBERTa large LoRA \| Batch Size \| 4 \| 4 \| 4 \| 4 \| 4 \| 4 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 8):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > SST-2"

### C8. `batch_size`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:666` (column: RoBERTa large LoRA / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "RoBERTa large LoRA \| Batch Size \| 4 \| 4 \| 4 \| 4 \| 4 \| 4 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 4):
  - 4 — command `--per_device_train_batch_size` at [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > STS-B"

### C9. `batch_size`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:674` (column: RoBERTa large LoRA / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "RoBERTa large LoRA \| Batch Size \| 4 \| 4 \| 4 \| 4 \| 4 \| 4 \| 4 \| 4"
- **Code** (highest precedence first; likely effective: 8):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > SST-2"

### C10. `batch_size`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:674` (column: RoBERTa large LoRA / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "RoBERTa large LoRA \| Batch Size \| 4 \| 4 \| 4 \| 4 \| 4 \| 4 \| 4 \| 4"
- **Code** (highest precedence first; likely effective: 8):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > RTE"

### C11. `epochs`

- **Paper**: `30` → 30 at `iclr2022_conference.tex:667` (column: RoBERTa large LoRA / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 10 \| 20 \| 20 \| 10 \| 20 \| 20 \| 30"
- **Code** (highest precedence first; likely effective: 10):
  - 10 — command `--num_train_epochs` at [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > STS-B"

### C12. `weight_decay`

- **Paper**: `0.0` → 0 at `iclr2022_conference.tex:770` (column: DART)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Weight Decay \| 0.01 \| 0.01 \| 0.0"
- **Code** (highest precedence first; likely effective: 0.01):
  - 0.01 — command `--weight_decay` at [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52): `python -m torch.distributed.launch --nproc_per_node=1 src/gpt2_ft.py \`
- Scope: compared only with files matching "GPT-2"

### C13. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:743` (column: DeBERTa XXL LoRA / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA Config. \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/deberta_v2_xxlarge_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > MNLI"

### C14. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:743` (column: DeBERTa XXL LoRA / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA Config. \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/deberta_v2_xxlarge_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_sst2.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > SST-2"

### C15. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:743` (column: DeBERTa XXL LoRA / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA Config. \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/deberta_v2_xxlarge_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > MRPC"

### C16. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:743` (column: DeBERTa XXL LoRA / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA Config. \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/deberta_v2_xxlarge_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > CoLA"

### C17. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:743` (column: DeBERTa XXL LoRA / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA Config. \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/deberta_v2_xxlarge_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > QNLI"

### C18. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:743` (column: DeBERTa XXL LoRA / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA Config. \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/deberta_v2_xxlarge_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qqp.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > QQP"

### C19. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:743` (column: DeBERTa XXL LoRA / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA Config. \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/deberta_v2_xxlarge_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_rte.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > RTE"

### C20. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:743` (column: DeBERTa XXL LoRA / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA Config. \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/deberta_v2_xxlarge_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_stsb.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > STS-B"

### C21. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:662` (column: RoBERTa base LoRA / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_alpha` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa base LoRA > MNLI"

### C22. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:662` (column: RoBERTa base LoRA / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_alpha` at [examples/NLU/roberta_base_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_sst2.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa base LoRA > SST-2"

### C23. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:662` (column: RoBERTa base LoRA / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_alpha` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa base LoRA > MRPC"

### C24. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:662` (column: RoBERTa base LoRA / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_alpha` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa base LoRA > CoLA"

### C25. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:662` (column: RoBERTa base LoRA / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_alpha` at [examples/NLU/roberta_base_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa base LoRA > QNLI"

### C26. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:662` (column: RoBERTa base LoRA / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_alpha` at [examples/NLU/roberta_base_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qqp.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa base LoRA > QQP"

### C27. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:662` (column: RoBERTa base LoRA / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_alpha` at [examples/NLU/roberta_base_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_rte.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa base LoRA > RTE"

### C28. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:662` (column: RoBERTa base LoRA / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_alpha` at [examples/NLU/roberta_base_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_stsb.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa base LoRA > STS-B"

### C29. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:744` (column: DeBERTa XXL LoRA / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 32):
  - 32 — command `--lora_alpha` at [examples/NLU/deberta_v2_xxlarge_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > MNLI"

### C30. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:744` (column: DeBERTa XXL LoRA / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 32):
  - 32 — command `--lora_alpha` at [examples/NLU/deberta_v2_xxlarge_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_sst2.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > SST-2"

### C31. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:744` (column: DeBERTa XXL LoRA / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 32):
  - 32 — command `--lora_alpha` at [examples/NLU/deberta_v2_xxlarge_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > MRPC"

### C32. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:744` (column: DeBERTa XXL LoRA / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 32):
  - 32 — command `--lora_alpha` at [examples/NLU/deberta_v2_xxlarge_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > CoLA"

### C33. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:744` (column: DeBERTa XXL LoRA / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 32):
  - 32 — command `--lora_alpha` at [examples/NLU/deberta_v2_xxlarge_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > QNLI"

### C34. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:744` (column: DeBERTa XXL LoRA / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 32):
  - 32 — command `--lora_alpha` at [examples/NLU/deberta_v2_xxlarge_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qqp.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > QQP"

### C35. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:744` (column: DeBERTa XXL LoRA / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 32):
  - 32 — command `--lora_alpha` at [examples/NLU/deberta_v2_xxlarge_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_rte.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > RTE"

### C36. `lora_alpha`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:744` (column: DeBERTa XXL LoRA / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "LoRA \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 32):
  - 32 — command `--lora_alpha` at [examples/NLU/deberta_v2_xxlarge_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_stsb.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "DeBERTa > DeBERTa XXL LoRA > STS-B"

## Ambiguous — several values, or the paper value is overridden (209)

### A1. `learning_rate`

- **Paper**: `3E-05` → 3e-05 at `iclr2022_conference.tex:684` (column: Adpt^P (3M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: the code sets 4 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A2. `learning_rate`

- **Paper**: `3E-05` → 3e-05 at `iclr2022_conference.tex:684` (column: Adpt^P (3M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: the code sets 4 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A3. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:684` (column: Adpt^P (3M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A4. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:684` (column: Adpt^P (3M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A5. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:684` (column: Adpt^P (3M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A6. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:684` (column: Adpt^P (3M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A7. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:684` (column: Adpt^P (3M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A8. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:684` (column: Adpt^P (3M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A9. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:691` (column: Adpt^P (0.8M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A10. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:691` (column: Adpt^P (0.8M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A11. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:691` (column: Adpt^P (0.8M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A12. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:691` (column: Adpt^P (0.8M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A13. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:691` (column: Adpt^P (0.8M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A14. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:691` (column: Adpt^P (0.8M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A15. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:691` (column: Adpt^P (0.8M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A16. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:691` (column: Adpt^P (0.8M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A17. `learning_rate`

- **Paper**: `3E-05` → 3e-05 at `iclr2022_conference.tex:698` (column: Adpt^H (6M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: the code sets 4 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A18. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:698` (column: Adpt^H (6M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A19. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:698` (column: Adpt^H (6M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A20. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:698` (column: Adpt^H (6M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A21. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:698` (column: Adpt^H (6M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A22. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:698` (column: Adpt^H (6M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A23. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:698` (column: Adpt^H (6M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A24. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:698` (column: Adpt^H (6M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-05 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A25. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:705` (column: Adpt^H (0.8M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A26. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:705` (column: Adpt^H (0.8M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A27. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:705` (column: Adpt^H (0.8M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A28. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:705` (column: Adpt^H (0.8M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A29. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:705` (column: Adpt^H (0.8M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A30. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:705` (column: Adpt^H (0.8M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A31. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:705` (column: Adpt^H (0.8M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A32. `learning_rate`

- **Paper**: `3E-04` → 0.0003 at `iclr2022_conference.tex:705` (column: Adpt^H (0.8M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Learning Rate \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04 \| 3E-04"
- **Code** (highest precedence first; likely effective: 0.0003, 0.0004, 0.0005, 0.0002):
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0003 — command `--learning_rate` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0005 — command `--learning_rate` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0004 — command `--learning_rate` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A33. `learning_rate`

- **Paper**: `5.00E-06` → 5e-06 at `iclr2022_conference.tex:816` (column: Fine-Tune)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Learning Rate \| 5.00E-06 \| 5.00E-04 \| 1.00E-04 \| 1.6E-03 \| 1.00E-04 \| 2.00E-04"
- **Code** (highest precedence first; likely effective: 0.0001):
  - 0.0001 — command `--learning_rate` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0001 — command `--learning_rate` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1e-05 — argparse_default `--lr` at [examples/NLG/src/optimizer.py:20](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L20): `parser.add_argument('--lr', default=0.00001, type=float, help='learning rate')`
  - 0.001 — code_default `lr` at [examples/NLG/src/optimizer.py:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L51): `def __init__(self, params, lr=1e-3, betas=(0.9, 0.98), eps=1e-6, weight_decay=0.0, correct_bias=True):`
  - 0.1 — code_default `max_lr` at [examples/NLG/src/optimizer.py:147](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L147): `max_lr : float = 0.1,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A34. `learning_rate`

- **Paper**: `5.00E-04` → 0.0005 at `iclr2022_conference.tex:816` (column: PreEmbed)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Learning Rate \| 5.00E-06 \| 5.00E-04 \| 1.00E-04 \| 1.6E-03 \| 1.00E-04 \| 2.00E-04"
- **Code** (highest precedence first; likely effective: 0.0001):
  - 0.0001 — command `--learning_rate` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0001 — command `--learning_rate` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1e-05 — argparse_default `--lr` at [examples/NLG/src/optimizer.py:20](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L20): `parser.add_argument('--lr', default=0.00001, type=float, help='learning rate')`
  - 0.001 — code_default `lr` at [examples/NLG/src/optimizer.py:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L51): `def __init__(self, params, lr=1e-3, betas=(0.9, 0.98), eps=1e-6, weight_decay=0.0, correct_bias=True):`
  - 0.1 — code_default `max_lr` at [examples/NLG/src/optimizer.py:147](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L147): `max_lr : float = 0.1,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A35. `learning_rate`

- **Paper**: `1.6E-03` → 0.0016 at `iclr2022_conference.tex:816` (column: BitFit)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Learning Rate \| 5.00E-06 \| 5.00E-04 \| 1.00E-04 \| 1.6E-03 \| 1.00E-04 \| 2.00E-04"
- **Code** (highest precedence first; likely effective: 0.0001):
  - 0.0001 — command `--learning_rate` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0001 — command `--learning_rate` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1e-05 — argparse_default `--lr` at [examples/NLG/src/optimizer.py:20](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L20): `parser.add_argument('--lr', default=0.00001, type=float, help='learning rate')`
  - 0.001 — code_default `lr` at [examples/NLG/src/optimizer.py:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L51): `def __init__(self, params, lr=1e-3, betas=(0.9, 0.98), eps=1e-6, weight_decay=0.0, correct_bias=True):`
  - 0.1 — code_default `max_lr` at [examples/NLG/src/optimizer.py:147](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L147): `max_lr : float = 0.1,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A36. `learning_rate`

- **Paper**: `2.00E-04` → 0.0002 at `iclr2022_conference.tex:816` (column: LoRA)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Learning Rate \| 5.00E-06 \| 5.00E-04 \| 1.00E-04 \| 1.6E-03 \| 1.00E-04 \| 2.00E-04"
- **Code** (highest precedence first; likely effective: 0.0001):
  - 0.0001 — command `--learning_rate` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0.0001 — command `--learning_rate` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1e-05 — argparse_default `--lr` at [examples/NLG/src/optimizer.py:20](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L20): `parser.add_argument('--lr', default=0.00001, type=float, help='learning rate')`
  - 0.001 — code_default `lr` at [examples/NLG/src/optimizer.py:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L51): `def __init__(self, params, lr=1e-3, betas=(0.9, 0.98), eps=1e-6, weight_decay=0.0, correct_bias=True):`
  - 0.1 — code_default `max_lr` at [examples/NLG/src/optimizer.py:147](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L147): `max_lr : float = 0.1,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A37. `batch_size`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:1020` (column: MNLI-100)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "Batch Size \| - \| 20 \| 20 \| 100 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A38. `batch_size`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:1020` (column: MNLI-1k)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "Batch Size \| - \| 20 \| 20 \| 100 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A39. `batch_size`

- **Paper**: `100` → 100 at `iclr2022_conference.tex:1020` (column: MNLI-10K)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "Batch Size \| - \| 20 \| 20 \| 100 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A40. `batch_size`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:1020` (column: MNLI-392K)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "Batch Size \| - \| 20 \| 20 \| 100 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A41. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:201`
  - Section: Appendix: Aren't Existing Solutions Good Enough?
  - Context: "tabular c\|ccc Batch Size \| 32 \| 16 \| 1"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: 3 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A42. `batch_size`

- **Paper**: `16` → 16 at `iclr2022_conference.tex:201`
  - Section: Appendix: Aren't Existing Solutions Good Enough?
  - Context: "tabular c\|ccc Batch Size \| 32 \| 16 \| 1"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: 3 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A43. `batch_size`

- **Paper**: `1` → 1 at `iclr2022_conference.tex:201`
  - Section: Appendix: Aren't Existing Solutions Good Enough?
  - Context: "tabular c\|ccc Batch Size \| 32 \| 16 \| 1"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A44. `batch_size`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:666` (column: RoBERTa large LoRA / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "RoBERTa large LoRA \| Batch Size \| 4 \| 4 \| 4 \| 4 \| 4 \| 4 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 32, 4):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 4 — command `--per_device_train_batch_size` at [examples/NLU/roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > MNLI"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A45. `batch_size`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:674` (column: RoBERTa large LoRA / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "RoBERTa large LoRA \| Batch Size \| 4 \| 4 \| 4 \| 4 \| 4 \| 4 \| 4 \| 4"
- **Code** (highest precedence first; likely effective: 32, 4):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 4 — command `--per_device_train_batch_size` at [examples/NLU/roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > MNLI"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A46. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:682` (column: Adpt^P (3M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (3M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A47. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:682` (column: Adpt^P (3M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (3M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A48. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:682` (column: Adpt^P (3M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (3M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A49. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:682` (column: Adpt^P (3M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (3M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A50. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:682` (column: Adpt^P (3M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (3M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A51. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:682` (column: Adpt^P (3M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (3M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A52. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:682` (column: Adpt^P (3M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (3M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A53. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:682` (column: Adpt^P (3M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (3M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A54. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:689` (column: Adpt^P (0.8M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A55. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:689` (column: Adpt^P (0.8M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A56. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:689` (column: Adpt^P (0.8M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A57. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:689` (column: Adpt^P (0.8M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A58. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:689` (column: Adpt^P (0.8M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A59. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:689` (column: Adpt^P (0.8M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A60. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:689` (column: Adpt^P (0.8M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A61. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:689` (column: Adpt^P (0.8M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^P (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A62. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:696` (column: Adpt^H (6M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (6M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A63. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:696` (column: Adpt^H (6M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (6M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A64. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:696` (column: Adpt^H (6M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (6M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A65. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:696` (column: Adpt^H (6M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (6M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A66. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:696` (column: Adpt^H (6M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (6M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A67. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:696` (column: Adpt^H (6M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (6M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A68. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:696` (column: Adpt^H (6M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (6M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A69. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:696` (column: Adpt^H (6M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (6M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A70. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:703` (column: Adpt^H (0.8M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A71. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:703` (column: Adpt^H (0.8M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A72. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:703` (column: Adpt^H (0.8M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A73. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:703` (column: Adpt^H (0.8M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A74. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:703` (column: Adpt^H (0.8M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A75. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:703` (column: Adpt^H (0.8M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A76. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:703` (column: Adpt^H (0.8M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A77. `batch_size`

- **Paper**: `32` → 32 at `iclr2022_conference.tex:703` (column: Adpt^H (0.8M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "Adpt^H (0.8M) \| Batch Size \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32 \| 32"
- **Code** (highest precedence first; likely effective: 32, 16, 4, 8):
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 32 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--per_device_train_batch_size` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 4 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A78. `batch_size`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:772` (column: E2E)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Batch Size \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 8, 1):
  - 8 — command `--train_batch_size` at [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52): `python -m torch.distributed.launch --nproc_per_node=1 src/gpt2_ft.py \`
  - 1 — command `--batch_size` at [examples/NLG/README.md:81](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L81): `python -m torch.distributed.launch --nproc_per_node=1 src/gpt2_beam.py \`
  - 10 — argparse_default `--batch_size` at [examples/NLG/src/gpt2_beam.py:45](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/gpt2_beam.py#L45): `parser.add_argument('--batch_size', type=int, default=10,`
  - 8 — argparse_default `--train_batch_size` at [examples/NLG/src/gpt2_ft.py:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/gpt2_ft.py#L47): `parser.add_argument('--train_batch_size', type=int, default=8, help='training batch size')`
- Scope: compared only with files matching "GPT-2"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A79. `batch_size`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:772` (column: WebNLG)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Batch Size \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 8, 1):
  - 8 — command `--train_batch_size` at [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52): `python -m torch.distributed.launch --nproc_per_node=1 src/gpt2_ft.py \`
  - 1 — command `--batch_size` at [examples/NLG/README.md:81](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L81): `python -m torch.distributed.launch --nproc_per_node=1 src/gpt2_beam.py \`
  - 10 — argparse_default `--batch_size` at [examples/NLG/src/gpt2_beam.py:45](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/gpt2_beam.py#L45): `parser.add_argument('--batch_size', type=int, default=10,`
  - 8 — argparse_default `--train_batch_size` at [examples/NLG/src/gpt2_ft.py:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/gpt2_ft.py#L47): `parser.add_argument('--train_batch_size', type=int, default=8, help='training batch size')`
- Scope: compared only with files matching "GPT-2"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A80. `batch_size`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:772` (column: DART)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Batch Size \| 8 \| 8 \| 8"
- **Code** (highest precedence first; likely effective: 8, 1):
  - 8 — command `--train_batch_size` at [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52): `python -m torch.distributed.launch --nproc_per_node=1 src/gpt2_ft.py \`
  - 1 — command `--batch_size` at [examples/NLG/README.md:81](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L81): `python -m torch.distributed.launch --nproc_per_node=1 src/gpt2_beam.py \`
  - 10 — argparse_default `--batch_size` at [examples/NLG/src/gpt2_beam.py:45](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/gpt2_beam.py#L45): `parser.add_argument('--batch_size', type=int, default=10,`
  - 8 — argparse_default `--train_batch_size` at [examples/NLG/src/gpt2_ft.py:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/gpt2_ft.py#L47): `parser.add_argument('--train_batch_size', type=int, default=8, help='training batch size')`
- Scope: compared only with files matching "GPT-2"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A81. `batch_size`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:794`
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "For all GPT-3 experiments, we train using AdamW for 2 epochs with a batch size of 128 samples and a weight decay factor of 0.1."
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A82. `batch_size`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:811` (column: Fine-Tune)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Batch Size \| 128 \| 128 \| 128 \| 128 \| 128 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A83. `batch_size`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:811` (column: PreEmbed)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Batch Size \| 128 \| 128 \| 128 \| 128 \| 128 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A84. `batch_size`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:811` (column: PreLayer)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Batch Size \| 128 \| 128 \| 128 \| 128 \| 128 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A85. `batch_size`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:811` (column: BitFit)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Batch Size \| 128 \| 128 \| 128 \| 128 \| 128 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A86. `batch_size`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:811` (column: Adapter^H)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Batch Size \| 128 \| 128 \| 128 \| 128 \| 128 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A87. `batch_size`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:811` (column: LoRA)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Batch Size \| 128 \| 128 \| 128 \| 128 \| 128 \| 128"
- **Code** (highest precedence first; likely effective: 8, 32, 16):
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 8 — command `--per_device_train_batch_size` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:43](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L43): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:47](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L47): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - 32 — command `--bs` at [examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh:51](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/scripts/fsmt/eval-allenai-wmt16.sh#L51): `PYTHONPATH="src:examples/seq2seq" python examples/seq2seq/run_eval.py $MODEL_PATH $DATA_DIR/val.source $SAVE_DIR/test_translations.txt --reference_path $DATA_DIR/val.target --score_path $SAVE_DIR/test`
  - … 16 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 3 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A88. `epochs`

- **Paper**: `40` → 40 at `iclr2022_conference.tex:1021` (column: MNLI-100)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "\# Epoch \| - \| 40 \| 40 \| 4 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A89. `epochs`

- **Paper**: `40` → 40 at `iclr2022_conference.tex:1021` (column: MNLI-1k)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "\# Epoch \| - \| 40 \| 40 \| 4 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A90. `epochs`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:1021` (column: MNLI-10K)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "\# Epoch \| - \| 40 \| 40 \| 4 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A91. `epochs`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:1021` (column: MNLI-392K)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "\# Epoch \| - \| 40 \| 40 \| 4 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A92. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:667` (column: RoBERTa large LoRA / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 10 \| 20 \| 20 \| 10 \| 20 \| 20 \| 30"
- **Code** (highest precedence first; likely effective: 5, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 10 — command `--num_train_epochs` at [examples/NLU/roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > MNLI"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A93. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:675` (column: RoBERTa large LoRA / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 10 \| 20 \| 20 \| 10 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 10 — command `--num_train_epochs` at [examples/NLU/roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "RoBERTa > RoBERTa large LoRA > MNLI"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A94. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:683` (column: Adpt^P (3M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A95. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:683` (column: Adpt^P (3M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A96. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:683` (column: Adpt^P (3M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A97. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:683` (column: Adpt^P (3M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A98. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:683` (column: Adpt^P (3M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A99. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:683` (column: Adpt^P (3M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A100. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:683` (column: Adpt^P (3M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A101. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:683` (column: Adpt^P (3M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A102. `epochs`

- **Paper**: `5` → 5 at `iclr2022_conference.tex:690` (column: Adpt^P (0.8M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 5 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A103. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:690` (column: Adpt^P (0.8M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 5 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A104. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:690` (column: Adpt^P (0.8M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 5 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A105. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:690` (column: Adpt^P (0.8M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 5 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A106. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:690` (column: Adpt^P (0.8M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 5 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A107. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:690` (column: Adpt^P (0.8M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 5 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A108. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:690` (column: Adpt^P (0.8M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 5 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A109. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:690` (column: Adpt^P (0.8M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 5 \| 20 \| 20 \| 20 \| 10 \| 20 \| 20 \| 20"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A110. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:697` (column: Adpt^H (6M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A111. `epochs`

- **Paper**: `5` → 5 at `iclr2022_conference.tex:697` (column: Adpt^H (6M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A112. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:697` (column: Adpt^H (6M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A113. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:697` (column: Adpt^H (6M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A114. `epochs`

- **Paper**: `5` → 5 at `iclr2022_conference.tex:697` (column: Adpt^H (6M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A115. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:697` (column: Adpt^H (6M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A116. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:697` (column: Adpt^H (6M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A117. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:697` (column: Adpt^H (6M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A118. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:704` (column: Adpt^H (0.8M) / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A119. `epochs`

- **Paper**: `5` → 5 at `iclr2022_conference.tex:704` (column: Adpt^H (0.8M) / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A120. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:704` (column: Adpt^H (0.8M) / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A121. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:704` (column: Adpt^H (0.8M) / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A122. `epochs`

- **Paper**: `5` → 5 at `iclr2022_conference.tex:704` (column: Adpt^H (0.8M) / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A123. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:704` (column: Adpt^H (0.8M) / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A124. `epochs`

- **Paper**: `20` → 20 at `iclr2022_conference.tex:704` (column: Adpt^H (0.8M) / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A125. `epochs`

- **Paper**: `10` → 10 at `iclr2022_conference.tex:704` (column: Adpt^H (0.8M) / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "\# Epochs \| 10 \| 5 \| 10 \| 10 \| 5 \| 20 \| 20 \| 10"
- **Code** (highest precedence first; likely effective: 5, 80, 30, 25, 60, 40, 20, 10):
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 80 — command `--num_train_epochs` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 30 — command `--num_train_epochs` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 8 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A126. `epochs`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:794`
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "For all GPT-3 experiments, we train using AdamW for 2 epochs with a batch size of 128 samples and a weight decay factor of 0.1."
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A127. `epochs`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:812` (column: Fine-Tune)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "\# Epoch \| 2 \| 2 \| 2 \| 2 \| 2 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A128. `epochs`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:812` (column: PreEmbed)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "\# Epoch \| 2 \| 2 \| 2 \| 2 \| 2 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A129. `epochs`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:812` (column: PreLayer)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "\# Epoch \| 2 \| 2 \| 2 \| 2 \| 2 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A130. `epochs`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:812` (column: BitFit)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "\# Epoch \| 2 \| 2 \| 2 \| 2 \| 2 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A131. `epochs`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:812` (column: Adapter^H)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "\# Epoch \| 2 \| 2 \| 2 \| 2 \| 2 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A132. `epochs`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:812` (column: LoRA)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "\# Epoch \| 2 \| 2 \| 2 \| 2 \| 2 \| 2"
- **Code** (highest precedence first; likely effective: 5):
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 5 — command `--num_train_epochs` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A133. `train_steps`

- **Paper**: `26,000` → 26000 at `iclr2022_conference.tex:1079`
  - Section: Appendix: Additional Experiments on Low-Rank Matrices > Effect of r on GPT-2
  - Context: "Using the E2E NLG Challenge dataset as an example, we report the validation loss and test metrics achieved by different choices of r after training for 26,000 steps."
- **Code** (highest precedence first; likely effective: 1):
  - 1 — code_default `max_steps` at [examples/NLG/src/optimizer.py:150](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L150): `max_steps : int = 1,`
- Note: the only value found is a function-signature default, which callers often override

### A134. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:1018` (column: MNLI-100)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "Warmup Tokens \| - \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A135. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:1018` (column: MNLI-1k)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "Warmup Tokens \| - \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A136. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:1018` (column: MNLI-10K)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "Warmup Tokens \| - \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A137. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:1018` (column: MNLI-392K)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "Warmup Tokens \| - \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A138. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:813` (column: Fine-Tune)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Warmup Tokens \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A139. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:813` (column: PreEmbed)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Warmup Tokens \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A140. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:813` (column: PreLayer)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Warmup Tokens \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A141. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:813` (column: BitFit)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Warmup Tokens \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A142. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:813` (column: Adapter^H)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Warmup Tokens \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A143. `warmup_steps`

- **Paper**: `250,000` → 250000 at `iclr2022_conference.tex:813` (column: LoRA)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "Warmup Tokens \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000 \| 250,000"
- **Code** (highest precedence first; likely effective: 1000):
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 1000 — command `--warmup_steps` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — code_default `warmup_steps` at [examples/NLG/src/optimizer.py:149](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L149): `warmup_steps : int = 0,`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A144. `optimizer`

- **Paper**: `Adam` → Adam at `iclr2022_conference.tex:136`
  - Section: Appendix: Introduction
  - Context: "We follow the conventions set out by and use Adam for model optimization and use a Transformer MLP feedforward dimension d_{ffn} = 4 x d_{model}."
- **Code** (highest precedence first; likely effective: AdamW, SGD):
  - AdamW — code_literal `optimizer` at [examples/NLG/src/optimizer.py:300](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L300): `optimizer = AdamW(`
  - SGD — code_literal `optimizer` at [examples/NLG/src/optimizer.py:312](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L312): `optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.0)`
  - AdamW — code_literal `optimizer` at [examples/NLG/src/optimizer.py:320](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L320): `optimizer = AdamW(`
- Note: the code sets 2 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A145. `optimizer`

- **Paper**: `Adam` → Adam at `iclr2022_conference.tex:295`
  - Section: Appendix: Our Method > Applying LoRA to Transformer
  - Context: "For a large Transformer trained with Adam, we reduce that VRAM usage by up to 2/3 if r\ll d_{model} as we do not need to store the optimizer states for the frozen parameters."
- **Code** (highest precedence first; likely effective: AdamW, SGD):
  - AdamW — code_literal `optimizer` at [examples/NLG/src/optimizer.py:300](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L300): `optimizer = AdamW(`
  - SGD — code_literal `optimizer` at [examples/NLG/src/optimizer.py:312](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L312): `optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.0)`
  - AdamW — code_literal `optimizer` at [examples/NLG/src/optimizer.py:320](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L320): `optimizer = AdamW(`
- Note: the code sets 2 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A146. `optimizer`

- **Paper**: `AdamW` → AdamW at `iclr2022_conference.tex:794`
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "For all GPT-3 experiments, we train using AdamW for 2 epochs with a batch size of 128 samples and a weight decay factor of 0.1."
- **Code** (highest precedence first; likely effective: AdamW, SGD):
  - AdamW — code_literal `optimizer` at [examples/NLG/src/optimizer.py:300](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L300): `optimizer = AdamW(`
  - SGD — code_literal `optimizer` at [examples/NLG/src/optimizer.py:312](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L312): `optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.0)`
  - AdamW — code_literal `optimizer` at [examples/NLG/src/optimizer.py:320](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/src/optimizer.py#L320): `optimizer = AdamW(`
- Note: 2 different values at the same precedence (code_literal); one matches, and the tool cannot tell which one this experiment used

### A147. `max_seq_length`

- **Paper**: `128` → 128 at `expt.tex:91`
  - Section: Appendix: Empirical Experiments > RoBERTa base/large
  - Context: "First, we use the same batch size for all tasks and use a sequence length of 128 to match the adapter baselines."
- **Code** (highest precedence first; likely effective: 128, 512):
  - 128 — command `--max_seq_length` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 128 — command `--max_seq_length` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 512 — command `--max_seq_length` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 512 — command `--max_seq_length` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 512 — command `--max_seq_length` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa base/large"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A148. `max_seq_length`

- **Paper**: `512` → 512 at `iclr2022_conference.tex:202`
  - Section: Appendix: Aren't Existing Solutions Good Enough?
  - Context: "Sequence Length \| 512 \| 256 \| 128"
- **Code** (highest precedence first; likely effective: 256):
  - 256 — command `--max_seq_length` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 256 — command `--max_seq_length` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 50 — config `task_specific_params.text-generation.max_length` at [examples/NLG/vocab/config.json:29](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/vocab/config.json#L29): `"max_length": 50`
  - 119 — code_default `max_len` at [examples/NLU/utils/style_doc.py:410](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/utils/style_doc.py#L410): `def style_rst_file(doc_file, max_len=119, check_only=False):`
  - 119 — code_default `max_len` at [examples/NLU/utils/style_doc.py:429](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/utils/style_doc.py#L429): `def style_docstring(docstring, max_len=119):`
  - … 4 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A149. `max_seq_length`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:202`
  - Section: Appendix: Aren't Existing Solutions Good Enough?
  - Context: "Sequence Length \| 512 \| 256 \| 128"
- **Code** (highest precedence first; likely effective: 256):
  - 256 — command `--max_seq_length` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 256 — command `--max_seq_length` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 50 — config `task_specific_params.text-generation.max_length` at [examples/NLG/vocab/config.json:29](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/vocab/config.json#L29): `"max_length": 50`
  - 119 — code_default `max_len` at [examples/NLU/utils/style_doc.py:410](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/utils/style_doc.py#L410): `def style_rst_file(doc_file, max_len=119, check_only=False):`
  - 119 — code_default `max_len` at [examples/NLU/utils/style_doc.py:429](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/utils/style_doc.py#L429): `def style_docstring(docstring, max_len=119):`
  - … 4 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A150. `max_seq_length`

- **Paper**: `128` → 128 at `iclr2022_conference.tex:639`
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "For a fair comparison with the setup in and , we restrict the model sequence length to 128 and used a fixed batch size for all tasks."
- **Code** (highest precedence first; likely effective: 128, 512):
  - 128 — command `--max_seq_length` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 128 — command `--max_seq_length` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 512 — command `--max_seq_length` at [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 512 — command `--max_seq_length` at [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 512 — command `--max_seq_length` at [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 13 more in report.json
- Scope: compared only with files matching "RoBERTa"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A151. `max_seq_length`

- **Paper**: `384` → 384 at `iclr2022_conference.tex:795`
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-3
  - Context: "We use a sequence length of 384 for WikiSQL , 768 for MNLI , and 2048 for SAMSum ."
- **Code** (highest precedence first; likely effective: 256):
  - 256 — command `--max_seq_length` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 256 — command `--max_seq_length` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 50 — config `task_specific_params.text-generation.max_length` at [examples/NLG/vocab/config.json:29](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/vocab/config.json#L29): `"max_length": 50`
  - 119 — code_default `max_len` at [examples/NLU/utils/style_doc.py:410](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/utils/style_doc.py#L410): `def style_rst_file(doc_file, max_len=119, check_only=False):`
  - 119 — code_default `max_len` at [examples/NLU/utils/style_doc.py:429](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/utils/style_doc.py#L429): `def style_docstring(docstring, max_len=119):`
  - … 4 more in report.json
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A152. `lora_rank`

- **Paper**: `2` → 2 at `expt.tex:47`
  - Section: Appendix: Empirical Experiments > Baselines
  - Context: "The number of trainable parameters is determined by the rank r and the shape of the original weights: \|\Theta\| = 2 x \hat{L}_{LoRA} x d_{model} x r, where \hat{L}_{LoRA} is the number of weight matrices we apply LoRA to."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A153. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:1031` (column: MNLI-100)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "LoRA \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A154. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:1031` (column: MNLI-1k)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "LoRA \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A155. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:1031` (column: MNLI-10K)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "LoRA \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A156. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:1031` (column: MNLI-392K)
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "LoRA \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8 \| r_q=r_v=8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A157. `lora_rank`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:1103`
  - Section: Appendix: Additional Experiments on Low-Rank Matrices > Effect of r on GPT-2
  - Context: "\caption{Validation loss and test set metrics on E2E NLG Challenge achieved by LoRA with different rank r using GPT-2 Medium."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A158. `lora_rank`

- **Paper**: `1` → 1 at `iclr2022_conference.tex:1103`
  - Section: Appendix: Additional Experiments on Low-Rank Matrices > Effect of r on GPT-2
  - Context: "Unlike on GPT-3 where r=1 suffices for many tasks, here the performance peaks at r=16 for validation loss and r=4 for BLEU, suggesting the GPT-2 Medium has a similar intrinsic rank for adaptation compared to GPT-3 175B."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: one of the several values the paper lists matches the code

### A159. `lora_rank`

- **Paper**: `16` → 16 at `iclr2022_conference.tex:1103`
  - Section: Appendix: Additional Experiments on Low-Rank Matrices > Effect of r on GPT-2
  - Context: "Unlike on GPT-3 where r=1 suffices for many tasks, here the performance peaks at r=16 for validation loss and r=4 for BLEU, suggesting the GPT-2 Medium has a similar intrinsic rank for adaptation compared to GPT-3 175B."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: the paper lists several values here (1, 16, 4)

### A160. `lora_rank`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:1103`
  - Section: Appendix: Additional Experiments on Low-Rank Matrices > Effect of r on GPT-2
  - Context: "Unlike on GPT-3 where r=1 suffices for many tasks, here the performance peaks at r=16 for validation loss and r=4 for BLEU, suggesting the GPT-2 Medium has a similar intrinsic rank for adaptation compared to GPT-3 175B."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: one of the several values the paper lists matches the code

### A161. `lora_rank`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:1129`
  - Section: Appendix: Additional Experiments on Low-Rank Matrices > Amplification Factor
  - Context: "As shown in \autoref{sec:compare_delta_w_to_w}, for r=4, this amplification factor is as large as 20."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A162. `lora_rank`

- **Paper**: `64` → 64 at `iclr2022_conference.tex:1131`
  - Section: Appendix: Additional Experiments on Low-Rank Matrices > Amplification Factor
  - Context: "One may notice, however, for r=64, this amplification factor is only around 2, meaning that most directions learned in \Delta W with r=64 are not being amplified by much."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A163. `lora_rank`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:1133`
  - Section: Appendix: Additional Experiments on Low-Rank Matrices > Amplification Factor
  - Context: "In contrast, those directions in the rank-4 version of \Delta W (corresponding to r=4) are amplified by a much larger factor 20."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A164. `lora_rank`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:297`
  - Section: Appendix: Our Method > Applying LoRA to Transformer
  - Context: "With r=4 and only the query and value projection matrices being adapted, the checkpoint size is reduced by roughly 10,000x (from 350GB to 35MB)\footnote{We still need the 350GB model during deployment; however, storing 100 adapted models only requires 350GB + 35MB * 100 \approx 354GB as opposed t..."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A165. `lora_rank`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:376`
  - Section: Appendix: Understanding the Low-Rank Updates > Which Weight Matrices in Transformer Should We Apply LoRA to?
  - Context: "We set a parameter budget of 18M (roughly 35MB if stored in FP16) on GPT-3 175B, which corresponds to r=8 if we adapt one type of attention weights or r=4 if we adapt two types, for all 96 layers."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A166. `lora_rank`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:376`
  - Section: Appendix: Understanding the Low-Rank Updates > Which Weight Matrices in Transformer Should We Apply LoRA to?
  - Context: "We set a parameter budget of 18M (roughly 35MB if stored in FP16) on GPT-3 175B, which corresponds to r=8 if we adapt one type of attention weights or r=4 if we adapt two types, for all 96 layers."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A167. `lora_rank`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:387` (column: \# of Trainable Parameters = 18M)
  - Section: Appendix: Understanding the Low-Rank Updates > Which Weight Matrices in Transformer Should We Apply LoRA to?
  - Context: "Rank r \| 8 \| 8 \| 8 \| 8 \| 4 \| 4 \| 2"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A168. `lora_rank`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:387` (column: \# of Trainable Parameters = 18M)
  - Section: Appendix: Understanding the Low-Rank Updates > Which Weight Matrices in Transformer Should We Apply LoRA to?
  - Context: "Rank r \| 8 \| 8 \| 8 \| 8 \| 4 \| 4 \| 2"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A169. `lora_rank`

- **Paper**: `2` → 2 at `iclr2022_conference.tex:387` (column: \# of Trainable Parameters = 18M)
  - Section: Appendix: Understanding the Low-Rank Updates > Which Weight Matrices in Transformer Should We Apply LoRA to?
  - Context: "Rank r \| 8 \| 8 \| 8 \| 8 \| 4 \| 4 \| 2"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A170. `lora_rank`

- **Paper**: `r=1` → 1 at `iclr2022_conference.tex:413`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "tabular r\|c\|ccccc \| Weight Type \| r=1 \| r=2 \| r=4 \| r=8 \| r=64"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A171. `lora_rank`

- **Paper**: `r=2` → 2 at `iclr2022_conference.tex:413`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "tabular r\|c\|ccccc \| Weight Type \| r=1 \| r=2 \| r=4 \| r=8 \| r=64"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A172. `lora_rank`

- **Paper**: `r=4` → 4 at `iclr2022_conference.tex:413`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "tabular r\|c\|ccccc \| Weight Type \| r=1 \| r=2 \| r=4 \| r=8 \| r=64"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A173. `lora_rank`

- **Paper**: `r=8` → 8 at `iclr2022_conference.tex:413`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "tabular r\|c\|ccccc \| Weight Type \| r=1 \| r=2 \| r=4 \| r=8 \| r=64"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A174. `lora_rank`

- **Paper**: `r=64` → 64 at `iclr2022_conference.tex:413`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "tabular r\|c\|ccccc \| Weight Type \| r=1 \| r=2 \| r=4 \| r=8 \| r=64"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A175. `lora_rank`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:436`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\parhead{Subspace similarity between different r} Given A_{r=8} and A_{r=64} which are the learned adaptation matrices with rank r = 8 and 64 using the same pre-trained model, we perform singular value decomposition and obtain the right-singular unitary matrices U_{A_{r=8}} and U_{A_{r=64}}."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A176. `lora_rank`

- **Paper**: `64` → 64 at `iclr2022_conference.tex:436`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\parhead{Subspace similarity between different r} Given A_{r=8} and A_{r=64} which are the learned adaptation matrices with rank r = 8 and 64 using the same pre-trained model, we perform singular value decomposition and obtain the right-singular unitary matrices U_{A_{r=8}} and U_{A_{r=64}}."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A177. `lora_rank`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:438`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\footnote{Note that a similar analysis can be carried out with B and the left-singular unitary matrices -- we stick with A for our experiments.} We hope to answer: how much of the subspace spanned by the top i singular vectors in U_{A_{r=8}} (for 1\leq i \leq 8) is contained in the subspace spann..."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A178. `lora_rank`

- **Paper**: `64` → 64 at `iclr2022_conference.tex:438`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\footnote{Note that a similar analysis can be carried out with B and the left-singular unitary matrices -- we stick with A for our experiments.} We hope to answer: how much of the subspace spanned by the top i singular vectors in U_{A_{r=8}} (for 1\leq i \leq 8) is contained in the subspace spann..."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A179. `lora_rank`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:441`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\footnote{Note that a similar analysis can be carried out with B and the left-singular unitary matrices -- we stick with A for our experiments.} We hope to answer: how much of the subspace spanned by the top i singular vectors in U_{A_{r=8}} (for 1\leq i \leq 8) is contained in the subspace spann..."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A180. `lora_rank`

- **Paper**: `64` → 64 at `iclr2022_conference.tex:441`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\footnote{Note that a similar analysis can be carried out with B and the left-singular unitary matrices -- we stick with A for our experiments.} We hope to answer: how much of the subspace spanned by the top i singular vectors in U_{A_{r=8}} (for 1\leq i \leq 8) is contained in the subspace spann..."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A181. `lora_rank`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:445`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "where U_{A_{r=8}}^i represents the columns of U_{A_{r=8}} corresponding to the top-i singular vectors."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A182. `lora_rank`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:461`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\begin{center} \parbox{0.85\linewidth}{ Directions corresponding to the top singular vector overlap significantly between A_{r=8} and A_{r=64}, while others do not."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A183. `lora_rank`

- **Paper**: `64` → 64 at `iclr2022_conference.tex:461`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\begin{center} \parbox{0.85\linewidth}{ Directions corresponding to the top singular vector overlap significantly between A_{r=8} and A_{r=64}, while others do not."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A184. `lora_rank`

- **Paper**: `1` → 1 at `iclr2022_conference.tex:461`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\Delta W_q) of A_{r=64} share a subspace of dimension 1 with normalized similarity >0.5, providing an explanation of why r=1 performs quite well in our downstream tasks for GPT-3.} \end{center}"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A185. `lora_rank`

- **Paper**: `8` → 8 at `iclr2022_conference.tex:464`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "Since both A_{r=8} and A_{r=64} are learned using the same pre-trained model, \autoref{fig:qv8_qv64} indicates that the top singular-vector directions of A_{r=8} and A_{r=64} are the most useful, while other directions potentially contain mostly random noises accumulated during training."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A186. `lora_rank`

- **Paper**: `64` → 64 at `iclr2022_conference.tex:464`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "Since both A_{r=8} and A_{r=64} are learned using the same pre-trained model, \autoref{fig:qv8_qv64} indicates that the top singular-vector directions of A_{r=8} and A_{r=64} are the most useful, while other directions potentially contain mostly random noises accumulated during training."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A187. `lora_rank`

- **Paper**: `64` → 64 at `iclr2022_conference.tex:476`
  - Section: Appendix: Understanding the Low-Rank Updates > What is the Optimal Rank r for LoRA?
  - Context: "\parhead{Subspace similarity between different random seeds} We further confirm this by plotting the normalized subspace similarity between two randomly seeded runs with r=64, shown in \autoref{fig:UA_across_random_seeds}."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A188. `lora_rank`

- **Paper**: `r=4` → 4 at `iclr2022_conference.tex:498`
  - Section: Appendix: Understanding the Low-Rank Updates > How Does the Adaptation Matrix W Compare to W?
  - Context: "tabular c\|ccc\|ccc \| r=4 \| r=4 \| r=4 \| r=64 \| r=64 \| r=64"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A189. `lora_rank`

- **Paper**: `r=64` → 64 at `iclr2022_conference.tex:498`
  - Section: Appendix: Understanding the Low-Rank Updates > How Does the Adaptation Matrix W Compare to W?
  - Context: "tabular c\|ccc\|ccc \| r=4 \| r=4 \| r=4 \| r=64 \| r=64 \| r=64"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A190. `lora_rank`

- **Paper**: `4` → 4 at `iclr2022_conference.tex:516`
  - Section: Appendix: Understanding the Low-Rank Updates > How Does the Adaptation Matrix W Compare to W?
  - Context: "Third, the amplification factor is rather huge: 21.5\approx 6.91/0.32 for r=4."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A191. `lora_rank`

- **Paper**: `64` → 64 at `iclr2022_conference.tex:517`
  - Section: Appendix: Understanding the Low-Rank Updates > How Does the Adaptation Matrix W Compare to W?
  - Context: "See \autoref{app:amplification_factor} for why r=64 has a smaller amplification factor."
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A192. `lora_rank`

- **Paper**: `r=1` → 1 at `iclr2022_conference.tex:951` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "5 * Adapter^ H \| r=1 \| 7.1 M \| 71.9 \| 89.8"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A193. `lora_rank`

- **Paper**: `r=4` → 4 at `iclr2022_conference.tex:952` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r=4 \| 21.2 M \| 73.2 \| 91.0"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A194. `lora_rank`

- **Paper**: `r=8` → 8 at `iclr2022_conference.tex:953` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r=8 \| 40.1 M \| 73.2 \| 91.5"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A195. `lora_rank`

- **Paper**: `r=64` → 64 at `iclr2022_conference.tex:955` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r=64 \| 304.4 M \| 72.6 \| 91.5"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A196. `lora_rank`

- **Paper**: `r_{v}=2` → 2 at `iclr2022_conference.tex:957` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "LoRA \| r_ v =2 \| 4.7 M \| 73.4 \| 91.7"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A197. `lora_rank`

- **Paper**: `r_q=r_v=1` → 1 at `iclr2022_conference.tex:958` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_v=1 \| 4.7 M \| 73.4 \| 91.3"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A198. `lora_rank`

- **Paper**: `r_q=r_v=2` → 2 at `iclr2022_conference.tex:959` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_v=2 \| 9.4 M \| 73.3 \| 91.4"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A199. `lora_rank`

- **Paper**: `r_q=r_k=r_v=r_o=1` → 1 at `iclr2022_conference.tex:960` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_k=r_v=r_o=1 \| 9.4 M \| 74.1 \| 91.2"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A200. `lora_rank`

- **Paper**: `r_q=r_v=4` → 4 at `iclr2022_conference.tex:961` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_v=4 \| 18.8 M \| 73.7 \| 91.3"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A201. `lora_rank`

- **Paper**: `r_q=r_k=r_v=r_o=2` → 2 at `iclr2022_conference.tex:962` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_k=r_v=r_o=2 \| 18.8 M \| 73.7 \| 91.7"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A202. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:963` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_v=8 \| 37.7 M \| 73.8 \| 91.6"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A203. `lora_rank`

- **Paper**: `r_q=r_k=r_v=r_o=4` → 4 at `iclr2022_conference.tex:964` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_k=r_v=r_o=4 \| 37.7 M \| 74.0 \| 91.7"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A204. `lora_rank`

- **Paper**: `r_q=r_v=64` → 64 at `iclr2022_conference.tex:965` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_v=64 \| 301.9 M \| 73.6 \| 91.4"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A205. `lora_rank`

- **Paper**: `r_q=r_k=r_v=r_o=64` → 64 at `iclr2022_conference.tex:966` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_k=r_v=r_o=64 \| 603.8 M \| 73.9 \| 91.4"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A206. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:968` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "LoRA+PE \| r_q=r_v=8, l_p=8, l_i=4 \| 37.8 M \| 75.0 \| 91.4"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A207. `lora_rank`

- **Paper**: `r_q=r_v=32` → 32 at `iclr2022_conference.tex:969` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_v=32, l_p=8, l_i=4 \| 151.1 M \| 75.9 \| 91.1"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A208. `lora_rank`

- **Paper**: `r_q=r_v=64` → 64 at `iclr2022_conference.tex:970` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "r_q=r_v=64, l_p=8, l_i=4 \| 302.1 M \| 76.2 \| 91.3"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

### A209. `lora_rank`

- **Paper**: `r_q=r_v=8` → 8 at `iclr2022_conference.tex:972` (column: Hyperparameters)
  - Section: Appendix: Additional Empirical Experiments > Additional Experiments on GPT-3
  - Context: "LoRA+PL \| r_q=r_v=8, l_p=8, l_i=4 \| 52.8 M \| 72.9 \| 90.2"
- **Code** (highest precedence first; likely effective: 16):
  - 16 — command `--lora_r` at [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69): `python -m torch.distributed.launch --nproc_per_node=1 examples/text-classification/run_glue.py \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 16 — command `--lora_r` at [examples/NLU/mnli.rdrop.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.rdrop.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
- Scope: compared only with files matching "files not tied to another section"
- Note: no section or table title points at a specific file, so the code compared here may belong to a different experiment

## Missing in code — stated in the paper, not found in the code (22)

### M1. `epochs`

- **Paper**: `5` → 5 at `iclr2022_conference.tex:754`
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "We train all of our GPT-2 models using AdamW with a linear learning rate schedule for 5 epochs."
- Scope: compared only with files matching "GPT-2"
- Note: not set in the files this section points to

### M2. `epochs`

- **Paper**: `5` → 5 at `iclr2022_conference.tex:773` (column: E2E)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "\# Epoch \| 5 \| 5 \| 5"
- Scope: compared only with files matching "GPT-2"
- Note: not set in the files this section points to

### M3. `epochs`

- **Paper**: `5` → 5 at `iclr2022_conference.tex:773` (column: WebNLG)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "\# Epoch \| 5 \| 5 \| 5"
- Scope: compared only with files matching "GPT-2"
- Note: not set in the files this section points to

### M4. `epochs`

- **Paper**: `5` → 5 at `iclr2022_conference.tex:773` (column: DART)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "\# Epoch \| 5 \| 5 \| 5"
- Scope: compared only with files matching "GPT-2"
- Note: not set in the files this section points to

### M5. `warmup_steps`

- **Paper**: `500` → 500 at `iclr2022_conference.tex:774` (column: E2E)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Warmup Steps \| 500 \| 500 \| 500"
- Scope: compared only with files matching "GPT-2"
- Note: not set in the files this section points to

### M6. `warmup_steps`

- **Paper**: `500` → 500 at `iclr2022_conference.tex:774` (column: WebNLG)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Warmup Steps \| 500 \| 500 \| 500"
- Scope: compared only with files matching "GPT-2"
- Note: not set in the files this section points to

### M7. `warmup_steps`

- **Paper**: `500` → 500 at `iclr2022_conference.tex:774` (column: DART)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Warmup Steps \| 500 \| 500 \| 500"
- Scope: compared only with files matching "GPT-2"
- Note: not set in the files this section points to

### M8. `dropout`

- **Paper**: `0.15` → 0.15 at `iclr2022_conference.tex:742` (column: DeBERTa XXL LoRA / MNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "CLS Dropout \| 0.15 \| 0 \| 0 \| 0.1 \| 0.1 \| 0.2 \| 0.2 \| 0.2"
- Note: no setting with this name found in the code

### M9. `dropout`

- **Paper**: `0` → 0 at `iclr2022_conference.tex:742` (column: DeBERTa XXL LoRA / SST-2)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "CLS Dropout \| 0.15 \| 0 \| 0 \| 0.1 \| 0.1 \| 0.2 \| 0.2 \| 0.2"
- Note: no setting with this name found in the code

### M10. `dropout`

- **Paper**: `0` → 0 at `iclr2022_conference.tex:742` (column: DeBERTa XXL LoRA / MRPC)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "CLS Dropout \| 0.15 \| 0 \| 0 \| 0.1 \| 0.1 \| 0.2 \| 0.2 \| 0.2"
- Note: no setting with this name found in the code

### M11. `dropout`

- **Paper**: `0.1` → 0.1 at `iclr2022_conference.tex:742` (column: DeBERTa XXL LoRA / CoLA)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "CLS Dropout \| 0.15 \| 0 \| 0 \| 0.1 \| 0.1 \| 0.2 \| 0.2 \| 0.2"
- Note: no setting with this name found in the code

### M12. `dropout`

- **Paper**: `0.1` → 0.1 at `iclr2022_conference.tex:742` (column: DeBERTa XXL LoRA / QNLI)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "CLS Dropout \| 0.15 \| 0 \| 0 \| 0.1 \| 0.1 \| 0.2 \| 0.2 \| 0.2"
- Note: no setting with this name found in the code

### M13. `dropout`

- **Paper**: `0.2` → 0.2 at `iclr2022_conference.tex:742` (column: DeBERTa XXL LoRA / QQP)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "CLS Dropout \| 0.15 \| 0 \| 0 \| 0.1 \| 0.1 \| 0.2 \| 0.2 \| 0.2"
- Note: no setting with this name found in the code

### M14. `dropout`

- **Paper**: `0.2` → 0.2 at `iclr2022_conference.tex:742` (column: DeBERTa XXL LoRA / RTE)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "CLS Dropout \| 0.15 \| 0 \| 0 \| 0.1 \| 0.1 \| 0.2 \| 0.2 \| 0.2"
- Note: no setting with this name found in the code

### M15. `dropout`

- **Paper**: `0.2` → 0.2 at `iclr2022_conference.tex:742` (column: DeBERTa XXL LoRA / STS-B)
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "CLS Dropout \| 0.15 \| 0 \| 0 \| 0.1 \| 0.1 \| 0.2 \| 0.2 \| 0.2"
- Note: no setting with this name found in the code

### M16. `dropout`

- **Paper**: `0.1` → 0.1 at `iclr2022_conference.tex:771` (column: E2E)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Dropout Prob \| 0.1 \| 0.1 \| 0.0"
- Note: no setting with this name found in the code

### M17. `dropout`

- **Paper**: `0.1` → 0.1 at `iclr2022_conference.tex:771` (column: WebNLG)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Dropout Prob \| 0.1 \| 0.1 \| 0.0"
- Note: no setting with this name found in the code

### M18. `dropout`

- **Paper**: `0.0` → 0 at `iclr2022_conference.tex:771` (column: DART)
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "Dropout Prob \| 0.1 \| 0.1 \| 0.0"
- Note: no setting with this name found in the code

### M19. `optimizer`

- **Paper**: `AdamW` → AdamW at `iclr2022_conference.tex:635`
  - Section: Appendix: Hyperparameters Used in Experiments > RoBERTa
  - Context: "We train using AdamW with a linear learning rate decay schedule."
- Scope: compared only with files matching "RoBERTa"
- Note: not set in the files this section points to

### M20. `optimizer`

- **Paper**: `AdamW` → AdamW at `iclr2022_conference.tex:717`
  - Section: Appendix: Hyperparameters Used in Experiments > DeBERTa
  - Context: "We again train using AdamW with a linear learning rate decay schedule."
- Scope: compared only with files matching "DeBERTa"
- Note: not set in the files this section points to

### M21. `optimizer`

- **Paper**: `AdamW` → AdamW at `iclr2022_conference.tex:754`
  - Section: Appendix: Hyperparameters Used in Experiments > GPT-2
  - Context: "We train all of our GPT-2 models using AdamW with a linear learning rate schedule for 5 epochs."
- Scope: compared only with files matching "GPT-2"
- Note: not set in the files this section points to

### M22. `num_train_samples`

- **Paper**: `10k` → 10000 at `iclr2022_conference.tex:984`
  - Section: Appendix: Additional Empirical Experiments > Low-Data Regime
  - Context: "To evaluate the performance of different adaptation approaches in the low-data regime. we randomly sample 100, 1k and 10k training examples from the full training set of MNLI to form the low-data MNLI-n tasks."
- Note: no setting with this name found in the code

## Missing in paper — set in the code, never mentioned in the paper (1)

### M1. `seed`

- **Code** (highest precedence first; likely effective: 110, 0, 42):
  - 110 — command `--random_seed` at [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52): `python -m torch.distributed.launch --nproc_per_node=1 src/gpt2_ft.py \`
  - 0 — command `--seed` at [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0 — command `--seed` at [examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_pfeiffer_roberta_large_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=num_gpus \`
  - 0 — command `--seed` at [examples/NLU/deberta_v2_xxlarge_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_cola.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - 0 — command `--seed` at [examples/NLU/deberta_v2_xxlarge_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mnli.sh#L5): `python -m torch.distributed.launch --nproc_per_node=$num_gpus \`
  - … 25 more in report.json
- Note: the code sets this but the paper never mentions it

## Matches (144)

| Setting | Paper | Paper location | Code | Code location |
|---|---|---|---|---|
| learning_rate | 5E-04 | `iclr2022_conference.tex:660` | 0.0005 (command) | [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5) |
| learning_rate | 5E-04 | `iclr2022_conference.tex:660` | 0.0005 (command) | [examples/NLU/roberta_base_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_sst2.sh#L5) |
| learning_rate | 4E-04 | `iclr2022_conference.tex:660` | 0.0004 (command) | [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5) |
| learning_rate | 4E-04 | `iclr2022_conference.tex:660` | 0.0004 (command) | [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5) |
| learning_rate | 4E-04 | `iclr2022_conference.tex:660` | 0.0004 (command) | [examples/NLU/roberta_base_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qnli.sh#L5) |
| learning_rate | 5E-04 | `iclr2022_conference.tex:660` | 0.0005 (command) | [examples/NLU/roberta_base_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qqp.sh#L5) |
| learning_rate | 5E-04 | `iclr2022_conference.tex:660` | 0.0005 (command) | [examples/NLU/roberta_base_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_rte.sh#L5) |
| learning_rate | 4E-04 | `iclr2022_conference.tex:660` | 0.0004 (command) | [examples/NLU/roberta_base_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_stsb.sh#L5) |
| learning_rate | 3E-04 | `iclr2022_conference.tex:668` | 0.0003 (command) | [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5) |
| learning_rate | 4E-04 | `iclr2022_conference.tex:668` | 0.0004 (command) | [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5) |
| learning_rate | 3E-04 | `iclr2022_conference.tex:668` | 0.0003 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| learning_rate | 2E-04 | `iclr2022_conference.tex:668` | 0.0002 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| learning_rate | 3E-04 | `iclr2022_conference.tex:668` | 0.0003 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| learning_rate | 4E-04 | `iclr2022_conference.tex:668` | 0.0004 (command) | [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5) |
| learning_rate | 3E-04 | `iclr2022_conference.tex:676` | 0.0003 (command) | [examples/NLU/adapter_houlsby_roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/adapter_houlsby_roberta_large_mnli.sh#L5) |
| learning_rate | 4E-04 | `iclr2022_conference.tex:676` | 0.0004 (command) | [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5) |
| learning_rate | 3E-04 | `iclr2022_conference.tex:676` | 0.0003 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| learning_rate | 2E-04 | `iclr2022_conference.tex:676` | 0.0002 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| learning_rate | 3E-04 | `iclr2022_conference.tex:676` | 0.0003 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| learning_rate | 4E-04 | `iclr2022_conference.tex:676` | 0.0004 (command) | [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5) |
| learning_rate | 1E-04 | `iclr2022_conference.tex:740` | 0.0001 (command) | [examples/NLU/deberta_v2_xxlarge_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mnli.sh#L5) |
| learning_rate | 6E-05 | `iclr2022_conference.tex:740` | 6e-05 (command) | [examples/NLU/deberta_v2_xxlarge_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_sst2.sh#L5) |
| learning_rate | 2E-04 | `iclr2022_conference.tex:740` | 0.0002 (command) | [examples/NLU/deberta_v2_xxlarge_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mrpc.sh#L5) |
| learning_rate | 1E-04 | `iclr2022_conference.tex:740` | 0.0001 (command) | [examples/NLU/deberta_v2_xxlarge_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qnli.sh#L5) |
| learning_rate | 1E-04 | `iclr2022_conference.tex:740` | 0.0001 (command) | [examples/NLU/deberta_v2_xxlarge_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qqp.sh#L5) |
| learning_rate | 2E-04 | `iclr2022_conference.tex:740` | 0.0002 (command) | [examples/NLU/deberta_v2_xxlarge_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_stsb.sh#L5) |
| learning_rate | 0.0002 | `iclr2022_conference.tex:777` | 0.0002 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| learning_rate | 0.0002 | `iclr2022_conference.tex:777` | 0.0002 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| learning_rate | 0.0002 | `iclr2022_conference.tex:777` | 0.0002 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| learning_rate | 1.00E-04 | `iclr2022_conference.tex:816` | 0.0001 (command) | [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5) |
| learning_rate | 1.00E-04 | `iclr2022_conference.tex:816` | 0.0001 (command) | [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5) |
| batch_size | 16 | `iclr2022_conference.tex:658` | 16 (command) | [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5) |
| batch_size | 16 | `iclr2022_conference.tex:658` | 16 (command) | [examples/NLU/roberta_base_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_sst2.sh#L5) |
| batch_size | 16 | `iclr2022_conference.tex:658` | 16 (command) | [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5) |
| batch_size | 32 | `iclr2022_conference.tex:658` | 32 (command) | [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5) |
| batch_size | 32 | `iclr2022_conference.tex:658` | 32 (command) | [examples/NLU/roberta_base_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qnli.sh#L5) |
| batch_size | 16 | `iclr2022_conference.tex:658` | 16 (command) | [examples/NLU/roberta_base_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qqp.sh#L5) |
| batch_size | 32 | `iclr2022_conference.tex:658` | 32 (command) | [examples/NLU/roberta_base_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_rte.sh#L5) |
| batch_size | 16 | `iclr2022_conference.tex:658` | 16 (command) | [examples/NLU/roberta_base_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_stsb.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:666` | 4 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:666` | 4 (command) | [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:666` | 4 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:666` | 4 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| batch_size | 8 | `iclr2022_conference.tex:666` | 8 (command) | [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:674` | 4 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:674` | 4 (command) | [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:674` | 4 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:674` | 4 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:674` | 4 (command) | [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5) |
| batch_size | 8 | `iclr2022_conference.tex:738` | 8 (command) | [examples/NLU/deberta_v2_xxlarge_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mnli.sh#L5) |
| batch_size | 8 | `iclr2022_conference.tex:738` | 8 (command) | [examples/NLU/deberta_v2_xxlarge_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_sst2.sh#L5) |
| batch_size | 32 | `iclr2022_conference.tex:738` | 32 (command) | [examples/NLU/deberta_v2_xxlarge_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mrpc.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:738` | 4 (command) | [examples/NLU/deberta_v2_xxlarge_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_cola.sh#L5) |
| batch_size | 6 | `iclr2022_conference.tex:738` | 6 (command) | [examples/NLU/deberta_v2_xxlarge_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qnli.sh#L5) |
| batch_size | 8 | `iclr2022_conference.tex:738` | 8 (command) | [examples/NLU/deberta_v2_xxlarge_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qqp.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:738` | 4 (command) | [examples/NLU/deberta_v2_xxlarge_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_rte.sh#L5) |
| batch_size | 4 | `iclr2022_conference.tex:738` | 4 (command) | [examples/NLU/deberta_v2_xxlarge_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_stsb.sh#L5) |
| epochs | 30 | `iclr2022_conference.tex:659` | 30 (command) | [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5) |
| epochs | 60 | `iclr2022_conference.tex:659` | 60 (command) | [examples/NLU/roberta_base_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_sst2.sh#L5) |
| epochs | 30 | `iclr2022_conference.tex:659` | 30 (command) | [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5) |
| epochs | 80 | `iclr2022_conference.tex:659` | 80 (command) | [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5) |
| epochs | 25 | `iclr2022_conference.tex:659` | 25 (command) | [examples/NLU/roberta_base_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qnli.sh#L5) |
| epochs | 25 | `iclr2022_conference.tex:659` | 25 (command) | [examples/NLU/roberta_base_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qqp.sh#L5) |
| epochs | 80 | `iclr2022_conference.tex:659` | 80 (command) | [examples/NLU/roberta_base_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_rte.sh#L5) |
| epochs | 40 | `iclr2022_conference.tex:659` | 40 (command) | [examples/NLU/roberta_base_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_stsb.sh#L5) |
| epochs | 10 | `iclr2022_conference.tex:667` | 10 (command) | [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5) |
| epochs | 20 | `iclr2022_conference.tex:667` | 20 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| epochs | 20 | `iclr2022_conference.tex:667` | 20 (command) | [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5) |
| epochs | 10 | `iclr2022_conference.tex:667` | 10 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| epochs | 20 | `iclr2022_conference.tex:667` | 20 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| epochs | 20 | `iclr2022_conference.tex:667` | 20 (command) | [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5) |
| epochs | 10 | `iclr2022_conference.tex:675` | 10 (command) | [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5) |
| epochs | 20 | `iclr2022_conference.tex:675` | 20 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| epochs | 20 | `iclr2022_conference.tex:675` | 20 (command) | [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5) |
| epochs | 10 | `iclr2022_conference.tex:675` | 10 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| epochs | 20 | `iclr2022_conference.tex:675` | 20 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| epochs | 20 | `iclr2022_conference.tex:675` | 20 (command) | [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5) |
| epochs | 10 | `iclr2022_conference.tex:675` | 10 (command) | [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5) |
| epochs | 5 | `iclr2022_conference.tex:739` | 5 (command) | [examples/NLU/deberta_v2_xxlarge_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mnli.sh#L5) |
| epochs | 16 | `iclr2022_conference.tex:739` | 16 (command) | [examples/NLU/deberta_v2_xxlarge_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_sst2.sh#L5) |
| epochs | 30 | `iclr2022_conference.tex:739` | 30 (command) | [examples/NLU/deberta_v2_xxlarge_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mrpc.sh#L5) |
| epochs | 10 | `iclr2022_conference.tex:739` | 10 (command) | [examples/NLU/deberta_v2_xxlarge_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_cola.sh#L5) |
| epochs | 8 | `iclr2022_conference.tex:739` | 8 (command) | [examples/NLU/deberta_v2_xxlarge_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qnli.sh#L5) |
| epochs | 11 | `iclr2022_conference.tex:739` | 11 (command) | [examples/NLU/deberta_v2_xxlarge_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qqp.sh#L5) |
| epochs | 11 | `iclr2022_conference.tex:739` | 11 (command) | [examples/NLU/deberta_v2_xxlarge_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_rte.sh#L5) |
| epochs | 10 | `iclr2022_conference.tex:739` | 10 (command) | [examples/NLU/deberta_v2_xxlarge_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_stsb.sh#L5) |
| weight_decay | 0 | `iclr2022_conference.tex:741` | 0 (command) | [examples/NLU/deberta_v2_xxlarge_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mnli.sh#L5) |
| weight_decay | 0.01 | `iclr2022_conference.tex:741` | 0.01 (command) | [examples/NLU/deberta_v2_xxlarge_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_sst2.sh#L5) |
| weight_decay | 0.01 | `iclr2022_conference.tex:741` | 0.01 (command) | [examples/NLU/deberta_v2_xxlarge_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_mrpc.sh#L5) |
| weight_decay | 0 | `iclr2022_conference.tex:741` | 0 (command) | [examples/NLU/deberta_v2_xxlarge_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_cola.sh#L5) |
| weight_decay | 0.01 | `iclr2022_conference.tex:741` | 0.01 (command) | [examples/NLU/deberta_v2_xxlarge_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qnli.sh#L5) |
| weight_decay | 0.01 | `iclr2022_conference.tex:741` | 0.01 (command) | [examples/NLU/deberta_v2_xxlarge_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_qqp.sh#L5) |
| weight_decay | 0.01 | `iclr2022_conference.tex:741` | 0.01 (command) | [examples/NLU/deberta_v2_xxlarge_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_rte.sh#L5) |
| weight_decay | 0.1 | `iclr2022_conference.tex:741` | 0.1 (command) | [examples/NLU/deberta_v2_xxlarge_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/deberta_v2_xxlarge_stsb.sh#L5) |
| weight_decay | 0.01 | `iclr2022_conference.tex:770` | 0.01 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| weight_decay | 0.01 | `iclr2022_conference.tex:770` | 0.01 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| max_seq_length | 256 | `iclr2022_conference.tex:202` | 256 (command) | [examples/NLU/mnli.cutoff.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/mnli.cutoff.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:661` | 8 (command) | [examples/NLU/roberta_base_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mnli.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:661` | 8 (command) | [examples/NLU/roberta_base_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_sst2.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:661` | 8 (command) | [examples/NLU/roberta_base_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_mrpc.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:661` | 8 (command) | [examples/NLU/roberta_base_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_cola.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:661` | 8 (command) | [examples/NLU/roberta_base_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qnli.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:661` | 8 (command) | [examples/NLU/roberta_base_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_qqp.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:661` | 8 (command) | [examples/NLU/roberta_base_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_rte.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:661` | 8 (command) | [examples/NLU/roberta_base_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_base_stsb.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:669` | 8 (command) | [examples/NLU/roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mnli.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:669` | 8 (command) | [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:669` | 8 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:669` | 8 (command) | [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:669` | 8 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:669` | 8 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:669` | 8 (command) | [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:669` | 8 (command) | [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:677` | 8 (command) | [examples/NLU/roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mnli.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:677` | 8 (command) | [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:677` | 8 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:677` | 8 (command) | [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:677` | 8 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:677` | 8 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:677` | 8 (command) | [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5) |
| lora_rank | r_q=r_v=8 | `iclr2022_conference.tex:677` | 8 (command) | [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5) |
| lora_rank | r_q=r_v=4 | `iclr2022_conference.tex:778` | 4 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| lora_rank | r_q=r_v=4 | `iclr2022_conference.tex:778` | 4 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| lora_rank | r_q=r_v=4 | `iclr2022_conference.tex:778` | 4 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| lora_rank | r=16 | `iclr2022_conference.tex:954` | 16 (command) | [examples/NLU/README.md:69](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/README.md#L69) |
| lora_alpha | 16 | `iclr2022_conference.tex:670` | 16 (command) | [examples/NLU/roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mnli.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:670` | 16 (command) | [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:670` | 16 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:670` | 16 (command) | [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:670` | 16 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:670` | 16 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:670` | 16 (command) | [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:670` | 16 (command) | [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:678` | 16 (command) | [examples/NLU/roberta_large_mnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mnli.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:678` | 16 (command) | [examples/NLU/roberta_large_sst2.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_sst2.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:678` | 16 (command) | [examples/NLU/roberta_large_mrpc.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_mrpc.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:678` | 16 (command) | [examples/NLU/roberta_large_cola.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_cola.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:678` | 16 (command) | [examples/NLU/roberta_large_qnli.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qnli.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:678` | 16 (command) | [examples/NLU/roberta_large_qqp.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_qqp.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:678` | 16 (command) | [examples/NLU/roberta_large_rte.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_rte.sh#L5) |
| lora_alpha | 16 | `iclr2022_conference.tex:678` | 16 (command) | [examples/NLU/roberta_large_stsb.sh:5](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLU/roberta_large_stsb.sh#L5) |
| lora_alpha | 32 | `iclr2022_conference.tex:779` | 32 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| lora_alpha | 32 | `iclr2022_conference.tex:779` | 32 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
| lora_alpha | 32 | `iclr2022_conference.tex:779` | 32 (command) | [examples/NLG/README.md:52](https://github.com/microsoft/LoRA/blob/c4593f060e6a368d7bb5af5273b8e42810cdef90/examples/NLG/README.md#L52) |
