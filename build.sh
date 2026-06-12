#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

rm -rf _build
myst build --execute --html
python3 fix_math_rtl.py
