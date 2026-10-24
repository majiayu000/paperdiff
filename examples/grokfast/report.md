# paperdiff report: arXiv:2405.20233

- Paper: arXiv:2405.20233 (LaTeX source, main file `main.tex`)
- Title: Grokfast: Accelerated Grokking by \ Amplifying Slow Gradients
- Code: https://github.com/ironjr/grokfast @ `93b2248e351d`
- Generated: 2026-10-24T19:46:38Z by paperdiff 0.1.0

| Category | Count |
|---|---|
| conflict | 0 |
| ambiguous | 1 |
| missing_in_code | 10 |
| missing_in_paper | 1 |
| match | 24 |

> paperdiff reports differences between what a paper states and what its code configures. A difference can come from a typo, a later code change, a setting defined elsewhere, a reasonable implementation choice, or an extraction error by this tool. It is not a judgement about whether the paper is correct, and it is not an accusation of misconduct. Check each item by hand before citing it.

## Ambiguous — several values, or the paper value is overridden (1)

### A1. `hidden_size`

- **Paper**: `128` → 128 at `sections/B_implementation.tex:10`
  - Section: Appendix: Task Details > Binary Operation (Algorithmic Data)
  - Context: "The network is a two-layer decoder-only Transformer with hidden dimension of 128 and 4 heads in its attention."
- **Code** (highest precedence first; likely effective: 128, 1):
  - 128 — code_default `dim` at [main.py:50](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L50): `def __init__(self, dim=128, num_layers=2, num_heads=4, num_tokens=97, seq_len=5):`
  - 128 — code_literal `dim` at [main.py:105](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L105): `model = Decoder(`
  - 1 — code_literal `dim` at [main.py:152](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L152): `dl = torch.split(data, args.batch_size, dim=1)`
- Scope: compared only with files matching "files not tied to another section"
- Note: 2 different values at the same precedence (code_default); one matches, and the tool cannot tell which one this experiment used

## Missing in code — stated in the paper, not found in the code (10)

### M1. `train_steps`

- **Paper**: `50k` → 50000 at `sections/B_implementation.tex:38`
  - Section: Appendix: Task Details > QM9
  - Context: "The network is initialized with weights x 3 larger than that of Kaiming initialization and trained for 50k iterations."
- Scope: compared only with files matching "QM9"
- Note: not set in the files this section points to

### M2. `warmup_steps`

- **Paper**: `10` → 10 at `sections/B_implementation.tex:13`
  - Section: Appendix: Task Details > Binary Operation (Algorithmic Data)
  - Context: "We use cross entropy loss to train the network and an Adam with betas (\beta_{1}, \beta_{2}) = (0.9, 0.98) , a constant learning rate of 10^{-3} , batch size of 512 , and linear learning rate warmup schedule over the first 10 iterations."
- Note: no setting with this name found in the code

### M3. `hidden_size`

- **Paper**: `256` → 256 at `sections/B_implementation.tex:44`
  - Section: Appendix: Task Details > IMDb
  - Context: "For IMDb dataset , we use LSTM with two layers, embedding dimension of 64, hidden dimension of 256, and vocabulary size of 1001, including the padding token."
- Scope: compared only with files matching "IMDb"
- Note: not set in the files this section points to

### M4. `num_layers`

- **Paper**: `2` → 2 at `sections/4_experiment.tex:57`
  - Section: Experiment > IMDb
  - Context: "Finally, we train a 2-layer LSTM network for sentiment analysis in the IMDb dataset under the grokking phenomenon ."
- Scope: compared only with files matching "IMDb"
- Note: not set in the files this section points to

### M5. `num_layers`

- **Paper**: `two` → 2 at `sections/B_implementation.tex:34`
  - Section: Appendix: Task Details > QM9
  - Context: "The output of the Graph ConvNet is a global average pooling, followed by a two-layer MLP with a ReLU and hidden channel of 32."
- Scope: compared only with files matching "QM9"
- Note: not set in the files this section points to

### M6. `num_layers`

- **Paper**: `two` → 2 at `sections/B_implementation.tex:44`
  - Section: Appendix: Task Details > IMDb
  - Context: "For IMDb dataset , we use LSTM with two layers, embedding dimension of 64, hidden dimension of 256, and vocabulary size of 1001, including the padding token."
- Scope: compared only with files matching "IMDb"
- Note: not set in the files this section points to

### M7. `train_fraction`

- **Paper**: `50:50` → 0.5 at `sections/B_implementation.tex:36`
  - Section: Appendix: Task Details > QM9
  - Context: "The data is again randomly split into train and validation sets with 50:50 size ratio."
- Note: no setting with this name found in the code

### M8. `train_fraction`

- **Paper**: `75:25` → 0.75 at `sections/B_implementation.tex:49`
  - Section: Appendix: Task Details > IMDb
  - Context: "We trained the model with the first 1000 rows from the dataset, split into train and validation sets with 75:25 size ratio."
- Note: no setting with this name found in the code

### M9. `num_train_samples`

- **Paper**: `100` → 100 at `sections/B_implementation.tex:35`
  - Section: Appendix: Task Details > QM9
  - Context: "To simulate the overfitting environment, we use the first 100 samples from the data."
