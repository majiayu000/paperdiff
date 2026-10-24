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
