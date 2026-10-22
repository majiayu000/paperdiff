"""Shared fixtures: a tiny LaTeX paper and a tiny repository that disagree in known ways."""

from pathlib import Path

import pytest

PAPER_MAIN = r"""\documentclass{article}
\title{Toyformer: A Small Test Paper}
\begin{document}
\maketitle
\section{Introduction}
Prior work used SGD at scale. % we tried Adam once
\input{sections/setup}
\begin{figure}
We plot curves smoothed with momentum 0.95.
\end{figure}
\end{document}
Text after the end is ignored, learning rate of 9.
"""

PAPER_SETUP = r"""\section{Experiments}
\subsection{MNIST}
We use AdamW with a learning rate of $3 \times 10^{-4}$, batch size of $128$, and train for 20 epochs.
We use $(\beta_1, \beta_2) = (0.9, 0.98)$ and a random seed of 42.
The data is split into train and validation sets with 90:10 ratio.

\subsection{CIFAR}
We use a learning rate of \texttt{1e-3} and a batch size of 256.
We warm up the learning rate over the first 500 steps.

\begin{tabular}{ll|cc}
\toprule
Method & Setting & MNIST & CIFAR \\
\midrule
\multirow{2}{*}{\makecell{Toy \\ base}} & Batch Size & 128 & 64 \\
 & \# Epochs & \multicolumn{2}{c}{20} \\
 & Warmup Ratio & 0.1 & 0.1 \\
\bottomrule
\end{tabular}
"""

TRAIN_MNIST = """import argparse
import torch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr", type=float, default=3e-4)
    parser.add_argument("--batch_size", type=int, default=128)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    steps = 0
    opt = torch.optim.AdamW([], lr=args.lr, betas=(0.9, 0.98))
"""

TRAIN_CIFAR = """from absl import flags
flags.DEFINE_float("learning_rate", 1e-3, "lr")
flags.DEFINE_integer("batch_size", 256, "bs")
WARMUP_STEPS = 100
"""

CONFIG = """train:
  lr: 0.001
  batch_size: 256
"""

README = """# Toyformer

```bash
python train_cifar.py --batch_size=512 \\
    --learning_rate 1e-3
```
"""

RUN_SH = """LR=5e-4
python train_mnist.py --lr $LR --seed 7
"""


@pytest.fixture
def paper_dir(tmp_path: Path) -> Path:
    d = tmp_path / "paper"
    (d / "sections").mkdir(parents=True)
    (d / "main.tex").write_text(PAPER_MAIN)
    (d / "sections" / "setup.tex").write_text(PAPER_SETUP)
    (d / "unused.tex").write_text(r"\section{Old} learning rate of 7.")
    return d


@pytest.fixture
def repo_dir(tmp_path: Path) -> Path:
    d = tmp_path / "repo"
    (d / "configs").mkdir(parents=True)
    (d / "train_mnist.py").write_text(TRAIN_MNIST)
    (d / "train_cifar.py").write_text(TRAIN_CIFAR)
    (d / "configs" / "cifar.yaml").write_text(CONFIG)
    (d / "README.md").write_text(README)
    (d / "run_mnist.sh").write_text(RUN_SH)
    return d
