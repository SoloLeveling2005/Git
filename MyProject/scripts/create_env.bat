cd ..\


python -m pip install --upgrade pip


@echo off
set /p title_venv="Enter venv name: "


python -m venv %title_venv%


call .%title_venv%/bin/activate.bat

cmd