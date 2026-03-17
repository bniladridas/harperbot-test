#!/usr/bin/env bash
set -euo pipefail

python3 -c "import sample_inline; print(sample_inline.slow_demo())"

