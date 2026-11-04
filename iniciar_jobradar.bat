@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo Ambiente nao encontrado. Execute primeiro: python -m venv .venv
  pause
  exit /b 1
)

echo Iniciando JobRadar Brasil. Mantenha esta janela aberta.
".venv\Scripts\python.exe" main.py
