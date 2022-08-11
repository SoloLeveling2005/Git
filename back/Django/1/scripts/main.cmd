cd ..\

python.exe -m pip install --upgrade pip

pip install env

python -m venv env

call .\env\Scripts\activate.bat

pip install --upgrade php





pip install -r requirements.txt

pip freeze > requirements.txt





pip install django

pip install pillow

django-admin startproject settings .

@echo off
set /p id="Enter startapp_app: "

django-admin startapp %id%


python manage.py makemigrtions
python manage.py migrate




python manage.py runserver 127.0.0.1:8000