from paperdiff.code import extract_repo

from fixtures import repo_dir  # noqa: F401  (pytest fixtures)


def _find(settings, key, file):
    return sorted((s.value, s.source, s.line) for s in settings if s.key == key and s.file == file)


def test_argparse_flags_and_calls(repo_dir):
    s = extract_repo(repo_dir)
    assert _find(s, "learning_rate", "train_mnist.py") == [(0.0003, "argparse_default", 6)]
    assert _find(s, "optimizer", "train_mnist.py") == [("AdamW", "code_literal", 12)]
    assert _find(s, "adam_beta2", "train_mnist.py") == [(0.98, "code_literal", 12)]
    assert _find(s, "learning_rate", "train_cifar.py") == [(0.001, "flag_default", 2)]
    # module-level constants count, counters inside functions do not
    assert _find(s, "warmup_steps", "train_cifar.py") == [(100.0, "code_literal", 4)]
    assert _find(s, "train_steps", "train_mnist.py") == []


def test_yaml_with_line_numbers(repo_dir):
    s = extract_repo(repo_dir)
    assert _find(s, "learning_rate", "configs/cifar.yaml") == [(0.001, "config", 2)]
    assert next(x for x in s if x.file == "configs/cifar.yaml" and x.key == "batch_size").name == "train.batch_size"


def test_readme_and_shell_commands(repo_dir):
    s = extract_repo(repo_dir)
    readme = [x for x in s if x.file == "README.md"]
    assert {(x.key, x.value, x.line) for x in readme} == {("batch_size", 512.0, 4), ("learning_rate", 0.001, 4)}
    assert all(x.target == "train_cifar.py" for x in readme)
    sh = {(x.key, x.value) for x in s if x.file == "run_mnist.sh"}
    assert sh == {("learning_rate", 0.0005), ("seed", 7.0)}  # $LR resolved from the script


def test_excludes(repo_dir):
    s = extract_repo(repo_dir, excludes=["configs/*"])
    assert not any(x.file.startswith("configs/") for x in s)
