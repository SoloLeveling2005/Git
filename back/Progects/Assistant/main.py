import json, pyaudio
import subprocess

import pyttsx3
from vosk import Model, KaldiRecognizer
import regex

import os
import time

import psutil as psutil
import re

model = Model('vosk-model-ru-0.22')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

path_telegram = r'D:/Download/Telegram Desktop/Telegram.exe'
path_whats_up = r"C:/Users/Admin/AppData/Local/WhatsApp/WhatsApp.exe"

print("start")
def say(tell):
    engine = pyttsx3.init()  # object creation

    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty('rate', 155)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    # engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
    #
    # """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
    # engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

    engine.say(tell)
    # engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']


for text in listen():
    print(text)
    open = ["открой", "открыть", "откроет", "открыл", ""]
    close = ["закрой", "закрыть", "закроет", "закрыл", ""]
    text_list = text.split()
    for value in text_list:
        # print("текст открывания ", value)
        if value in open:
            index_value = text_list.index(value)
            len_text_list = len(text_list)
            right_sum_in_list = len_text_list - (index_value + 1)
            text_which_find = ""
            for relevance in text_list:
                if text_list.index(relevance) >= (index_value + 1):
                    text_which_find += (relevance + " ")

            text_which_find = re.sub("^\s+|\n|\r|\s+$", '', text_which_find)

            print(text_which_find)
            if text_which_find == "телеграмм":
                # say("Открываю")
                os.startfile(path_telegram)
            elif text_which_find == "ват цап":
                os.startfile(path_whats_up)

            break
        elif value in close:
            index_value = text_list.index(value)
            len_text_list = len(text_list)
            right_sum_in_list = len_text_list - (index_value + 1)
            text_which_find = ""
            for relevance in text_list:
                if text_list.index(relevance) >= (index_value + 1):
                    text_which_find += (relevance + " ")

            text_which_find = re.sub("^\s+|\n|\r|\s+$", '', text_which_find)

            print(text_which_find)
            if text_which_find == "телеграмм":
                subprocess.call(path_telegram)
                for process in (process for process in psutil.process_iter() if process.name() == "Telegram.exe"):
                    process.kill()
            break
    if text == "сколько тебе лет":
        say("Мне 36")
    elif text == "как тебя зовут":
        say("Меня зовут Виктория")

# engine = pyttsx3.init()  # object creation
#
# """ RATE"""
# rate = engine.getProperty('rate')  # getting details of current speaking rate
# print(rate)  # printing current voice rate
# engine.setProperty('rate', 155)  # setting up new voice rate
#
# """VOLUME"""
# volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
# print(volume)  # printing current volume level
# # engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
# #
# # """VOICE"""
# voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# # engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
#
# engine.say("Hi")
# # engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()


#
#
# for process in (process for process in psutil.process_iter() if process.name()=="Telegram.exe"):
#     process.kill()
