First release.

- `paperdiff check <arXiv ID | PDF | LaTeX> <repo>`: compares hyperparameters, data split, seeds and training length stated in a paper with the code's argparse/absl defaults, YAML/hydra configs and README/shell commands. Every finding has the paper `file:line` and a permalink to the code line; categories are conflict, ambiguous, missing in code, missing in paper, match.
- Claims are matched to the script their experiment uses (section titles, table row groups and columns).
- `--fail-on conflict` for pre-submission CI; `--exclude` for vendored code.
- `paperdiff rerun spec.yaml --allow-run`: runs one command on your machine under a hard time limit and GPU count and compares the numbers it prints with the paper. Off by default.
- Example reports for Grokfast, DPO, BERT and LoRA, and a CPU rerun of Grokfast's MNIST experiment.
- Measured on SciCoQA's 92 real paper–code discrepancies: 0/92 found. 78 of them are method-level (equations, loss terms, layer order), which this release does not try to detect; only 3 are about a setting it compares. When it reports a conflict, 20 of 30 audited ones were real differences. Details: [README → Accuracy on SciCoQA](https://github.com/majiayu000/paperdiff#accuracy-on-scicoqa).

paperdiff reports differences; it does not judge whether a paper is correct and draws no conclusions about authors.
