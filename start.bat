@echo off
setlocal
cd /d "%~dp0"

if not exist .venv\Scripts\python.exe (
  echo Primero instala las dependencias: install.bat
  echo Si fallo, mira README.md - Si el script falla.
  exit /b 1
)

.venv\Scripts\python.exe gui\app.py
exit /b %errorlevel%
