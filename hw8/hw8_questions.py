from random import randint
from telebot import types
import telebot
import re
import os

CFG = {
    'API_TOKEN': "<API_TOKEN>",
    'LOG_BOT': "log_bot.txt",
    'USERS_FILE': "users.txt",
    'REPLIES_DIR': "hw8/replies",
    'ADMINS_IDS': (948908953,),
    'IS_QUESTION_MODE' : False
}

def new_inline_keyboard(btn_names: list, btn_data_list: list, row_wight=1):
    markup = types.InlineKeyboardMarkup(row_width=row_wight)
    for i in range(len(btn_names)):
        markup.add(types.InlineKeyboardButton(btn_names[i], callback_data=btn_data_list[i]))
    return markup

def read_file(filename: str):
    with open(filename, mode='r', encoding='UTF-8') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
    return lines

def write_file(filename: str, data):
    with open(filename, mode='a', encoding='UTF-8') as file:
        file.write(data + "\n")

def write_obj(filename: str, data):
    with open(filename, mode='a', encoding='UTF-8') as file:
        file.write(data)

def write_log(message, text=None):
    from datetime import datetime
    line = f"{datetime.now()} {message.from_user.first_name} {message.from_user.last_name} {message.from_user.username}: "
    if text == None:
        line += f"{message.text}"
    else:
        line += text
    write_file(CFG['LOG_BOT'], line)

bot = telebot.TeleBot(CFG['API_TOKEN'])

@bot.message_handler(commands=['start', 'reset'])
def send_welcome(message):
    CFG['IS_QUESTION_MODE'] = False
    if message.from_user.id in CFG['ADMINS_IDS']:
        markup = new_inline_keyboard(['📨 Сделать рассылку'], ['send_all'])
        text = "Команды для админов"
    else:
        markup = new_inline_keyboard(['📝 Зарегистрироваться', '❓ Задать вопрос'], ['btn1', 'btn2'])
        text = "Приветствую! У меня есть возможность зарегистрировать пользователя! Также тех. поддержка может ответить на Ваш вопрос"
    bot.send_message(message.from_user.id, text, reply_markup=markup)

@bot.message_handler(func=lambda x: CFG['IS_QUESTION_MODE'], content_types=['text'])
def text_message(message):
    write_log(message, "BOT: Задан вопрос в тех. поддержку")
    filename = f"{CFG['REPLIES_DIR']}/q_{message.id}_{message.from_user.id}.txt"
    data = '{' + f'"message_id": {message.id}, "user_id": {message.from_user.id}, "question": "{message.text}"' + '}'
    write_obj(filename, data)
    bot.send_message(message.from_user.id, """Ваш вопрос успешно направлен службе поддержки. Пожалуйста, подождите ответа. \
В случае, если Вы передумали, или ответ слишком долгий, введите команду "/reset" и выберите пункт "❓ Задать вопрос" """)

@bot.callback_query_handler(lambda x: x.data == 'btn1')
def register_user(message):
    if str(message.from_user.id) not in read_file(CFG['USERS_FILE']):
        write_file(CFG['USERS_FILE'], f"{message.from_user.id}")
        write_log(message, text="BOT: Попытка регистрации")
        bot.send_message(message.from_user.id, text="Регистрация прошла успешно")
        write_log(message, text="BOT: Регистрация прошла успешно")
    else:
        write_log(message, text="BOT: Пользователь уже зарегистрирован")
        bot.send_message(message.from_user.id, "Вы уже зарегистрированы")

@bot.callback_query_handler(lambda x: x.data == 'btn2')
def welcome(message):
    CFG['IS_QUESTION_MODE'] = True
    bot.send_message(message.from_user.id, "Задайте, пожалуйста, Ваш вопрос")

@bot.callback_query_handler(lambda x: x.data == 'send_all')
def send_all(message):
    for id in read_file(CFG['USERS_FILE']):
        bot.send_message(id, "Совещание через 5 минут")
        write_log(message, text="BOT: Админ сделал рассылку")

bot.polling()