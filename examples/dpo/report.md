# paperdiff report: arXiv:2305.18290

- Paper: arXiv:2305.18290 (LaTeX source, main file `main.tex`)
- Title: Direct Preference Optimization:\ Your Language Model is Secretly a Reward Model
- Code: https://github.com/eric-mitchell/direct-preference-optimization @ `f8b8c0f49dc9`
- Generated: 2026-10-24T19:46:39Z by paperdiff 0.1.0

| Category | Count |
|---|---|
| conflict | 2 |
| ambiguous | 1 |
| missing_in_code | 0 |
| missing_in_paper | 1 |
| match | 3 |

> paperdiff reports differences between what a paper states and what its code configures. A difference can come from a typo, a later code change, a setting defined elsewhere, a reasonable implementation choice, or an extraction error by this tool. It is not a judgement about whether the paper is correct, and it is not an accusation of misconduct. Check each item by hand before citing it.

## Conflicts — the code sets a different value (2)

### C1. `learning_rate`

- **Paper**: `1e-6` → 1e-06 at `main.tex:583`
  - Section: Appendix: DPO Implementation Details and Hyperparameters
  - Context: "Unless noted otherwise, we use a \beta = 0.1, batch size of 64 and the RMSprop optimizer with a learning rate of 1e-6 by default."
- **Code** (highest precedence first; likely effective: 5e-07):
  - 5e-07 — config `lr` at [config/config.yaml:51](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/config/config.yaml#L51): `lr: 5e-7`

### C2. `epochs`

- **Paper**: `3` → 3 at `main.tex:591`
  - Section: Appendix: Further Details on the Experimental Set-Up > IMDb Sentiment Experiment and Baseline Details
  - Context: "The RLHF reward model is initialized from the gpt2-large model and trained for 3 epochs on the preference datasets, and we take the checkpoint with the highest validation set accuracy."
- **Code** (highest precedence first; likely effective: 1):
  - 1 — config `n_epochs` at [config/config.yaml:68](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/config/config.yaml#L68): `n_epochs: 1`

## Ambiguous — several values, or the paper value is overridden (1)

### A1. `batch_size`

- **Paper**: `64` → 64 at `main.tex:583`
  - Section: Appendix: DPO Implementation Details and Hyperparameters
  - Context: "Unless noted otherwise, we use a \beta = 0.1, batch size of 64 and the RMSprop optimizer with a learning rate of 1e-6 by default."
- **Code** (highest precedence first; likely effective: 64, 32):
  - 64 — command `batch_size` at [README.md:32](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/README.md#L32): `python -u train.py model=pythia69 datasets=[hh] loss=sft exp_name=anthropic_dpo_pythia69 gradient_accumulation_steps=2 batch_size=64 eval_batch_size=32 trainer=FSDPTrainer sample_during_eval=false`
  - 64 — command `batch_size` at [README.md:36](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/README.md#L36): `python -u train.py model=blank_model model.name_or_path=/PATH/TO/LLAMA/WEIGHTS model.block_name=LlamaDecoderLayer datasets=[hh,shp] loss=sft exp_name=anthropic_shp_sft_llama_7b gradient_accumulation_s`
  - 32 — command `batch_size` at [README.md:52](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/README.md#L52): `python -u train.py model=pythia69 datasets=[hh] loss=dpo loss.beta=0.1 model.archive=/path/to/checkpoint/from/sft/step-XXXX/policy.pt exp_name=anthropic_dpo_pythia69 gradient_accumulation_steps=2 batc`
  - 64 — command `batch_size` at [README.md:75](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/README.md#L75): `python -u train.py model=pythia28 datasets=[hh] loss=sft exp_name=anthropic_dpo_pythia28 gradient_accumulation_steps=2 batch_size=64 eval_batch_size=32 trainer=FSDPTrainer sample_during_eval=false mod`
  - 64 — command `batch_size` at [README.md:85](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/README.md#L85): `python -u train.py model=pythia28 datasets=[hh] loss=dpo loss.beta=0.1 exp_name=anthropic_dpo_pythia28 gradient_accumulation_steps=2 batch_size=64 eval_batch_size=32 trainer=FSDPTrainer sample_during_`
  - … 2 more in report.json
- Note: 2 different values at the same precedence (command); one matches, and the tool cannot tell which one this experiment used

## Missing in paper — set in the code, never mentioned in the paper (1)

### M1. `seed`

- **Code** (highest precedence first; likely effective: 0):
  - 0 — config `seed` at [config/config.yaml:2](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/config/config.yaml#L2): `seed: 0`
  - 0 — code_default `seed` at [preference_datasets.py:290](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/preference_datasets.py#L290): `seed:int = 0,`
  - 42 — code_literal `seed` at [preference_datasets.py:56](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/preference_datasets.py#L56): `dataset = dataset.shuffle(seed=42)`
- Note: the code sets this but the paper never mentions it

## Matches (3)

| Setting | Paper | Paper location | Code | Code location |
|---|---|---|---|---|
| epochs | 1 | `main.tex:591` | 1 (config) | [config/config.yaml:68](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/config/config.yaml#L68) |
| warmup_steps | 150 | `main.tex:583` | 150 (config) | [config/config.yaml:83](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/config/config.yaml#L83) |
| optimizer | RMSprop | `main.tex:583` | RMSprop (config) | [config/config.yaml:80](https://github.com/eric-mitchell/direct-preference-optimization/blob/f8b8c0f49dc92a430bae41585f9d467d3618fe2f/config/config.yaml#L80) |
