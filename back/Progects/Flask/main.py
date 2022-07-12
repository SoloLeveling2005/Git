
from flask import Flask
import os
import time



# ИМПОРТИРУЕМ БИБЛИОТЕКИ


# Импортируем библиотеку для работы с комндной строкой Windows
import sys
import os.path
import os



app = Flask(__name__)
@app.route("/read")
def index():
    file = open("text", "r+")
    text = file.readline()
    print(text)
    return f"<h1>{text}</h1>"




if __name__ == '__main__':
    app.run()
