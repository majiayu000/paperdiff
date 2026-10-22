# Rerun: Grokfast MNIST on CPU

Paper: Grokfast (arXiv:2405.20233), MNIST experiment. The paper says that with α = 0.8, λ = 0.1 and weight decay 2.0
"the delay until grokking is reduced by ×22.0" and the final evaluation accuracy rises "from 89.8% to 91.2%"
(`sections/4_experiment.tex:40-41`). The repo's README command for this experiment (`README.md:207`) passes
`--alpha 0.8 --lamb 0.1 --weight_decay 2.0` but no `--filter`, whose default is `none` (`main_mnist.py:241`), so it
trains without the Grokfast gradient filter.

Two runs, same machine (Apple Silicon, CPU only, `gpus: 0`), seed 0 (the script default), 100,000 steps each,
budget 1500 s each, run with `paperdiff rerun ... --allow-run`:

| Spec | Command difference | Final val. acc. | Paper | Verdict (±1.0 pt) | Wall time |
|---|---|---|---|---|---|
| [paper-setting.yaml](paper-setting.yaml) → [result](paper-setting/rerun.md) | `--filter ema` added | 91.0% | 91.2% | reproduced | 789 s |
| [readme-command.yaml](readme-command.yaml) → [result](readme-command/rerun.md) | README command verbatim | 90.7% | 91.2% | reproduced | 691 s |

Before running, `paperdiff rerun paper-setting.yaml` without `--allow-run` refused and exited with code 2.

## What the logs add (manual analysis, not a paperdiff feature)

The final accuracy cannot tell the two runs apart, and the paper's main claim is about speed, which it gives only
as a ratio. From the progress lines in each `rerun.log`, the first logged step at which validation accuracy reached
a threshold (the script evaluates every 667 steps after step 150, so these are upper bounds):

| Threshold | With `--filter ema` | README command (no filter) |
|---|---|---|
| 80% | 1,334 | 1,334 |
| 85% | 2,001 | 2,001 |
| 90% | 14,007 | 12,006 |

In this one CPU run, the README command, which only sets weight decay 2.0, reaches the same accuracies as fast
as the run with the filter. That is one seed on different hardware, so it does not show that the paper's ×22 is
wrong. Its baseline for the ×22 comparison is presumably the default weight decay 0.01, which we did not run. It
does show that the README command does not exercise the method it is listed under, which is what
[ironjr/grokfast#16](https://github.com/ironjr/grokfast/issues/16) asks about.

`rerun.log` files are not committed (about 600 KB each of progress-bar output); `rerun.json` holds the last 50
lines.
