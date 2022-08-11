cd ..\

@echo off
set /p title_venv="Enter venv name: "
call %title_venv%/bin/activate.bat

pip install django

@echo off
set /p title_app="Enter app name: "
django-admin startproject %title_app%

cmd