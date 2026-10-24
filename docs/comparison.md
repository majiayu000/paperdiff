# paperdiff compared with related tools

Checked 2026-10-23. Stars, last push and license come from the GitHub API on that date. Feature cells come from
each project's README or paper; "—" means the question does not apply to that kind of project.

## At a glance

| | paperdiff | [SciCoQA](https://github.com/UKPLab/scicoqa) | [claimcheck](https://github.com/asech109/claimcheck) | [Paper2Code](https://github.com/going-doer/Paper2Code) | [paper2code skill](https://github.com/PrathamLearnsToCode/paper2code) | [PaperBench](https://github.com/openai/frontier-evals) | [CORE-Bench](https://github.com/siegelz/core-bench) | [42 checker](https://github.com/midnightoatmeal/42-ML_reproducibility_checker) | [paper-workshop](https://github.com/tjhavranek/paper-workshop) | [paperswithcode.co](https://paperswithcode.co/) |
|---|---|---|---|---|---|---|---|---|---|---|
| What it is | CLI: paper vs its own code | Dataset + LLM eval code | CLI for authors | Multi-agent code generator | Agent skill, code generator | Agent benchmark | Agent benchmark | Streamlit app | Claude Code skill (review + rewrite) | Website (papers, trends) |
| Stars / last push | new | 7 / 2026-09-30 | 0 / 2026-05-14 | 4,997 / 2026-03-25 | 1,537 / 2026-04-03 | 1,321 (repo) / 2026-10-12 | 80 / 2025-11-23 | 0 / 2025-11-15 | 11 / 2026-08-09 | — |
| License | MIT | Apache-2.0 | MIT | Apache-2.0 | MIT | MIT | MIT | MIT | not stated | — |
| Direction | paper ↔ existing code | paper ↔ existing code | own paper ↔ own code | paper → new code | paper → new code | paper → new code (scored) | run existing code | paper ↔ existing code | paper → review, rerun | discovery |
| Input: arXiv ID | ✅ | ✗ (dataset PDFs) | ✗ (local .tex) | ✅ PDF/LaTeX | ✅ | — | — | ✅ PDF link | ✅ | ✅ |
| Reads LaTeX source | ✅ preferred | ✗ | ✅ | ✅ optional | partial | — | — | ✗ | partial | ✗ |
| PDF fallback | ✅ | ✅ | ✗ | ✅ | ✅ | — | — | ✅ | ✅ | — |
| Hyperparameter tables (row groups, spans) | ✅ | via LLM | ✗ | via LLM | via LLM | — | — | ✗ | via LLM | ✗ |
| Code: argparse / absl defaults | ✅ | via LLM | ✗ | — | — | — | — | ✗ | via LLM | ✗ |
| Code: YAML / hydra configs | ✅ | via LLM | ✅ | — | — | — | — | ✗ | via LLM | ✗ |
| Code: README / shell launch commands | ✅ | via LLM | ✗ | — | — | — | — | ✗ | ✗ | ✗ |
| Per-experiment scoping (section → script) | ✅ | ✗ | ✗ | — | — | — | — | ✗ | ✗ | ✗ |
| `file:line` on both sides | ✅ + permalinks | free text | ✅ | — | § citations in code | — | — | ✗ | quote-grounded | ✗ |
| Difference categories | conflict / ambiguous / missing ×2 / match | taxonomy (paper) | match / mismatch / unverifiable | — | — | — | — | inconsistency flags | review comments | — |
| Runs code | opt-in, time/GPU cap | ✗ | ✗ (by design) | ✗ | ✗ | ✅ agent | ✅ agent | ✗ | ✅ | ✗ |
| Needs an LLM / API key | no | yes | no | yes (OpenAI or vLLM) | yes (host agent) | yes | yes | no | yes (host agent) | — |
| Machine-readable output | JSON + Markdown | JSONL | Markdown + exit code | repo | repo | scores | scores | UI | documents | — |
| Published accuracy figure | SciCoQA real split: recall 0/92 (78 of 92 items are method-level, out of scope); audited precision 20/30 | best of 22 LLMs finds 46.7% of real discrepancies | none | — | — | best agent 21.0% replication score | — | "50+ dataset links, 25+ mismatches" (self-reported) | none | — |

Sources for the numbers: SciCoQA [arXiv:2601.12910](https://arxiv.org/abs/2601.12910); PaperBench
[arXiv:2504.01848](https://arxiv.org/abs/2504.01848) (20 ICML 2024 papers, 8,316 graded items, Claude 3.5 Sonnet (New)
21.0%); 42 checker README. The PaperBench stars are for the `openai/frontier-evals` repository, which hosts several
benchmarks.

## Where paperdiff is weaker

- **Method-level differences** (a loss term, the order of two layers) are out of scope; SciCoQA and LLM-based
  reviewers can at least attempt them. In docs/research.md about half of the real reviewer complaints are of this kind.
- **Only listed settings** ([keys.py](../src/paperdiff/keys.py)) are compared; anything else is silently out of scope.
- **Recall on SciCoQA's real split is 0/92.** 78 of its 92 discrepancies are method-level and 11 are settings
  outside keys.py; of the 3 that are about a compared setting, one paper could not be fetched and two were missed
  (a weight decay the paper never mentions, set through a variable; layer widths written as "400 neurons" against a
  list-valued `expert_units`). SciCoQA's best LLM finds 46.7% of the real discrepancies, so on this benchmark an
  LLM-based reader is far ahead. Details: [eval/scicoqa/results.md](../eval/scicoqa/results.md).
- **No web UI**, unlike the 42 checker and paperswithcode.co.

## Where it is stronger

- When it reports a conflict, it is usually a real difference: 20 of 30 randomly sampled conflicts on the SciCoQA
  papers were real (20 of 27 after two extraction fixes), with `file:line` on both sides to check.

- Deterministic, no API key, runs in seconds, same answer every time.
- Each claim is compared with the script its experiment uses, not the whole repository.
- Reruns are off by default and, when enabled, bounded by a hard time limit and a GPU count.
