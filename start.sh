#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -x .venv/bin/python ]]; then
  echo "Primero instala las dependencias:"
  echo "  ./install.sh"
  echo "Si falló, mira README.md → Si el script falla."
  exit 1
fi

exec .venv/bin/python gui/app.py
