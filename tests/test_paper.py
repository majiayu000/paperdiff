from paperdiff.paper import extract, load_latex, load_paper

from fixtures import paper_dir  # noqa: F401  (pytest fixtures)


def _claims(paper_dir):
    return load_paper("latex", paper_dir, "toy").claims


def by_key(claims, key):
    return [c for c in claims if c.key == key]


def test_follows_inputs_and_keeps_source_lines(paper_dir):
    lines, main = load_latex(paper_dir)
    assert main == "main.tex"
    files = {ln.file for ln in lines}
    assert "sections/setup.tex" in files and "unused.tex" not in files
    lr = [c for c in _claims(paper_dir) if c.key == "learning_rate" and c.origin == "text"]
    assert [(c.value, c.loc) for c in lr] == [(0.0003, "sections/setup.tex:3"), (0.001, "sections/setup.tex:8")]


def test_title_comments_figures_and_end_document(paper_dir):
    paper = load_paper("latex", paper_dir, "toy")
    assert paper.title == "Toyformer: A Small Test Paper"
    values = {(c.key, c.value) for c in paper.claims}
    assert ("optimizer", "Adam") not in values  # inside a % comment
    assert ("momentum", 0.95) not in values  # inside a figure
    assert ("learning_rate", 9.0) not in values  # after \end{document}
    assert ("optimizer", "SGD") not in values  # prior work, not this paper's setup


def test_sentence_claims(paper_dir):
    claims = _claims(paper_dir)
    text = [c for c in claims if c.origin == "text"]
    got = {(c.key, c.value) for c in text}
    assert {("batch_size", 128.0), ("epochs", 20.0), ("optimizer", "AdamW"), ("seed", 42.0),
            ("adam_beta1", 0.9), ("adam_beta2", 0.98), ("batch_size", 256.0), ("warmup_steps", 500.0),
            ("train_fraction", 0.9)} <= got
    mnist_bs = next(c for c in text if c.key == "batch_size" and c.value == 128.0)
    assert mnist_bs.section == "Experiments > MNIST"


def test_table_rows_with_groups_and_spans(paper_dir):
    table = [c for c in _claims(paper_dir) if c.origin == "table"]
    got = {(c.key, c.value, c.column) for c in table}
    assert ("batch_size", 128.0, "Toy base / MNIST") in got
    assert ("batch_size", 64.0, "Toy base / CIFAR") in got
    assert ("epochs", 20.0, "Toy base / CIFAR") in got  # \multicolumn{2} spreads over both columns
    assert not any(c.key == "warmup_steps" for c in table)  # "Warmup Ratio" is a different unit


def test_lr_not_taken_from_unrelated_numbers():
    from paperdiff.paper import Line

    lines = [Line("x.tex", 1, r"The learning rate is decayed by a factor of 10 every 30 epochs."),
             Line("x.tex", 2, ""),
             Line("x.tex", 3, r"We linearly warm up the learning rate from 0 to 1e-6 over 150 steps.")]
    claims = extract(lines)
    assert not any(c.key == "learning_rate" for c in claims)
    assert [(c.key, c.value) for c in claims if c.key == "warmup_steps"] == [("warmup_steps", 150.0)]


def test_comparisons_and_equation_numbers_are_not_settings():
    from paperdiff.paper import Line

    lines = [Line("x.tex", 1, r"We compare LoRA with $r = 8$ and $r = 64$ on the same task."),
             Line("x.tex", 2, ""),
             Line("x.pdf", 3, "LR(r, D) = -E log s(r(x, yw) - r(x, yl)) (2) where s is the logistic function.")]
    claims = extract(lines)
    ranks = [c for c in claims if c.key == "lora_rank"]
    assert [c.value for c in ranks] == [8.0, 64.0] and all(c.values == [8.0, 64.0] for c in ranks)
    assert not any(c.key == "learning_rate" for c in claims)


def test_two_settings_in_one_cell():
    from paperdiff.paper import Line

    rows = [r"\begin{tabular}{ll|cc}", r"Method & Setting & MNLI & SST-2 \\",
            r"\multirow{2}{*}{LoRA} & Batch Size & 16 & 16 \\",
            r" & LoRA Config. & \multicolumn{2}{c}{$r_q=r_v=8$} \\",
            r" & Other & lr=1e-4, bs=32 & 0 \\", r"\end{tabular}"]
    claims = extract([Line("t.tex", i + 1, t) for i, t in enumerate(rows)])
    got = {(c.key, c.value, c.column, c.loc) for c in claims if c.key in ("lora_rank", "learning_rate")}
    assert ("lora_rank", 8.0, "LoRA / MNLI", "t.tex:4") in got and ("lora_rank", 8.0, "LoRA / SST-2", "t.tex:4") in got
    assert ("learning_rate", 0.0001, "LoRA / MNLI", "t.tex:5") in got
    assert ("batch_size", 32.0) in {(c.key, c.value) for c in claims if c.loc == "t.tex:5"}


def test_sweeps_and_flattened_pdf_exponents():
    from paperdiff.paper import Line

    lines = [Line("x.tex", 1, "We test the following values of the learning rate: 0.0001, 0.00025, 0.0005, 0.001."),
             Line("x.tex", 2, ""),
             Line("x.pdf", 3, "We use Adam with learning rate = .001 and weight decay = 10−5.", page=1)]
    claims = extract(lines)
    lr = next(c for c in claims if c.key == "learning_rate" and c.line == 1)
    assert lr.values == [0.0001, 0.00025, 0.0005, 0.001]
    assert [c.value for c in claims if c.key == "weight_decay"] == [1e-05]
