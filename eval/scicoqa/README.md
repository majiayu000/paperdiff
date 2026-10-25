# Evaluation on SciCoQA (real split)

[SciCoQA](https://github.com/UKPLab/scicoqa) (Baumgärtner & Gurevych, ACL 2026, [arXiv:2601.12910](https://arxiv.org/abs/2601.12910))
collects 92 real paper–code discrepancies from GitHub issues and reproducibility papers. The data files are licensed
CC-BY 4.0, which allows this use with attribution. They are **not** committed here; `download.py` fetches
`data/scicoqa-real-v1.1.jsonl` from the UKPLab repository into `~/.cache/paperdiff/scicoqa/`.

These rules and `labels.json` were written and committed **before** paperdiff was run on any SciCoQA paper.

## Coverage labels (`labels.json`)

Each of the 92 items is labelled from its gold description alone:

- `keys` — the discrepancy is about the value of a setting paperdiff compares (`src/paperdiff/keys.py`), whatever
  the variable is called in the code. 3 items.
- `other_setting` — a configurable value that is not in keys.py (learning-rate schedule, number of runs, dataset
  name, dilation rates, …). 11 items.
- `method` — everything else: equations, loss terms, layer order, data handling logic. 78 items.

"Coverable subset" in the results means the `keys` items.

## Running paperdiff

For each item, paperdiff runs on the paper version SciCoQA pins (`paper_url_versioned`: arXiv LaTeX source via
export.arxiv.org when the paper is on arXiv, otherwise the PDF at that URL) and the repository at the pinned commit
(`code_url_versioned`). Items that share the same paper and commit share one run. Default options, no `--exclude`.

## Matching (fixed)

Let a *finding* be any paperdiff finding whose category is not `match`. A gold item is **detected** when some
finding from its run satisfies both:

1. **Location**: one of the finding's code candidates is in a file SciCoQA lists for the item
   (`relevant_code_files_gpt` ∪ `relevant_code_files_gemini` ∪ `changed_code_files.file_name`), compared by path
   suffix. Findings without code candidates (`missing_in_code`) qualify if the gold texts contain the finding's
   setting name in words (the key's paper-side phrase).
2. **Value**: the finding's paper value, or one of its code values, appears among the numbers in the item's gold
   texts (`origin_discrepancy_text`, `discrepancy_description_gpt`, `discrepancy_description_gemini`), compared
   with paperdiff's own number normalisation; for string values (optimizer names), a case-insensitive substring.

The coverage labels are not used for detection, only for splitting the results.

Two recall numbers:

- **strict**: only `conflict` findings count;
- **any**: `conflict`, `ambiguous`, `missing_in_code` and `missing_in_paper` count.

## Precision

SciCoQA lists the discrepancies someone reported, not all that exist, so a paperdiff conflict that matches no gold
item is not necessarily wrong. Two numbers:

- **precision vs gold** (lower bound): share of all `conflict` findings that match some gold item of their paper by
  the rule above;
- **audited precision**: a random sample of 30 `conflict` findings (Python `random.Random(20261025).sample`, over
  findings sorted by paper, then location), each judged by opening both cited locations: *real difference* (the
  paper and the code really state different values for the same setting of the same experiment) or *false* (wrong
  extraction or wrong pairing). Judged by the tool's author, which is a bias to keep in mind.

## Results and changes made during the evaluation

Results: [results.md](results.md). Earlier snapshots: [results-before-fetch-fix.md](results-before-fetch-fix.md),
[results-before-extraction-fixes.md](results-before-extraction-fixes.md).

The rules above did not change. paperdiff itself changed twice while the evaluation was running:

1. **Downloads** (no test information used for the fix itself, but found because the evaluation hit it): large arXiv
   source tarballs were cut short by the server and failed; arXiv answered HTTP 429 and paperdiff silently fell back
   to the PDF. Now 429/503 are waited out, truncated downloads resume with a Range request, and the PDF fallback is
   used only when the source is genuinely unavailable (403/404). Before: 53 completed runs, 6 from LaTeX source
   and 47 from PDF; after: 62 completed, 41 from LaTeX source. Strict recall stayed 0/92; "any" recall went from
   13/92 to 12/92 (all coincidental, see below); conflicts went from 85 to 87.
2. **Extraction** (informed by the audit sample, i.e. by test data): PDF text that flattens `10⁻⁵` to `10−5`
   (U+2212) is read as 1e-5, and a value followed by a comma-separated list of values is treated as a sweep.
   Conflicts went from 87 to 82; 3 of the 30 audited findings, all judged false, are no longer reported.
   Recall did not change.

The two misses on coverable items (`f2b47a1a`, `66841ab0`) were not fixed: each fix would be tailored to a single
test item.

All 12 items detected under the "any" rule were checked by hand: in each case the matching finding is about a
different setting that happens to share a number and a file with the gold description (for example a batch size of
14 for an item about a loss term). None describes the gold discrepancy.

## `--llm` mode (rules fixed before the first `--llm` run)

**Runs.** The same (paper version, commit) pairs as above, `paperdiff check --llm` defaults: provider Anthropic,
model `claude-sonnet-5-5`, at most 6 paper sections per paper, 40,000 characters per request, cap $1 per paper.
Runs that failed to fetch above still count as not detected. Before the full run, 3 papers (the first three pairs
in sorted order) are run to measure cost; the full run happens only if the extrapolated cost for all pairs is at
most $20.

**Candidates.** A kept `--llm` finding (one that passed the citation check) is a *candidate* for a gold item if
its code location is in one of the item's gold files (same suffix rule as above).

**Recall.** An item is *detected* when a person reading its gold description and a candidate judges that the
candidate describes the same discrepancy: the same code construct (function, loss term, layer, data step) and the
same direction of mismatch. Judgments are recorded in `llm-recall.json` with a one-line reason. Reported for all 92
items, the method-level subset (78), the coverable subset (3) and the other-setting subset (11). The share of items
with at least one candidate is reported as an automatic upper bound.

**Precision.** 30 kept `--llm` findings drawn with `random.Random(20261025).sample` from all kept findings sorted
by paper URL, then paper location, then code location. Each is judged by reading both cited locations: *real* (the
paper and the code really differ in the way the finding says) or *false* (they agree, or the finding misreads one
side, or the two sides are about different things). Recorded in `llm-audit.json`.

**Citation check.** The share of proposed findings dropped because a cited location does not exist or the quote is
not found there, over all runs.

Judgments are made by the tool's author.
