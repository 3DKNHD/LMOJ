# LMOJ

[English](#english) · [Español](#español)

Local programming judge in the style of DMOJ.  
Juez de programación local al estilo DMOJ.

---

## English

LMOJ runs on your machine: problem statements, an in-browser editor, verdicts, submission history, and editorials.

Hidden tests are **not** shipped as copyable `.in` files. Each problem has its own `secret/gen.py`. The judge runs it with the official solution and caches tests outside the pack.

### Requirements

- Python 3.10+
- Git
- `g++` with C++17 (optional: Python 3 to submit as `py3`)

### Install

```bash
git clone https://github.com/3DKNHD/LMOJ.git
cd LMOJ
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
chmod +x lmoj
./lmoj gui
```

Open http://127.0.0.1:5050. The default port is **5050** (`config.json`).

### Commands

```
./lmoj gui
./lmoj status
./lmoj test aplusb
./lmoj test aplusb --sample
./lmoj test aplusb --lang py3
./lmoj sync
./lmoj new-problem my-problem   # pack author, not the contestant
```

Submitted code is stored in `workspace/`. Submissions and the test cache live in `data/` (not tracked by git).

### Problem pack

A starter pack is already in `problems/` and works offline. See `problems/PACK.md` for the format.

To pull another pack from GitHub:

1. That repository’s root **is** the pack (one folder per problem).
2. In the UI: **Sync**, paste `https://github.com/USER/REPO.git`.
3. Or run `./lmoj sync https://github.com/USER/REPO.git`.

The URL is saved in `config.json`. Later `./lmoj sync` runs `git pull`.

### Problem layout

```
problems/aplusb/
  meta.json          points, TL, ML, tags
  statement.md
  editorial.md       optional public tutorial
  samples/01.in
  samples/01.out
  secret/gen.py      generator for THIS problem
  secret/sol.cpp     official solution; builds hidden outputs
```

`generate()` yields `(name, input)` pairs. Do not reuse a generic generator across problems: each `gen.py` should target this statement’s edge cases. The judge never shows hidden input/output (samples only, like DMOJ).

---

## Español

LMOJ corre en tu máquina: enunciados, editor en el navegador, veredictos, historial de envíos y editoriales.

Los casos ocultos **no** se publican como `.in` copiables. Cada problema trae su propio `secret/gen.py`. El juez lo corre con la solución oficial y cachea los tests fuera del pack.

### Requisitos

- Python 3.10+
- Git
- `g++` con C++17 (opcional: Python 3 para enviar en `py3`)

### Instalación

```bash
git clone https://github.com/3DKNHD/LMOJ.git
cd LMOJ
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
chmod +x lmoj
./lmoj gui
```

Abre http://127.0.0.1:5050. El puerto por defecto es **5050** (`config.json`).

### Comandos

```
./lmoj gui
./lmoj status
./lmoj test aplusb
./lmoj test aplusb --sample
./lmoj test aplusb --lang py3
./lmoj sync
./lmoj new-problem mi-problema   # autor del pack, no el concursante
```

El código enviado queda en `workspace/`. Envíos y caché en `data/` (no van al git).

### Pack de problemas

El pack de ejemplo está en `problems/` y se puede usar sin red. El formato está en `problems/PACK.md`.

Para bajar otro pack desde GitHub:

1. La raíz de ese repositorio **es** el pack (una carpeta por problema).
2. En la web: **Sync**, pega `https://github.com/USUARIO/REPO.git`.
3. O: `./lmoj sync https://github.com/USUARIO/REPO.git`.

La URL queda en `config.json`. Los siguientes `./lmoj sync` hacen `git pull`.

### Estructura de un problema

```
problems/aplusb/
  meta.json          puntos, TL, ML, tags
  statement.md
  editorial.md       opcional, tutorial público
  samples/01.in
  samples/01.out
  secret/gen.py      generador de ESTE problema
  secret/sol.cpp     oficial: genera las salidas ocultas
```

`generate()` produce pares `(nombre, entrada)`. Nada de un generador genérico copiado de un problema a otro: cada `gen.py` ataca los bordes de **este** enunciado. El juez no muestra input/output de casos ocultos (sí de samples, como DMOJ).
