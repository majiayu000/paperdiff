# paperdiff report: arXiv:1810.04805

- Paper: arXiv:1810.04805 (LaTeX source, main file `main.tex`)
- Title: BERT: Pre-training of Deep Bidirectional Transformers for \ Language Understanding
- Code: https://github.com/google-research/bert @ `eedf5716ce12`
- Generated: 2026-10-22T08:14:57Z by paperdiff 0.1.0

| Category | Count |
|---|---|
| conflict | 7 |
| ambiguous | 13 |
| missing_in_code | 5 |
| missing_in_paper | 1 |
| match | 6 |

> paperdiff reports differences between what a paper states and what its code configures. A difference can come from a typo, a later code change, a setting defined elsewhere, a reasonable implementation choice, or an extraction error by this tool. It is not a judgement about whether the paper is correct, and it is not an accusation of misconduct. Check each item by hand before citing it.

## Conflicts — the code sets a different value (7)

### C1. `learning_rate`

- **Paper**: `1e-4` → 0.0001 at `bert_details.tex:55`
  - Section: Appendix: Additional Details for BERT > Pre-training Procedure
  - Context: "We use Adam with learning rate of 1e-4, {\beta}_1=0.9, {\beta}_2=0.999, L2 weight decay of 0.01, learning rate warmup over the first 10,000 steps, and linear decay of the learning rate."
