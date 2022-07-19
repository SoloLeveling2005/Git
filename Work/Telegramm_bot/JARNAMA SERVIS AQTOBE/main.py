import time
import os
import re
from random import randint
from connect import bot
import telebot
from telebot import types  # кнопки Telegram
import requests
import datetime



print("Нажмите Ctrl+C если хотите завершить работу бота")

url = '<a href="https://t.me/jsaqtobe">Jarnama Servis Aqtobe</a>'
url_bot = "https://t.me/Jarnama_Servis_Aqtobe_bot"
id_admin = 5351207184
id_chanel = "@jsaqtobe"
# id_admin = 5351207184
# id_chanel = "@testing_bot2022"


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Создать объявление')
    item2 = types.KeyboardButton('Правила')
    item3 = types.KeyboardButton('Группа')
    item4 = types.KeyboardButton('Заказать рекламу')
    item5 = types.KeyboardButton('Написать Администратору')

    markup.add(item1, item2)
    markup.add(item3, item4)
    markup.add(item5)

    bot.send_message(message.chat.id,
                     f"Здравствуйте, @Jarnama_Servis_Aqtobe_bot поможет Вам разместить объявления в группе {url}",
                     parse_mode='HTML', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global step,rename
    if message.text == 'Создать объявление':
        # bot.delete_message(message.chat.id, message.message_id)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Задать вопрос', callback_data='Task_question')
        button2 = types.InlineKeyboardButton(text='Продам', callback_data='Sell')
        button3 = types.InlineKeyboardButton(text='Куплю', callback_data='Buy')
        button4 = types.InlineKeyboardButton(text='Услуга', callback_data='Service')
        button5 = types.InlineKeyboardButton(text='Аренда', callback_data='Rent')
        button6 = types.InlineKeyboardButton(text='Работа', callback_data='Work')
        button7 = types.InlineKeyboardButton(text='Партнерство', callback_data='Partnership')
        button8 = types.InlineKeyboardButton(text='Отдам', callback_data='Give')
        button9 = types.InlineKeyboardButton(text='Обмен', callback_data='Exchange')
        markup.add(button1)
        markup.add(button2, button3)
        markup.add(button4, button5)
        markup.add(button6, button7)
        markup.add(button8, button9)
        bot.send_message(message.chat.id, "Выберите тип объявления", reply_markup=markup)
    elif message.text == 'Правила':
        bot.delete_message(message.chat.id, message.message_id - 1)
        with open('rules.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        bot.send_message(message.chat.id,
                         f"{text}", parse_mode='HTML')
    elif message.text == 'Группа':
        bot.delete_message(message.chat.id,message.message_id - 1)
        bot.send_message(message.chat.id,
                         f"<b>Jarnama Servis Aqtobe</b>\nАқтөбе қалалық сауда алаңы \nТорговая площадка города Актобе \n{url}",
                         parse_mode='HTML')
    elif message.text == 'Заказать рекламу':
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id,
                         f'''По вопросам рекламы в группе <b>Jarnama Servis Aqtobe</b>, свяжитесь с <a href="tg://user?id={id_admin}">Администратором</a>''',
                         parse_mode='HTML', disable_web_page_preview=True)
    elif message.text == 'Написать Администратору':
        bot.delete_message(message.chat.id, message.message_id - 1)
        if step == "0":
            msg = bot.send_message(message.chat.id,
                                   'Введите сообщение для Администратора. Бот принимает только текст.')
            bot.register_next_step_handler(msg, send_message)
        else:
            step = 0
            rename = ""
            msg = bot.send_message(message.chat.id,
                                   'Введите сообщение для Администратора. Бот принимает только текст.')
            bot.register_next_step_handler(msg, send_message)

user_username = ""


