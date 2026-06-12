#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if [ -f .venv/bin/activate ]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

python3 generate_notebooks.py 2>/dev/null || true

echo "Starting MyST (http://localhost:3000) ..."
myst start &
MYST_PID=$!
trap 'kill "$MYST_PID" 2>/dev/null' INT TERM

echo "Waiting for content build..."
until [ -d _build/site/content ] && compgen -G "_build/site/content/*.json" > /dev/null; do
  sleep 1
done

echo "Applying LTR fix to inline math (refresh browser after first patch)..."
while kill -0 "$MYST_PID" 2>/dev/null; do
  python3 fix_math_rtl.py >/dev/null 2>&1 || true
  sleep 3
done
