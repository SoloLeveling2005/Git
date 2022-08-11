cd ..\

call .\env\Scripts\activate.bat
@echo off
set /p id="Enter name_app: "

pip install Django

django-admin startapp %id%

python manage.py makemigrations

python manage.py migrate

cmd 