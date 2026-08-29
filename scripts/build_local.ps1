# CURRENTLY ONLY WORK FOR WINDOWS

# 1. Activate the python virtual environment inside the current script scope
Write-Host "Activating python .venv..." -ForegroundColor Cyan
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& .venv\Scripts\Activate.ps1)

python scripts/inject_page_exports.py
jupyter-book build --pdf
jupyter-book start
