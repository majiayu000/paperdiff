import pytest

from paperdiff.values import clean_latex, equal, find_numbers, fmt, parse_scalar


@pytest.mark.parametrize(
    "text, expected",
    [
        (r"$10^{-3}\,$", [0.001]),
        (r"$3 \times 10^{-4}$", [0.0003]),
        (r"\texttt{1e-6}", [1e-6]),
        ("5.00E-04", [0.0005]),
        ("1,000,000 steps", [1_000_000]),
        ("50k iterations", [50_000]),
        ("1M", [1_000_000]),
        (r"10\%", [0.1]),
        ("(0.9, 0.98)", [0.9, 0.98]),
        ("{8c564b}", []),  # a colour code, not a number
        ("V100 GPUs", []),
    ],
)
def test_find_numbers(text, expected):
    assert [n.value for n in find_numbers(clean_latex(text))] == pytest.approx(expected)


def test_word_numbers_only_when_asked():
    assert find_numbers("a two-layer MLP") == []
    assert [n.value for n in find_numbers("a two-layer MLP", words=True)] == [2]


@pytest.mark.parametrize(
    "raw, expected",
    [(3e-4, 3e-4), ("5e-7", 5e-7), ("20_000", 20000.0), ("RMSprop", "RMSprop"), ("null", None), ("true", True)],
)
def test_parse_scalar(raw, expected):
    assert parse_scalar(raw) == expected


def test_equal_and_fmt():
    assert equal(0.0003, 3e-4)
    assert equal("torch.optim.AdamW", "adamw")
    assert not equal("Adam", "AdamW")
    assert not equal(1.0, "1")
    assert fmt(128.0) == "128" and fmt(3e-4) == "0.0003"
