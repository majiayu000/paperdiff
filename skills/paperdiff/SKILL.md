---
name: paperdiff
description: Compare the experimental setup a paper states (hyperparameters, data split, seeds, training length) with what its public code configures, and optionally rerun one or two key numbers under an explicit budget. Use when someone wants to check a paper against its repository before reproducing it, reviewing it, or submitting it.
---

# paperdiff

paperdiff reports differences. It does not decide whether a paper is right, and its output is never an accusation of misconduct. Say so when you relay results.

## 1. Static check (always safe; never runs the target code)

```bash
uvx --from git+https://github.com/majiayu000/paperdiff paperdiff check <arXiv ID | paper.pdf | tex dir> <repo URL | path> -o paperdiff-out
```

- arXiv sources are fetched from export.arxiv.org, one request at a time, and cached. Do not loop over many papers.
- If the repo vendors a library (a copy of `transformers`, `third_party/`), rerun with `--exclude 'path/*'`.
- Read `paperdiff-out/report.md`. Conflicts are the strongest signal; check each one by opening both locations before repeating it to the user. "Ambiguous" and "missing" items need a person to decide.

## 2. Rerun (only with the user's explicit approval)

1. From the report and the paper, pick at most 1–3 numbers that can finish within the user's budget, preferring CPU-sized runs (small models, data subsets).
2. Write a spec (format: `docs/design.md` §7.2): `repo`, `command` as a list (no shell), `budget.timeout_s` (required), `budget.gpus`, `budget.tokens` (the agent token budget you were given, recorded for the audit trail), and `targets` with the paper value, its `file:line`, a regex that captures the metric, and a tolerance.
3. Show the user the spec, the command and the budget. Run only after they agree:

```bash
paperdiff rerun spec.yaml --allow-run -o paperdiff-out/rerun
```

4. Report `rerun.md` as measured. A single mismatching run is not evidence that a result is irreproducible.

Never run anything outside the user's machine or sandbox, never raise the budget yourself, and never post results about a named paper anywhere without the user's explicit instruction.
