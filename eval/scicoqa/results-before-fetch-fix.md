# SciCoQA real split: results

- Runs: 74 (paper version, commit) pairs, 53 completed (6 from LaTeX source, 47 from PDF), 21 failed to fetch or parse.
- Items: 92; items whose run failed count as not detected.

## Recall

| Subset | Items | Detected (strict: conflict) | Detected (any non-match finding) |
|---|---|---|---|
| All items | 92 | 0/92 (0.0%) | 13/92 (14.1%) |
| Coverable (`keys`) | 3 | 0/3 (0.0%) | 0/3 (0.0%) |
| Other setting values | 11 | 0/11 (0.0%) | 3/11 (27.3%) |
| Method-level | 78 | 0/78 (0.0%) | 10/78 (12.8%) |

By SciCoQA category:

| Category | Items | Strict | Any |
|---|---|---|---|
| Algorithm | 22 | 0 | 5 |
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

Items detected by any rule: `9a6bc557`, `c9a26055`, `0b8b9b43`, `96d7973b`, `a17a3073`, `47339aed`, `c5dec3b3`, `7e9f9955`, `dfccf929`, `a950db48`, `3bdc7c6f`, `84acd23b`, `417ffbee`

## Precision

- Conflict findings over all completed runs: 85
- Precision vs gold (lower bound, gold is incomplete): 0/85 (0.0%)
- Audited precision (random sample, seed 20261025): 0/0 judged (0 of 0 not yet judged)

