#!/usr/bin/env bash
# Regenerate the example reports. Fetches each paper once from export.arxiv.org (cached afterwards).
set -euo pipefail
cd "$(dirname "$0")/.."
uv run paperdiff check 2405.20233 https://github.com/ironjr/grokfast -o examples/grokfast
uv run paperdiff check 2305.18290 https://github.com/eric-mitchell/direct-preference-optimization -o examples/dpo
uv run paperdiff check 1810.04805 https://github.com/google-research/bert -o examples/bert
# examples/NLU vendors a full copy of Hugging Face transformers; only the repo's own scripts are of interest.
uv run paperdiff check 2106.09685 https://github.com/microsoft/LoRA -o examples/lora \
  --exclude 'examples/NLU/src/*' --exclude 'examples/NLU/examples/*'