- Scope: compared only with files matching "QM9"
- Note: not set in the files this section points to

### M10. `num_train_samples`

- **Paper**: `1000` → 1000 at `sections/B_implementation.tex:49`
  - Section: Appendix: Task Details > IMDb
  - Context: "We trained the model with the first 1000 rows from the dataset, split into train and validation sets with 75:25 size ratio."
- Scope: compared only with files matching "IMDb"
- Note: not set in the files this section points to

## Missing in paper — set in the code, never mentioned in the paper (1)

### M1. `seed`

- **Code** (highest precedence first; likely effective: 0):
  - 0 — argparse_default `--seed` at [main.py:244](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L244): `parser.add_argument("--seed", type=int, default=0)`
  - 0 — argparse_default `--seed` at [main_imdb.py:371](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_imdb.py#L371): `parser.add_argument("--seed", type=int, default=0)`
  - 0 — argparse_default `--seed` at [main_mnist.py:225](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_mnist.py#L225): `parser.add_argument("--seed", type=int, default=0)`
  - 0 — argparse_default `--seed` at [main_qm9.py:210](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_qm9.py#L210): `parser.add_argument("--seed", type=int, default=0)`
- Note: the code sets this but the paper never mentions it

## Matches (24)

| Setting | Paper | Paper location | Code | Code location |
|---|---|---|---|---|
| learning_rate | 10^{-3} | `sections/B_implementation.tex:13` | 0.001 (argparse_default) | [main.py:248](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L248) |
| learning_rate | 10^{-3} | `sections/B_implementation.tex:22` | 0.001 (argparse_default) | [main_mnist.py:233](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_mnist.py#L233) |
| learning_rate | 10^{-3} | `sections/B_implementation.tex:37` | 0.001 (argparse_default) | [main_qm9.py:212](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_qm9.py#L212) |
| learning_rate | 3 x 10^{-4} | `sections/B_implementation.tex:48` | 0.0003 (argparse_default) | [main_imdb.py:374](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_imdb.py#L374) |
| batch_size | 512 | `sections/B_implementation.tex:13` | 512 (argparse_default) | [main.py:247](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L247) |
| batch_size | 200 | `sections/B_implementation.tex:22` | 200 (argparse_default) | [main_mnist.py:229](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_mnist.py#L229) |
| batch_size | 32 | `sections/B_implementation.tex:37` | 32 (argparse_default) | [main_qm9.py:211](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_qm9.py#L211) |
| batch_size | 50 | `sections/B_implementation.tex:48` | 50 (argparse_default) | [main_imdb.py:373](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_imdb.py#L373) |
| train_steps | 10^{5} | `sections/B_implementation.tex:22` | 100000 (argparse_default) | [main_mnist.py:228](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_mnist.py#L228) |
| train_steps | 10k | `sections/B_implementation.tex:50` | 10000 (argparse_default) | [main_imdb.py:372](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_imdb.py#L372) |
| optimizer | Adam | `sections/B_implementation.tex:13` | Adam (argparse_default) | [main.py:252](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L252) |
| optimizer | AdamW | `sections/B_implementation.tex:22` | AdamW (argparse_default) | [main_mnist.py:231](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_mnist.py#L231) |
| optimizer | AdamW | `sections/B_implementation.tex:37` | AdamW (code_literal) | [main_qm9.py:80](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_qm9.py#L80) |
| optimizer | AdamW | `sections/B_implementation.tex:48` | AdamW (code_literal) | [main_imdb.py:211](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_imdb.py#L211) |
| adam_beta1 | 0.9 | `sections/B_implementation.tex:13` | 0.9 (argparse_default) | [main.py:249](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L249) |
| adam_beta2 | 0.98 | `sections/B_implementation.tex:13` | 0.98 (argparse_default) | [main.py:250](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L250) |
| hidden_size | 200 | `sections/B_implementation.tex:19` | 200 (argparse_default) | [main_mnist.py:237](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_mnist.py#L237) |
| num_layers | two | `sections/1_introduction.tex:5` | 2 (code_default) | [main.py:50](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L50) |
| num_layers | two | `sections/2_preliminary.tex:62` | 2 (code_default) | [main.py:50](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L50) |
| num_layers | three | `sections/4_experiment.tex:38` | 3 (argparse_default) | [main_mnist.py:236](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_mnist.py#L236) |
| num_layers | two | `sections/B_implementation.tex:10` | 2 (code_default) | [main.py:50](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L50) |
| num_layers | three | `sections/B_implementation.tex:19` | 3 (argparse_default) | [main_mnist.py:236](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_mnist.py#L236) |
| num_heads | 4 | `sections/B_implementation.tex:10` | 4 (code_default) | [main.py:50](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main.py#L50) |
| num_train_samples | 1000 | `sections/B_implementation.tex:23` | 1000 (argparse_default) | [main_mnist.py:227](https://github.com/ironjr/grokfast/blob/93b2248e351d4bb9e4dda8ac32a6999b8970404b/main_mnist.py#L227) |
