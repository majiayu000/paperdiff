from paperdiff.align import align, classify
from paperdiff.code import Setting, extract_repo
from paperdiff.paper import Claim, load_paper

from fixtures import paper_dir, repo_dir  # noqa: F401  (pytest fixtures)


def claim(key, value, section="Experiments", values=None):
    return Claim(key, value, str(value), "p.tex:1", "p.tex", 1, section, "", "text", values=values or [value])


def setting(key, value, source, file="train.py", line=1):
    return Setting(key, key, value, source, file, line, "")


def test_categories():
    code = [setting("learning_rate", 0.001, "argparse_default"), setting("learning_rate", 0.0005, "command"),
            setting("batch_size", 64.0, "config")]
    assert classify(claim("batch_size", 64.0), code).category == "match"
    assert classify(claim("batch_size", 32.0), code).category == "conflict"
    overridden = classify(claim("learning_rate", 0.001), code)
    assert overridden.category == "ambiguous" and "overrides" in overridden.note
    assert classify(claim("learning_rate", 0.0005), code).category == "match"
    assert classify(claim("batch_size", 64.0, values=[32.0, 64.0]), code).category == "ambiguous"
    assert classify(claim("dropout", 0.1), code).category == "missing_in_code"


def test_same_precedence_disagreement_is_ambiguous():
    code = [setting("seed", 0.0, "argparse_default", "a.py"), setting("seed", 1.0, "argparse_default", "b.py")]
    assert classify(claim("seed", 0.0), code).category == "ambiguous"


def test_end_to_end_scoping(paper_dir, repo_dir):
    paper = load_paper("latex", paper_dir, "toy")
    findings = align(paper, extract_repo(repo_dir))

    def find(key, loc):
        return next(f for f in findings if f.claim and f.key == key and f.claim.loc == loc)

    # MNIST section is compared with the MNIST files only
    lr = find("learning_rate", "sections/setup.tex:3")
    assert lr.scope == "MNIST"
    assert {c.file for c in lr.candidates} == {"run_mnist.sh", "train_mnist.py"}
    assert lr.category == "ambiguous"  # 3e-4 is the argparse default, but run_mnist.sh passes 5e-4
    assert find("epochs", "sections/setup.tex:3").category == "conflict"  # 20 vs default 10
    # CIFAR batch size: README command (512) overrides the flag and YAML (256)
    bs = find("batch_size", "sections/setup.tex:8")
    assert bs.category == "ambiguous" and bs.effective == [512.0]
    # seed 42 in the paper; MNIST code uses 7 (command) / 0 (default)
    assert find("seed", "sections/setup.tex:4").category == "conflict"