- **Code** (highest precedence first; likely effective: 2e-05):
  - 2e-05 — command `--learning_rate` at [README.md:929](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L929): `python run_pretraining.py \`
  - 5e-05 — flag_default `learning_rate` at [run_pretraining.py:68](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_pretraining.py#L68): `flags.DEFINE_float("learning_rate", 5e-5, "The initial learning rate for Adam.")`
- Scope: compared only with files matching "Pre-training Procedure"

### C2. `batch_size`

- **Paper**: `256` → 256 at `bert_details.tex:55`
  - Section: Appendix: Additional Details for BERT > Pre-training Procedure
  - Context: "We train with batch size of 256 sequences (256 sequences * 512 tokens = 128,000 tokens/batch) for 1,000,000 steps, which is approximately 40 epochs over the 3.3 billion word corpus."
- **Code** (highest precedence first; likely effective: 32):
  - 32 — command `--train_batch_size` at [README.md:929](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L929): `python run_pretraining.py \`
  - 32 — flag_default `train_batch_size` at [run_pretraining.py:64](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_pretraining.py#L64): `flags.DEFINE_integer("train_batch_size", 32, "Total batch size for training.")`
- Scope: compared only with files matching "Pre-training Procedure"

### C3. `train_steps`

- **Paper**: `1,000,000` → 1000000 at `bert_details.tex:55`
  - Section: Appendix: Additional Details for BERT > Pre-training Procedure
  - Context: "We train with batch size of 256 sequences (256 sequences * 512 tokens = 128,000 tokens/batch) for 1,000,000 steps, which is approximately 40 epochs over the 3.3 billion word corpus."
- **Code** (highest precedence first; likely effective: 20):
  - 20 — command `--num_train_steps` at [README.md:929](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L929): `python run_pretraining.py \`
  - 100000 — flag_default `num_train_steps` at [run_pretraining.py:70](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_pretraining.py#L70): `flags.DEFINE_integer("num_train_steps", 100000, "Number of training steps.")`
- Scope: compared only with files matching "Pre-training Procedure"

### C4. `train_steps`

- **Paper**: `1M` → 1000000 at `bert_details.tex:89`
  - Section: Appendix: Additional Details for BERT > Comparison of BERT, ELMo ,and OpenAI GPT
  - Context: "\item GPT was trained for 1M steps with a batch size of 32,000 words;"
- **Code** (highest precedence first; likely effective: 20):
  - 20 — command `--num_train_steps` at [README.md:929](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L929): `python run_pretraining.py \`
  - 100000 — flag_default `num_train_steps` at [run_pretraining.py:70](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_pretraining.py#L70): `flags.DEFINE_integer("num_train_steps", 100000, "Number of training steps.")`

### C5. `train_steps`

- **Paper**: `1,000,000` → 1000000 at `more_ablation.tex:14`
  - Section: Appendix: Additional Ablation Studies > Effect of Number of Training Steps
  - Context: "Does BERT really need such a large amount of pre-training (128,000 words/batch * 1,000,000 steps) to achieve high fine-tuning accuracy? \\ Answer:"
- **Code** (highest precedence first; likely effective: 20):
  - 20 — command `--num_train_steps` at [README.md:929](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L929): `python run_pretraining.py \`
  - 100000 — flag_default `num_train_steps` at [run_pretraining.py:70](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_pretraining.py#L70): `flags.DEFINE_integer("num_train_steps", 100000, "Number of training steps.")`

### C6. `train_steps`

- **Paper**: `1M` → 1000000 at `more_ablation.tex:15`
  - Section: Appendix: Additional Ablation Studies > Effect of Number of Training Steps
  - Context: "Yes, \bertbase achieves almost 1.0\% additional accuracy on MNLI when trained on 1M steps compared to 500k steps."
- **Code** (highest precedence first; likely effective: 20):
  - 20 — command `--num_train_steps` at [README.md:929](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L929): `python run_pretraining.py \`
  - 100000 — flag_default `num_train_steps` at [run_pretraining.py:70](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_pretraining.py#L70): `flags.DEFINE_integer("num_train_steps", 100000, "Number of training steps.")`

### C7. `train_steps`

- **Paper**: `500k` → 500000 at `more_ablation.tex:15`
  - Section: Appendix: Additional Ablation Studies > Effect of Number of Training Steps
  - Context: "Yes, \bertbase achieves almost 1.0\% additional accuracy on MNLI when trained on 1M steps compared to 500k steps."
- **Code** (highest precedence first; likely effective: 20):
  - 20 — command `--num_train_steps` at [README.md:929](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L929): `python run_pretraining.py \`
  - 100000 — flag_default `num_train_steps` at [run_pretraining.py:70](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_pretraining.py#L70): `flags.DEFINE_integer("num_train_steps", 100000, "Number of training steps.")`

## Ambiguous — several values, or the paper value is overridden (13)

### A1. `learning_rate`

- **Paper**: `5e-5` → 5e-05 at `bert_details.tex:90`
  - Section: Appendix: Additional Details for BERT > Comparison of BERT, ELMo ,and OpenAI GPT
  - Context: "\item GPT used the same learning rate of 5e-5 for all fine-tuning experiments;"
- **Code** (highest precedence first; likely effective: 2e-05):
  - 2e-05 — command `--learning_rate` at [README.md:440](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L440): `python run_classifier.py \`
  - 5e-05 — flag_default `learning_rate` at [run_classifier.py:84](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_classifier.py#L84): `flags.DEFINE_float("learning_rate", 5e-5, "The initial learning rate for Adam.")`
  - 0.2 — code_literal `learning_rate` at [optimization_test.py:36](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/optimization_test.py#L36): `optimizer = optimization.AdamWeightDecayOptimizer(learning_rate=0.2)`
- Scope: compared only with files matching "files not tied to another section"
- Note: paper value appears only as a flag_default (run_classifier.py:84), which a command (precedence 4) likely overrides

### A2. `learning_rate`

- **Paper**: `5e-5` → 5e-05 at `experiment.tex:19`
  - Section: Experiments > GLUE
  - Context: "For each task, we selected the best fine-tuning learning rate (among 5e-5, 4e-5, 3e-5, and 2e-5) on the Dev set."
- **Code** (highest precedence first; likely effective: 2e-05):
  - 2e-05 — command `--learning_rate` at [README.md:440](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L440): `python run_classifier.py \`
  - 5e-05 — flag_default `learning_rate` at [run_classifier.py:84](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_classifier.py#L84): `flags.DEFINE_float("learning_rate", 5e-5, "The initial learning rate for Adam.")`
  - 0.2 — code_literal `learning_rate` at [optimization_test.py:36](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/optimization_test.py#L36): `optimizer = optimization.AdamWeightDecayOptimizer(learning_rate=0.2)`
- Scope: compared only with files matching "files not tied to another section"
- Note: paper value appears only as a flag_default (run_classifier.py:84), which a command (precedence 4) likely overrides

### A3. `learning_rate`

- **Paper**: `5e-5` → 5e-05 at `experiment.tex:43`
  - Section: Experiments > SQuAD v1.1
  - Context: "We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32."
- **Code** (highest precedence first; likely effective: 3e-05):
  - 3e-05 — command `--learning_rate` at [README.md:527](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L527): `python run_squad.py \`
  - 3e-05 — command `--learning_rate` at [README.md:564](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L564): `python run_squad.py \`
  - 3e-05 — command `--learning_rate` at [README.md:610](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L610): `python run_squad.py \`
  - 3e-05 — command `--learning_rate` at [README.md:646](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L646): `python run_squad.py \`
  - 5e-05 — flag_default `learning_rate` at [run_squad.py:91](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_squad.py#L91): `flags.DEFINE_float("learning_rate", 5e-5, "The initial learning rate for Adam.")`
- Scope: compared only with files matching "SQuAD v1.1"
- Note: paper value appears only as a flag_default (run_squad.py:91), which a command (precedence 4) likely overrides

### A4. `learning_rate`

- **Paper**: `5e-5` → 5e-05 at `experiment.tex:57`
  - Section: Experiments > SQuAD v2.0
  - Context: "We fine-tuned for 2 epochs with a learning rate of 5e-5 and a batch size of 48."
- **Code** (highest precedence first; likely effective: 3e-05):
  - 3e-05 — command `--learning_rate` at [README.md:527](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L527): `python run_squad.py \`
  - 3e-05 — command `--learning_rate` at [README.md:564](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L564): `python run_squad.py \`
  - 3e-05 — command `--learning_rate` at [README.md:610](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L610): `python run_squad.py \`
  - 3e-05 — command `--learning_rate` at [README.md:646](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L646): `python run_squad.py \`
  - 5e-05 — flag_default `learning_rate` at [run_squad.py:91](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_squad.py#L91): `flags.DEFINE_float("learning_rate", 5e-5, "The initial learning rate for Adam.")`
- Scope: compared only with files matching "SQuAD v2.0"
- Note: paper value appears only as a flag_default (run_squad.py:91), which a command (precedence 4) likely overrides

### A5. `batch_size`

- **Paper**: `16` → 16 at `bert_details.tex:66`
  - Section: Appendix: Additional Details for BERT > Fine-tuning Procedure
  - Context: "\begin{itemize}[noitemsep] \item {\bf Batch size}: 16, 32 \item {\bf Learning rate (Adam)}: 5e-5, 3e-5, 2e-5 \item {\bf Number of epochs}: 2, 3, 4 \end{itemize}"
- **Code** (highest precedence first; likely effective: 32, 8):
  - 32 — command `--train_batch_size` at [README.md:440](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L440): `python run_classifier.py \`
  - 8 — command `--batch_size` at [README.md:749](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L749): `python extract_features.py \`
  - 32 — flag_default `batch_size` at [extract_features.py:63](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/extract_features.py#L63): `flags.DEFINE_integer("batch_size", 32, "Batch size for predictions.")`
  - 32 — flag_default `train_batch_size` at [run_classifier.py:78](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_classifier.py#L78): `flags.DEFINE_integer("train_batch_size", 32, "Total batch size for training.")`
  - 13 — code_default `batch_size` at [modeling_test.py:35](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling_test.py#L35): `batch_size=13,`
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 2 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A6. `batch_size`

- **Paper**: `32` → 32 at `experiment.tex:19`
  - Section: Experiments > GLUE
  - Context: "We use a batch size of 32 and fine-tune for 3 epochs over the data for all GLUE tasks."
- **Code** (highest precedence first; likely effective: 32, 8):
  - 32 — command `--train_batch_size` at [README.md:440](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L440): `python run_classifier.py \`
  - 8 — command `--batch_size` at [README.md:749](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L749): `python extract_features.py \`
  - 32 — flag_default `batch_size` at [extract_features.py:63](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/extract_features.py#L63): `flags.DEFINE_integer("batch_size", 32, "Batch size for predictions.")`
  - 32 — flag_default `train_batch_size` at [run_classifier.py:78](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_classifier.py#L78): `flags.DEFINE_integer("train_batch_size", 32, "Total batch size for training.")`
  - 13 — code_default `batch_size` at [modeling_test.py:35](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling_test.py#L35): `batch_size=13,`
- Scope: compared only with files matching "files not tied to another section"
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

### A7. `batch_size`

- **Paper**: `32` → 32 at `experiment.tex:43`
  - Section: Experiments > SQuAD v1.1
  - Context: "We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32."
- **Code** (highest precedence first; likely effective: 12, 24):
  - 12 — command `--train_batch_size` at [README.md:527](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L527): `python run_squad.py \`
  - 24 — command `--train_batch_size` at [README.md:564](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L564): `python run_squad.py \`
  - 24 — command `--train_batch_size` at [README.md:610](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L610): `python run_squad.py \`
  - 24 — command `--train_batch_size` at [README.md:646](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L646): `python run_squad.py \`
  - 32 — flag_default `train_batch_size` at [run_squad.py:86](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_squad.py#L86): `flags.DEFINE_integer("train_batch_size", 32, "Total batch size for training.")`
- Scope: compared only with files matching "SQuAD v1.1"
- Note: paper value appears only as a flag_default (run_squad.py:86), which a command (precedence 4) likely overrides

### A8. `batch_size`

- **Paper**: `48` → 48 at `experiment.tex:57`
  - Section: Experiments > SQuAD v2.0
  - Context: "We fine-tuned for 2 epochs with a learning rate of 5e-5 and a batch size of 48."
- **Code** (highest precedence first; likely effective: 12, 24):
  - 12 — command `--train_batch_size` at [README.md:527](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L527): `python run_squad.py \`
  - 24 — command `--train_batch_size` at [README.md:564](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L564): `python run_squad.py \`
  - 24 — command `--train_batch_size` at [README.md:610](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L610): `python run_squad.py \`
  - 24 — command `--train_batch_size` at [README.md:646](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L646): `python run_squad.py \`
  - 32 — flag_default `train_batch_size` at [run_squad.py:86](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_squad.py#L86): `flags.DEFINE_integer("train_batch_size", 32, "Total batch size for training.")`
- Scope: compared only with files matching "SQuAD v2.0"
- Note: the code sets 2 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A9. `batch_size`

- **Paper**: `16` → 16 at `experiment.tex:69`
  - Section: Experiments > SWAG
  - Context: "We fine-tune the model for 3 epochs with a learning rate of 2e-5 and a batch size of 16."
- **Code** (highest precedence first; likely effective: 32, 8):
  - 32 — command `--train_batch_size` at [README.md:440](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L440): `python run_classifier.py \`
  - 8 — command `--batch_size` at [README.md:749](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L749): `python extract_features.py \`
  - 32 — flag_default `batch_size` at [extract_features.py:63](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/extract_features.py#L63): `flags.DEFINE_integer("batch_size", 32, "Batch size for predictions.")`
  - 32 — flag_default `train_batch_size` at [run_classifier.py:78](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_classifier.py#L78): `flags.DEFINE_integer("train_batch_size", 32, "Total batch size for training.")`
  - 13 — code_default `batch_size` at [modeling_test.py:35](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling_test.py#L35): `batch_size=13,`
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 2 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A10. `epochs`

- **Paper**: `3` → 3 at `experiment.tex:43`
  - Section: Experiments > SQuAD v1.1
  - Context: "We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32."
- **Code** (highest precedence first; likely effective: 2):
  - 2 — command `--num_train_epochs` at [README.md:527](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L527): `python run_squad.py \`
  - 2 — command `--num_train_epochs` at [README.md:564](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L564): `python run_squad.py \`
  - 2 — command `--num_train_epochs` at [README.md:610](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L610): `python run_squad.py \`
  - 2 — command `--num_train_epochs` at [README.md:646](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L646): `python run_squad.py \`
  - 3 — flag_default `num_train_epochs` at [run_squad.py:93](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_squad.py#L93): `flags.DEFINE_float("num_train_epochs", 3.0,`
- Scope: compared only with files matching "SQuAD v1.1"
- Note: paper value appears only as a flag_default (run_squad.py:93), which a command (precedence 4) likely overrides

### A11. `warmup_steps`

- **Paper**: `10,000` → 10000 at `bert_details.tex:55`
  - Section: Appendix: Additional Details for BERT > Pre-training Procedure
  - Context: "We use Adam with learning rate of 1e-4, {\beta}_1=0.9, {\beta}_2=0.999, L2 weight decay of 0.01, learning rate warmup over the first 10,000 steps, and linear decay of the learning rate."
- **Code** (highest precedence first; likely effective: 10):
  - 10 — command `--num_warmup_steps` at [README.md:929](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L929): `python run_pretraining.py \`
  - 10000 — flag_default `num_warmup_steps` at [run_pretraining.py:72](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/run_pretraining.py#L72): `flags.DEFINE_integer("num_warmup_steps", 10000, "Number of warmup steps.")`
- Scope: compared only with files matching "Pre-training Procedure"
- Note: paper value appears only as a flag_default (run_pretraining.py:72), which a command (precedence 4) likely overrides

### A12. `num_layers`

- **Paper**: `four` → 4 at `ablation.tex:33`
  - Section: Ablation Studies > Effect of Model Size
  - Context: "However, we believe that this is the first work to demonstrate convincingly that scaling to extreme model sizes also leads to large improvements on very small scale tasks, provided that the model has been sufficiently pre-trained. presented mixed results on the downstream task impact of increasin..."
- **Code** (highest precedence first; likely effective: 12, 5):
  - 12 — code_default `num_hidden_layers` at [modeling.py:757](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling.py#L757): `num_hidden_layers=12,`
  - 12 — code_default `num_hidden_layers` at [modeling.py:37](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling.py#L37): `num_hidden_layers=12,`
  - 5 — code_default `num_hidden_layers` at [modeling_test.py:42](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling_test.py#L42): `num_hidden_layers=5,`
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 2 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

### A13. `num_layers`

- **Paper**: `two` → 2 at `ablation.tex:51`
  - Section: Ablation Studies > Feature-based Approach with BERT
  - Context: "These contextual embeddings are used as input to a randomly initialized two-layer 768-dimensional BiLSTM before the classification layer."
- **Code** (highest precedence first; likely effective: 12, 5):
  - 12 — code_default `num_hidden_layers` at [modeling.py:757](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling.py#L757): `num_hidden_layers=12,`
  - 12 — code_default `num_hidden_layers` at [modeling.py:37](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling.py#L37): `num_hidden_layers=12,`
  - 5 — code_default `num_hidden_layers` at [modeling_test.py:42](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling_test.py#L42): `num_hidden_layers=5,`
- Scope: compared only with files matching "files not tied to another section"
- Note: the code sets 2 different values at the same precedence and none equals the paper; the tool cannot tell which one this experiment used

## Missing in code — stated in the paper, not found in the code (5)

### M1. `epochs`

- **Paper**: `40` → 40 at `bert_details.tex:55`
  - Section: Appendix: Additional Details for BERT > Pre-training Procedure
  - Context: "We train with batch size of 256 sequences (256 sequences * 512 tokens = 128,000 tokens/batch) for 1,000,000 steps, which is approximately 40 epochs over the 3.3 billion word corpus."
- Scope: compared only with files matching "Pre-training Procedure"
- Note: not set in the files this section points to

### M2. `weight_decay`

- **Paper**: `0.01` → 0.01 at `bert_details.tex:55`
  - Section: Appendix: Additional Details for BERT > Pre-training Procedure
  - Context: "We use Adam with learning rate of 1e-4, {\beta}_1=0.9, {\beta}_2=0.999, L2 weight decay of 0.01, learning rate warmup over the first 10,000 steps, and linear decay of the learning rate."
- Scope: compared only with files matching "Pre-training Procedure"
- Note: not set in the files this section points to

### M3. `dropout`

- **Paper**: `0.1` → 0.1 at `bert_details.tex:55`
  - Section: Appendix: Additional Details for BERT > Pre-training Procedure
  - Context: "We use a dropout probability of 0.1 on all layers."
- Scope: compared only with files matching "Pre-training Procedure"
- Note: not set in the files this section points to

### M4. `optimizer`

- **Paper**: `Adam` → Adam at `bert_details.tex:55`
  - Section: Appendix: Additional Details for BERT > Pre-training Procedure
  - Context: "We use Adam with learning rate of 1e-4, {\beta}_1=0.9, {\beta}_2=0.999, L2 weight decay of 0.01, learning rate warmup over the first 10,000 steps, and linear decay of the learning rate."
- Scope: compared only with files matching "Pre-training Procedure"
- Note: not set in the files this section points to

### M5. `num_train_samples`

- **Paper**: `3,600` → 3600 at `ablation.tex:29`
  - Section: Ablation Studies > Effect of Model Size
  - Context: "We can see that larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled training examples, and is substantially different from the pre-training tasks."
- Note: no setting with this name found in the code

## Missing in paper — set in the code, never mentioned in the paper (1)

### M1. `seed`

- **Code** (highest precedence first; likely effective: 12345):
  - 12345 — command `--random_seed` at [README.md:908](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L908): `python create_pretraining_data.py \`
  - 12345 — flag_default `random_seed` at [create_pretraining_data.py:54](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/create_pretraining_data.py#L54): `flags.DEFINE_integer("random_seed", 12345, "Random seed for data generation.")`
- Note: the code sets this but the paper never mentions it

## Matches (6)

| Setting | Paper | Paper location | Code | Code location |
|---|---|---|---|---|
| learning_rate | 2e-5 | `experiment.tex:69` | 2e-05 (command) | [README.md:440](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L440) |
| epochs | 3 | `experiment.tex:19` | 3 (command) | [README.md:440](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L440) |
| epochs | 2 | `experiment.tex:57` | 2 (command) | [README.md:527](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L527) |
| epochs | 3 | `experiment.tex:69` | 3 (command) | [README.md:440](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L440) |
| dropout | 0.1 | `bert_details.tex:63` | 0.1 (code_default) | [modeling.py:437](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/modeling.py#L437) |
| max_seq_length | 128 | `bert_details.tex:59` | 128 (command) | [README.md:908](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/README.md#L908) |
