# -*- coding: utf-8 -*-
import sys

import requests

# Импортируем библиотеки многопоточности
import threading
from threading import Thread

# Импортируем библиотеки для создания презентабельности проекта
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QCheckBox
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QSize, Qt

# Импортируем библиотеку для работы со временем
import time

# КОНТЕНТ

status_in_virtual = False
#  Очищаем старый скрипт чтобы не возникло ошибок


#  Очищаем прошлый скрипт чтобы не возникло ошибок

class MainWindow(QWidget):  # MainWindow - класс наследник(дочерний) от класса QWidget(родитель)
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)  # тут происходит вызов конструктора для родителя
        self.setWindowTitle(title)
        self.resize(width, height)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.line_edit_path = QLineEdit('http://127.0.0.1:5000/read')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_path, 0, 0)  # вкладываем QLineEdit -> QGridLayout

        self.label_check = QLabel('Пока ничего')  # экзампляр строки текста
        self.layout.addWidget(self.label_check, 1, 0)

        self.push_button_stop = QPushButton('Find')  # экзампляр строки ввода текста
        self.layout.addWidget(self.push_button_stop, 2, 2)  # вкладываем QLineEdit -> QGridLayout
        self.push_button_stop.clicked.connect(self.found)

        self.show()

    def found(self):
        url = self.line_edit_path.text()
        headers = {'User-agent': 'your bot 0.1'}
        response = requests.get(url=url, headers=headers)
        response = response.text[4:]
        response = response[:-5]
        print(response)
        self.label_check.setText(response)




app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'My App')
app.exec()