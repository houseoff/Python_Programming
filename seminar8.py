# Задача 1. Напишите чат-бота, который записывает сообщения всех пользователей, которые ему написали
# Задача 2. Добавьте боту возможность регистрации. Добавьте команду, которая запишет id и имя пользователя в файл
# Задача 3. Добавьте возможность рассылки напоминания всем зарегистрированным пользователям
# Задача 4. Добавьте боту клавиатуру для основных команд

from random import randint
from telebot import types
import telebot
import requests
import re

API_TOKEN = "<API_TOKEN>"
LOG_BOT = "log_bot.txt"
USERS_FILE = "users.txt"
ADMINS_IDS = ('<ID>',)

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

def write_log(message, text=None):
    from datetime import datetime
    line = f"{datetime.now()} {message.from_user.first_name} {message.from_user.last_name} {message.from_user.username}: "
    if text == None:
        line += f"{message.text}"
    else:
        line += text
    write_file(LOG_BOT, line)

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id in ADMINS_IDS:
        markup = new_inline_keyboard(['📨 Сделать рассылку'], ['send_all'])
        text = "Команды для админов"
    else:
        markup = new_inline_keyboard(['📝 Зарегистрироваться'], ['btn1'])
        text = "Приветствую! У меня есть возможность зарегистрировать пользователя!"
    bot.send_message(message.from_user.id, text, reply_markup=markup)

@bot.callback_query_handler(lambda x: x.data == 'btn1')
def register_user(message):
    print(message.from_user.id)
    print(read_file(USERS_FILE))
    if str(message.from_user.id) not in read_file(USERS_FILE):
        write_file(USERS_FILE, f"{message.from_user.id}")
        write_log(message, text="BOT: Попытка регистрации")
        bot.send_message(message.from_user.id, text="Зарегистрирован))")
        write_log(message, text="BOT: Регистрация прошла успешно")
    else:
        write_log(message, text="BOT: Пользователь уже зарегистрирован")
        bot.send_message(message.from_user.id, "Бро, ты уже зареган!")

@bot.callback_query_handler(lambda x: x.data == 'send_all')
def send_all(message):
    for id in read_file(USERS_FILE):
        bot.send_message(id, "Совещание через 5 минут")
        write_log(message, text="BOT: Админ сделал рассылку")

@bot.message_handler(content_types=['text'])
def text_message(message):
    write_log(message)

bot.polling()
