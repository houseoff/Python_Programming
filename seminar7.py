# Задача 5. Создайте telegram-бота, добавьте в него метод приветствия пользователя
# Задача 6. Добавьте модуль для определения погоды с помощью сайта wttr.in
import telebot
import requests
import re

API_TOKEN = "<API_TOKEN>"

bot = telebot.TeleBot(API_TOKEN)

# Общаемся с ботом с помощью декораторов. Код ниже отправляет сообщение при вызове команд help, start
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Приветствую! Я тест-бот, написанный на Python. \
Я пока ещё туповат, но разработчик, который меня создал, надеюсь, сделает меня умным)\
""")

# Бот реагирует на отправленный текст "Привет" и отвечает "Привет, имя и фамилия пользователя"
@bot.message_handler(content_types=['text'])
def greetings(message):
    print(message)
    if re.findall("привет", message.text, re.IGNORECASE):
        bot.reply_to(message, f"Привет, {message.from_user.first_name} {message.from_user.last_name}")
    elif re.findall("погода", message.text, re.IGNORECASE):
        request = requests.get('http://wttr.in/?0T')
        bot.reply_to(message, request.text)
    elif re.findall("котик", message.text, re.IGNORECASE):
        request = requests.get('http://cataas.com/cat')
        bot.send_photo(message.from_user.id, request.content)

bot.polling()