def send_message(message):
    global user_username
    user_username = message.from_user.username
    one = message.from_user.id
    two = message.from_user.first_name
    three = message.from_user.last_name
    if message.from_user.username is None:
        bot.send_message(id_admin,
                         f'От <a href="tg://user?id="5351207184">{two}</a> сообщение: {message.text}')
        bot.send_message(message.chat.id, 'Сообщение отправлено, с вами скоро свяжуться!')
    else:
        bot.send_message(id_admin,
                         f'От @{message.from_user.username} сообщение: {message.text}')
        bot.send_message(message.chat.id, 'Сообщение отправлено, с вами скоро свяжуться!')

    print(two)
    print(user_username)


# bot.send_message("@testing_bot2022","Hi")

text_message = ""
geolocation = ""

status = "False"
topic = ""
step = 0
user_id = ""
mess_id = 0
url_user = ""
img = ''
with_img = ""
rename = ""


def task_question_step_2(message):
    global step
    global user_id
    if step == 1:
        step = 2
        user_id = message.from_user.id
        global text_message
        text_message = message.text
        global url_user
        url_user = message.from_user.username

        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text='Продолжить без картинки', callback_data='Without_img_task_question')
        markup.add(button)

        msg = bot.send_message(message.chat.id,
                               'Отправьте картинку (шаг 2/2)', reply_markup=markup)

        bot.register_next_step_handler(msg, task_question_step_3)


def task_question_step_3(message):
    global step
    if step == 2:
        step = 3
        try:
            if message.content_type == 'photo':
                img = message.photo[2].file_id

                bot.send_photo(id_chanel, img, caption=text_message)
                bot.send_message(message.chat.id, 'Ваше объявление опубликовано!')

            else:
                bot.send_message(message.chat.id,
                                 f"Это не фото")
        finally:
            step = 0


#

def step_2(message):
    global step
    global geolocation
    global url_user
    global user_id
    if step == 1:
        step = 2
        user_id = message.from_user.id
        geolocation = message.text

        url_user = message.from_user.username

        msg = bot.send_message(message.chat.id,
                               '<b>Введите текст рекламного поста (шаг 2/3)</b> \n\nВведите подробное описание и контакты.',
                               parse_mode='HTML')
        bot.register_next_step_handler(msg, step_3)


def step_3(message):
    global step
    global with_img
    global text_message
    global status
    global user_id
    if step == 2:
        step = 3

        text_message = message.text

        status = "True"
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text='Продолжить без картинки', callback_data='Without_img')
        markup.add(button)
        with_img = "True"
        msg = bot.send_message(message.chat.id,
                               'Отправьте картинку (шаг 3/3)', reply_markup=markup)
        bot.register_next_step_handler(msg, step_4)


