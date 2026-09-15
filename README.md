# LMOJ

[English](#english) · [Español](#español)

Local programming judge in the style of DMOJ.  
Juez de programación local al estilo DMOJ.

---

## Español

LMOJ corre en tu máquina: enunciados, editor en el navegador, veredictos, historial y editoriales.

### Encender

Linux / macOS:

```bash
git clone https://github.com/3DKNHD/LMOJ.git
cd LMOJ
bash install.sh
./start.sh
```

Windows: clona el repo (GitHub → Code → Download ZIP, o Git), entra a la carpeta y:

```bat
install.bat
start.bat
```

Abre **http://127.0.0.1:5050**. Para salir, Ctrl+C en la terminal.

Problemas nuevos: en la web, **Sync**.

### Si el script falla

Hace falta **Python 3.10+**. Para enviar en C++ también **g++**. **Git** sirve para clonar y para Sync.

#### Python

- **Debian / Ubuntu:** `sudo apt update && sudo apt install python3 python3-venv python3-pip`
- **Fedora:** `sudo dnf install python3`
- **Arch:** `sudo pacman -S python`
- **macOS:** [python.org/downloads](https://www.python.org/downloads/) o `brew install python`
- **Windows:** [python.org/downloads](https://www.python.org/downloads/) — marca **Add python.exe to PATH**. O: `winget install Python.Python.3.12`

Comprueba: `python3 --version` (Windows: `py -3 --version`). Tiene que ser 3.10 o más.

Si `install.sh` se queja de `venv`: en Debian/Ubuntu instala `python3-venv` (arriba).

#### Git

- **Debian / Ubuntu:** `sudo apt install git`
- **Fedora:** `sudo dnf install git`
- **Arch:** `sudo pacman -S git`
- **macOS:** `xcode-select --install` o `brew install git`
- **Windows:** [git-scm.com](https://git-scm.com/download/win) o `winget install Git.Git`

#### g++ (solo si vas a enviar C++)

- **Debian / Ubuntu:** `sudo apt install g++`
- **Fedora:** `sudo dnf install gcc-c++`
- **Arch:** `sudo pacman -S gcc`
- **macOS:** `xcode-select --install` (el `g++` de Apple vale para C++17)
- **Windows:** [MSYS2](https://www.msys2.org/), luego en su terminal: `pacman -S mingw-w64-ucrt-x86_64-gcc`. Suma `C:\msys64\ucrt64\bin` al PATH. O: `winget install MSYS2.MSYS2`.

Sin g++ igual puedes enviar en **Python 3** desde la web.

#### Instalar LMOJ a mano

Linux / macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
./start.sh
```

Windows:

```bat
py -3 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
start.bat
```

---

## English

LMOJ runs on your machine: statements, an in-browser editor, verdicts, history, and editorials.

### Start

Linux / macOS:

```bash
git clone https://github.com/3DKNHD/LMOJ.git
cd LMOJ
bash install.sh
./start.sh
```

Windows: clone the repo, open that folder, then:

```bat
install.bat
start.bat
```

Open **http://127.0.0.1:5050**. Stop with Ctrl+C in the terminal.

New problems: **Sync** in the UI.

### If the script fails

You need **Python 3.10+**. For C++ submissions, **g++**. **Git** is used to clone and to Sync.

#### Python

- **Debian / Ubuntu:** `sudo apt update && sudo apt install python3 python3-venv python3-pip`
- **Fedora:** `sudo dnf install python3`
- **Arch:** `sudo pacman -S python`
- **macOS:** [python.org/downloads](https://www.python.org/downloads/) or `brew install python`
- **Windows:** [python.org/downloads](https://www.python.org/downloads/) — tick **Add python.exe to PATH**. Or: `winget install Python.Python.3.12`

Check: `python3 --version` (Windows: `py -3 --version`). Must be 3.10+.

If `install.sh` complains about `venv`, install `python3-venv` on Debian/Ubuntu.

#### Git

- **Debian / Ubuntu:** `sudo apt install git`
- **Fedora:** `sudo dnf install git`
- **Arch:** `sudo pacman -S git`
- **macOS:** `xcode-select --install` or `brew install git`
- **Windows:** [git-scm.com](https://git-scm.com/download/win) or `winget install Git.Git`

#### g++ (only if you submit C++)

- **Debian / Ubuntu:** `sudo apt install g++`
- **Fedora:** `sudo dnf install gcc-c++`
- **Arch:** `sudo pacman -S gcc`
- **macOS:** `xcode-select --install` (Apple’s `g++` is fine for C++17)
- **Windows:** [MSYS2](https://www.msys2.org/), then `pacman -S mingw-w64-ucrt-x86_64-gcc`. Add `C:\msys64\ucrt64\bin` to PATH. Or: `winget install MSYS2.MSYS2`.

Without g++ you can still submit **Python 3** in the UI.

#### Install LMOJ by hand

Linux / macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
./start.sh
```

Windows:

```bat
py -3 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
start.bat
```
