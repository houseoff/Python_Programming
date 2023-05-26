# Задача 1. Напишите чат-бота, который записывает сообщения всех пользователей, которые ему написали

from random import randint
from telebot import types
import telebot
import requests
import re
from datetime import datetime

API_TOKEN = "<API_TOKEN>"
LOG_BOT = "log_bot.txt"

bot = telebot.TeleBot(API_TOKEN)

def read_file(filename: str):
    with open(filename, mode='r', encoding='UTF-8') as file:
        return file.readlines()

def write_file(filename: str, data):
    with open(filename, mode='a', encoding='UTF-8') as file:
        file.write(data + "\n")

@bot.message_handler(commands=['start'])
def text_message(message):
    write_file(LOG_BOT, message.text)
    print(read_file(LOG_BOT))

@bot.message_handler(content_types=['text'])
def text_message(message):
    print(message)
    text = f"{datetime.now()} {message.from_user.first_name} {message.from_user.last_name} {message.chat.username}: {message.text}"
    write_file(LOG_BOT, text)
    print(read_file(LOG_BOT))

bot.polling()
