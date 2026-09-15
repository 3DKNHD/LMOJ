# LMOJ — juez local (estilo DMOJ)

Juez en tu PC: enunciado, Submit, veredictos, historial de envíos.
Los casos ocultos **no** viven como `.in` copiables. Cada problema trae su
propio `secret/gen.py`; el juez lo corre junto con la solución oficial y
cachea los tests fuera del pack.

## Arranque

```bash
cd ~/Documentos/Codes/Hobby/LMOJ
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
chmod +x lmoj
./lmoj gui          # http://127.0.0.1:5050
```

C++17: `g++ -std=c++17 -O2 -Wall -Wextra -Wshadow`. También Python 3.

## Pack desde GitHub

Cuando actualices problemas en un repo:

1. La raíz del repo es el pack (una carpeta por problema). Ver `problems/PACK.md`.
2. En la web: **Sync**, pega `https://github.com/USUARIO/REPO.git`.
3. O: `./lmoj sync https://github.com/USUARIO/REPO.git`

La URL queda en `config.json`. Los siguientes `./lmoj sync` hacen `git pull`.

El pack de ejemplo ya está en `problems/` (4 problemas) para usar el juez sin red.

## Comandos

```
./lmoj gui
./lmoj status
./lmoj test aplusb
./lmoj test aplusb --sample
./lmoj test aplusb --lang py3
./lmoj sync
./lmoj new-problem mi-problema   # para AUTOR, no para el concursante
```

Tu código se guarda en `workspace/`. Envíos y caché de tests en `data/` (local).

## Cómo está un problema

```
problems/aplusb/
  meta.json          puntos, TL, ML
  statement.md
  samples/01.in      solo ejemplos públicos
  samples/01.out
  secret/gen.py      generador único de ESTE problema
  secret/sol.cpp     oficial: produce las salidas ocultas
```

`generate()` produce pares `(nombre, entrada)`. Nada de un generador genérico
pasado de un problema a otro: cada `gen.py` ataca los bordes de su enunciado.
El juez no muestra input/output de casos ocultos (sí de samples, como DMOJ).

## Puerto

Si el gym ICPC ya usa el 5000, LMOJ escucha en **5050** (`config.json`).
