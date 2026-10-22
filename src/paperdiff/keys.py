"""Canonical settings and how papers and code name them.

Only settings listed here are compared. Anything else is ignored on purpose:
a missed setting is better than a wrong pairing.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Callable


@dataclass(frozen=True)
class Key:
    name: str
    kind: str  # "float" | "int" | "str"
    phrase: str  # regex over cleaned paper text
    number_before: bool = False  # "3 epochs" rather than "epochs of 3"
    code_names: tuple[str, ...] = ()
    # code name -> transform from the code value to this key's unit
    code_transforms: dict[str, Callable[[float], float]] = field(default_factory=dict)
    core: bool = False  # report when code sets it but the paper never mentions it
    context: str | None = None  # regex that must also occur in the same sentence


def _one_minus(v: float) -> float:
    return 1.0 - v


KEYS: list[Key] = [
    Key("learning_rate", "float", r"learning[- ]rates?|\blr\b(?!\s*\()",
        code_names=("lr", "learning_rate", "base_lr", "init_lr", "max_lr", "peak_lr", "lr_max"), core=True),
    Key("batch_size", "int", r"(?:mini-?)?batch[- ]?sizes?",
        code_names=("batch_size", "bs", "train_batch_size", "per_device_train_batch_size", "train_bs",
                    "global_batch_size", "total_batch_size", "batchsize"), core=True),
    Key("epochs", "int", r"(?:training )?epochs?", number_before=True,
        code_names=("epochs", "num_epochs", "n_epochs", "num_train_epochs", "max_epochs", "nepochs"), core=True),
    Key("train_steps", "int", r"(?:training |optimization |gradient |update )?(?:steps|iterations|updates)",
        number_before=True,
        code_names=("steps", "num_steps", "max_steps", "train_steps", "num_train_steps", "total_steps",
                    "optimization_steps", "num_iterations", "max_iter", "max_iters", "n_steps",
                    "training_steps", "iters", "n_iters", "num_iters", "iterations"), core=True,
        context=r"(?i)train|until|for|stop"),
    Key("warmup_steps", "int", r"warm[- ]?up",
        code_names=("warmup_steps", "num_warmup_steps", "warmup", "warmup_iters", "lr_warmup_steps",
                    "warmup_updates", "num_warmup")),
    Key("weight_decay", "float", r"weight[- ]decay|\bL2 (?:regularization|penalty)",
        code_names=("weight_decay", "wd", "l2", "l2_reg", "weight_decay_rate")),
    Key("dropout", "float", r"dropout(?: rate| probability| ratio)?",
        code_names=("dropout", "dropout_rate", "dropout_prob", "hidden_dropout_prob", "drop_rate",
                    "p_dropout", "dropout_p")),
    Key("seed", "int", r"(?:random )?seeds?(?= *(?:=|of|is|:|\())",
        code_names=("seed", "random_seed", "rng_seed", "manual_seed"), core=True),
    Key("optimizer", "str", r"\b(?:AdamW|Adam|SGD|RMSprop|RMSProp|Adafactor|LAMB|Adagrad|Lion|Muon)\b",
        code_names=("optimizer", "optim", "optimizer_type", "optimizer_name", "opt"), core=True,
        # A statement about this work's training, not a mention of optimizers in general.
        context=r"(?i)\b(?:we|our)\b[^.]*\b(?:use|train|optimi[sz]e|adopt|employ)|trained (?:with|using|by)"
                r"|optimi[sz]ed (?:with|using|by)"),
    Key("momentum", "float", r"momentum", code_names=("momentum",)),
    Key("adam_beta1", "float", r"\\beta_?\{?1\}?", code_names=("beta1", "adam_beta1", "b1")),
    Key("adam_beta2", "float", r"\\beta_?\{?2\}?", code_names=("beta2", "adam_beta2", "b2")),
    Key("adam_epsilon", "float", r"Adam(?:W)?[^.]{0,40}?\\(?:epsilon|varepsilon)",
        code_names=("adam_epsilon", "adam_eps", "eps")),
    Key("grad_clip", "float",
        r"gradient (?:norm )?clipping|clip(?:ped|ping)? (?:the )?gradients?(?: norm)?|max(?:imum)? gradient norm",
        code_names=("max_grad_norm", "grad_clip", "clip_grad_norm", "gradient_clip_val", "clip_norm",
                    "grad_norm_clip", "clip_grad")),
    Key("label_smoothing", "float", r"label smoothing",
        code_names=("label_smoothing", "label_smoothing_factor", "smoothing")),
    Key("max_seq_length", "int", r"(?:max(?:imum)? )?(?:sequence|context|input) length|max(?:imum)? length",
        code_names=("max_seq_length", "max_length", "seq_len", "max_seq_len", "block_size",
                    "context_length", "max_len")),
    Key("hidden_size", "int", r"hidden (?:size|dimension|dim|width)s?|model dimension",
        code_names=("hidden_size", "hidden_dim", "d_model", "n_embd", "hidden_width", "width", "dim")),
    Key("num_layers", "int", r"layers?\b", number_before=True,
        code_names=("num_layers", "n_layers", "n_layer", "num_hidden_layers", "depth"),
        context=r"(?i)transformer|mlp|network|lstm|encoder|decoder|model"),
    Key("num_heads", "int", r"(?:attention )?heads\b", number_before=True,
        code_names=("num_heads", "n_heads", "n_head", "num_attention_heads", "heads")),
    Key("num_gpus", "int", r"GPUs\b", number_before=True,
        code_names=("num_gpus", "n_gpus", "gpus", "ngpu", "nproc_per_node")),
    Key("lora_rank", "int", r"\brank\s*r\b|\br\s*=(?=\s*\d)",
        code_names=("lora_r", "lora_rank", "lora_dim")),
    Key("lora_alpha", "float", r"LoRA[^.]{0,20}?\\alpha|\\alpha_\{?r\}?",
        code_names=("lora_alpha",)),
    # Fraction of the labelled data used for training ("75:25 split" -> 0.75).
    Key("train_fraction", "float", r"(?:train(?:ing)?|validation|test)[^.]{0,60}?split|split[^.]{0,60}?ratio",
        code_names=("train_ratio", "train_frac", "train_fraction", "train_split",
                    "test_size", "val_ratio", "val_split", "valid_ratio", "test_ratio", "val_fraction",
                    "validation_split"),
        code_transforms={n: _one_minus for n in ("test_size", "val_ratio", "val_split", "valid_ratio",
                                                 "test_ratio", "val_fraction", "validation_split")}),
    Key("num_train_samples", "int",
        r"(?:training )?(?:samples|examples|images|rows|points|data points)\b", number_before=True,
        code_names=("train_points", "n_train", "num_train", "num_train_samples", "max_train_samples",
                    "train_samples", "n_train_samples"),
        context=r"(?i)subset|first|only|randomly (?:select|sample)"),
]

KEYS_BY_NAME = {k.name: k for k in KEYS}
_CODE_NAME_INDEX: dict[str, Key] = {}
for _k in KEYS:
    for _n in _k.code_names:
        _CODE_NAME_INDEX[_n] = _k


def key_for_code_name(name: str) -> Key | None:
    """Map a code identifier (argparse dest, YAML path, kwarg) to a canonical key."""
    leaf = name.strip("-").rsplit(".", 1)[-1].replace("-", "_").lower()
    return _CODE_NAME_INDEX.get(leaf)


PHRASES = [(k, re.compile(k.phrase, re.I if k.name not in ("optimizer",) else 0)) for k in KEYS]
