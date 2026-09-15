#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

have() { command -v "$1" >/dev/null 2>&1; }

pick_python() {
  local c
  for c in python3 python; do
    if have "$c" && "$c" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)' 2>/dev/null; then
      printf '%s\n' "$c"
      return 0
    fi
  done
  return 1
}

PY="$(pick_python)" || {
  echo "Falta Python 3.10 o más nuevo."
  echo "Cómo instalarlo: README.md → Si el script falla."
  exit 1
}

if ! "$PY" -c 'import venv' 2>/dev/null; then
  echo "Falta el módulo venv de Python."
  echo "Debian/Ubuntu: sudo apt install python3-venv"
  echo "Otras distros y Windows: README.md → Si el script falla."
  exit 1
fi

echo "Python: $PY ($("$PY" -c 'import sys; print(sys.version.split()[0])'))"
"$PY" -m venv .venv
.venv/bin/python -m pip install -U pip
.venv/bin/python -m pip install -r requirements.txt
chmod +x lmoj start.sh install.sh 2>/dev/null || true

if ! have git; then
  echo "Aviso: no hay git. El botón Sync de la web lo necesita. Ver README.md."
fi
if ! have g++; then
  echo "Aviso: no hay g++. Puedes enviar en Python 3; para C++ instala un compilador. Ver README.md."
fi

echo
echo "Listo. Arranca la GUI con:"
echo "  ./start.sh"
echo "Luego abre http://127.0.0.1:5050"
