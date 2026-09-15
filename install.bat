@echo off
setlocal EnableExtensions
cd /d "%~dp0"

set "PY="
where py >nul 2>&1
if %errorlevel%==0 (
  py -3 -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
  if not errorlevel 1 set "PY=py -3"
)

if not defined PY (
  where python >nul 2>&1
  if %errorlevel%==0 (
    python -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
    if not errorlevel 1 set "PY=python"
  )
)

if not defined PY (
  echo Falta Python 3.10 o mas nuevo.
  echo Como instalarlo: README.md - Si el script falla.
  exit /b 1
)

echo Usando %PY%
%PY% -m venv .venv
if errorlevel 1 (
  echo No se pudo crear .venv. En algunos Windows hace falta marcar "Add python.exe to PATH" al instalar Python.
  echo Ver README.md - Si el script falla.
  exit /b 1
)

.venv\Scripts\python.exe -m pip install -U pip
if errorlevel 1 exit /b 1
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

where git >nul 2>&1
if errorlevel 1 echo Aviso: no hay git. El boton Sync de la web lo necesita. Ver README.md.

where g++ >nul 2>&1
if errorlevel 1 echo Aviso: no hay g++. Puedes enviar en Python 3; para C++ instala un compilador. Ver README.md.

echo.
echo Listo. Arranca la GUI con start.bat
echo Luego abre http://127.0.0.1:5050
exit /b 0