def step_4(message):
    global step, geolocation, rename
    global img
    global mess_id
    global with_img
    global text_message
    global user_id
    if rename == "town":
        geolocation = message.text
    elif rename == "description":
        text_message = message.text
    elif rename == "image":
        img = message.photo[2].file_id
    if step == 3:
        step = 4
        try:

            print(message.content_type)
            print(with_img)
            if message.content_type == 'photo' and with_img == "True":
                img = message.photo[2].file_id

                mess = bot.send_photo(message.chat.id, img,
                                      caption=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={user_id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                      parse_mode='HTML')

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Опубликовать', callback_data='Public')
                button2 = types.InlineKeyboardButton(text='Исправить', callback_data='Edit')
                button3 = types.InlineKeyboardButton(text='Отменить', callback_data='Сancel')
                markup.add(button1)
                markup.add(button2)
                markup.add(button3)

                bot.send_message(message.chat.id, "Ваши дальнейшие действия", reply_markup=markup)


            elif with_img == "True":

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Опубликовать', callback_data='Public')
                button2 = types.InlineKeyboardButton(text='Исправить', callback_data='Edit')
                button3 = types.InlineKeyboardButton(text='Отменить', callback_data='Сancel')
                markup.add(button1)
                markup.add(button2)
                markup.add(button3)

                mess = bot.send_photo(message.chat.id, img,
                                      caption=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={user_id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                      parse_mode='HTML')
                mess_id = mess.id
                bot.send_message(message.chat.id, "Ваши дальнейшие действия", reply_markup=markup)

            elif with_img == "False":

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Опубликовать', callback_data='Public')
                button2 = types.InlineKeyboardButton(text='Исправить', callback_data='Edit')
                button3 = types.InlineKeyboardButton(text='Отменить', callback_data='Сancel')
                markup.add(button1)
                markup.add(button2)
                markup.add(button3)
                print("dats",topic)
                print("dats",geolocation)
                print("dats",text_message)
                mess = bot.send_message(message.chat.id,
                                        text=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={user_id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                        parse_mode='HTML', disable_web_page_preview=True)
                # ess = bot.send_message(message.chat.id,"Hi",parse_mode='HTML')

                bot.send_message(message.chat.id, "Ваши дальнейшие действия", reply_markup=markup)

        except:
            bot.send_message(message.chat.id,
                             f"Проверьте формат фото")
            step = 0
        finally:
            rename = ""


def step_4_5(message):
    global step
    global img
    global mess_id
    global with_img
    if step == 3:
        step = 4
        try:
            print(message.content_type)
            print(with_img)
            if message.content_type == 'photo' and with_img == "True":
                img = message.photo[2].file_id

                mess = bot.send_photo(message.chat.id, img,
                                      caption=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={message.from_user.id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                      parse_mode='HTML')

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Опубликовать', callback_data='Public')
                button2 = types.InlineKeyboardButton(text='Исправить', callback_data='Edit')
                button3 = types.InlineKeyboardButton(text='Отменить', callback_data='Сancel')
                markup.add(button1)
                markup.add(button2)
                markup.add(button3)

                bot.send_message(message.chat.id, "Ваши дальнейшие действия", reply_markup=markup)


            elif with_img == "True":

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Опубликовать', callback_data='Public')
                button2 = types.InlineKeyboardButton(text='Исправить', callback_data='Edit')
                button3 = types.InlineKeyboardButton(text='Отменить', callback_data='Сancel')
                markup.add(button1)
                markup.add(button2)
                markup.add(button3)

                mess = bot.send_photo(message.chat.id, img,
                                      caption=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={message.from_user.id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                      parse_mode='HTML')
                mess_id = mess.id
                bot.send_message(message.chat.id, "Ваши дальнейшие действия", reply_markup=markup)

            elif with_img == "False":

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Опубликовать', callback_data='Public')
                button2 = types.InlineKeyboardButton(text='Исправить', callback_data='Edit')
                button3 = types.InlineKeyboardButton(text='Отменить', callback_data='Сancel')
                markup.add(button1)
                markup.add(button2)
                markup.add(button3)

                mess = bot.send_message(message.chat.id,
                                        text=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={message.from_user.id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                        parse_mode='HTML')

                bot.send_message(message.chat.id, "Ваши дальнейшие действия", reply_markup=markup)
        except:
            bot.send_message(message.chat.id,
                             f"Проверьте формат фото")
            step = 0




def step_5(message):
    global step, rename
    global mess_id
    global img

    now = datetime.datetime.now()
    now = (str(now).split("."))[1]
    rand = randint(101, 999)
    now_rand = now + str(rand)
    print(now_rand)



    if step == 4:
        step = 5
        try:
            if with_img == "True":

                mess_chanel = bot.send_photo(id_chanel, img,
                                             caption=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={user_id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                             parse_mode='HTML')
                callback_data_dell_chanel = "Delete" + str(mess_chanel.id)
                print(callback_data_dell_chanel)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Просмотреть', url=f"https://t.me/jsaqtobe/{mess_chanel.id}")
                button2 = types.InlineKeyboardButton(text='Удалить', callback_data=callback_data_dell_chanel)
                markup.add(button1)
                markup.add(button2)

                mess_my = bot.send_photo(message.chat.id, img,
                                         caption=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={user_id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                         parse_mode='HTML', reply_markup=markup)

                bot.send_message(message.chat.id, 'Ваше объявление опубликовано!')
                mess = (str([mess_my.id, mess_chanel.id, now_rand]) + "\n")
                f = open('data_user.txt')
                old_data = f.read()
                f.close()
                f = open('data_user.txt', 'w')
                f.write(str(old_data) + str(mess))
                f.close()

            elif with_img == "False":

                mess_chanel = bot.send_message(id_chanel,
                                               text=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={user_id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                               parse_mode='HTML', disable_web_page_preview=True)

                callback_data_dell_chanel = "Delete" + str(mess_chanel.id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Просмотреть', url=f"https://t.me/jsaqtobe/{mess_chanel.id}")
                button2 = types.InlineKeyboardButton(text='Удалить', callback_data=callback_data_dell_chanel)
                markup.add(button1)
                markup.add(button2)

                mess_my = bot.send_message(message.chat.id,
                                           text=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={user_id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                           parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)



                bot.send_message(message.chat.id, 'Ваше объявление опубликовано!')

                mess = (str([mess_my.id, mess_chanel.id, now_rand]) + "\n")
                f = open('data_user.txt')
                old_data = f.read()
                f.close()
                f = open('data_user.txt', 'w')
                f.write(str(old_data) + str(mess))
                f.close()
        # except:
        #     print("Что то не то в ступени 5")
        finally:
            step = 0
            rename = ""



# def step_town():
#
# def step_description():
#
# def step_foto():

#


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call: types.CallbackQuery):

    print(call.message.id)
    print(call.data)

    call_data = (call.data).split("Delete")
    if len(call_data) > 1:
        print(call_data)
        print("Hi")
        try:
            id_message = call.message.id
            print(id_message)
            f = open('data_user.txt')
            old_data = f.read()
            new_data = ""
            old_data_list = old_data.split("\n")
            print(old_data_list)
            for i in old_data_list:
                if str(id_message) in str(i):
                    i = i.split(" ")
                    i = i[1].split("]")
                    i = i[0]
                    i = i.replace(",", "")
                    print(i)
                    bot.delete_message(id_chanel, int(i))
                    bot.send_message(call.message.chat.id,
                                     'Пост удален')
                else:
                    new_data += (str(i) + "\n")
            f.close()
            f = open('data_user.txt', 'w')
            f.write(str(new_data))
            f.close()

            f = open('data_user.txt')
            old_data = f.read()
            f.close()
            data_new = old_data.replace('\n\n', '\n')
            f = open('data_user.txt', 'w')
            f.write(str(data_new))
            f.close()
        except:
            bot.send_message(call.message.chat.id,
                     'Пост уже был удален')


    global status_task_question, rename
    global step
    global topic
    global geolocation
    global text_message
    global user_id
    global with_img

    def print_geolocation():
        msg = bot.send_message(call.message.chat.id,
                               '<b>Напишите ваше местоположение (шаг 1/3)</b>\n\nГород, населенный пункт',
                               parse_mode='HTML')
        bot.register_next_step_handler(msg, step_2)

    if call.data == "Task_question":
        topic = "Вопрос"

        if step == 0:
            step = 1
            msg = bot.send_message(call.message.chat.id,
                                   'Введите текст вопроса (шаг 1/2)')
            bot.register_next_step_handler(msg, task_question_step_2)

    elif call.data == "Without_img_task_question":
        step = 0
        bot.send_message(id_chanel,
                         text=f'{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={user_id}">НАПИСАТЬ АВТОРУ</a></b>',
                         parse_mode='HTML')
        bot.send_message(call.message.chat.id,
                         'Ваше объявление опубликовано!')

    elif call.data == "Without_img":
        with_img = "False"
        step_4(call.message)

    elif call.data == "Sell":
        topic = "Продам"
        if step == 0:
            step = 1
            print_geolocation()

    elif call.data == "Buy":
        topic = "Куплю"
        if step == 0:
            step = 1
            print_geolocation()

    elif call.data == "Service":
        topic = "Услуга"
        if step == 0:
            step = 1
            print_geolocation()

    elif call.data == "Rent":
        topic = "Аренда"
        if step == 0:
            step = 1
            print_geolocation()

    elif call.data == "Work":
        topic = "Работа"
        if step == 0:
            step = 1
            print_geolocation()

    elif call.data == "Partnership":
        topic = "Партнерство"
        if step == 0:
            step = 1
            print_geolocation()

    elif call.data == "Give":
        topic = "Отдам"
        if step == 0:
            step = 1
            print_geolocation()

    elif call.data == "Exchange":
        topic = "Обмен"
        if step == 0:
            step = 1
            print_geolocation()

    elif call.data == "Public":
        if step == 4:
            step_5(call.message)

    elif call.data == "Edit":
        if step == 4:
            if with_img == "True":
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Город', callback_data='Town')
                button2 = types.InlineKeyboardButton(text='Описание', callback_data='Description')
                button3 = types.InlineKeyboardButton(text='Фото', callback_data='Foto')
                markup.add(button1)
                markup.add(button2)
                markup.add(button3)

                mess = bot.send_photo(call.message.chat.id, img,
                                      caption=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={call.message.from_user.id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                      parse_mode='HTML')

                bot.send_message(call.message.chat.id, "Что исправить", reply_markup=markup)
            elif with_img == "False":
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Город', callback_data='Town')
                button2 = types.InlineKeyboardButton(text='Описание', callback_data='Description')
                button3 = types.InlineKeyboardButton(text='Фото', callback_data='Foto')
                markup.add(button1)
                markup.add(button2)
                markup.add(button3)

                mess = bot.send_message(call.message.chat.id, text=f'#{topic} ' + f'#{geolocation}' + f' \n\n{text_message} \n\n<b style=\"color:#fc5252;\"><a href="tg://user?id={call.message.from_user.id}">НАПИСАТЬ АВТОРУ</a></b>\n\n<b style=\"color:#fc5252;\"><a href="{url_bot}">Разместить бесплатные объявления через @Jarnama_Servis_Aqtobe_bot</a></b>',
                                      parse_mode='HTML')

                bot.send_message(call.message.chat.id, "Что исправить", reply_markup=markup)

    elif call.data == "Сancel":
        if step == 4:
            bot.send_message(call.message.chat.id, "Публикация отменена")
            step = 0
            topic = ""
            geolocation = ""
            text_message = ""
            rename = ""



    elif call.data == "Town":
        if step == 4:
            step = 3
            rename = "town"
            msg = bot.send_message(call.message.chat.id,
                                   '<b>Напишите ваше местоположение (шаг 1/3)</b>\n\nГород, населенный пункт',
                                   parse_mode='HTML')
            bot.register_next_step_handler(msg, step_4)

    elif call.data == "Description":
        if step == 4:
            step = 3
            rename = "description"
            msg = bot.send_message(call.message.chat.id,
                                   '<b>Введите текст рекламного поста (шаг 2/3)</b> \n\nВведите подробное описание и контакты.',
                                   parse_mode='HTML')
            bot.register_next_step_handler(msg, step_4)

    elif call.data == "Foto":
        if step == 4:
            step = 3
            rename = "foto"
            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text='Продолжить без картинки', callback_data='Without_img')
            markup.add(button)

            msg = bot.send_message(call.message.chat.id,
                                   'Отправьте картинку (шаг 3/3)', reply_markup=markup)
            with_img = "True"
            bot.register_next_step_handler(msg, step_4)




a = datetime.datetime.today()
print(a)


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        time.sleep(3)
        a = datetime.datetime.today()
        print(e)
        print(a)
        bot = telebot.TeleBot('5441523880:AAEhN8ED9N3z0VwAXNQdktrWlYQRpGqIhMA')
        bot.send_message(1303257033,
                         'Произошла остановка программы')
        os.system('python main2.py')
