# Задача 1. Создайте пользовательский аналог метода filter()

def custom_filter(func, obj):
    return (i for i in obj if func(i))

def task1():
    lst = [1, 2, 3, 4]
    print(list(custom_filter(lambda x: x % 2 == 0, lst)))

# Задача 2. Создайте метод, позволяющий замерить время работы других методов
def stopwatch(func):
    from time import time
    def decorator():
        start_time = time()
        func()
        print(f"Время выполнения: {time() - start_time}")
    return decorator

# Декоратор - добавление функции новых инструкций, не меняя инструкции самой функции (навешивание новых функций). Декоратор используется след. образом

# Навешивание декоратора происходит в месте определения функции

@stopwatch
def func_to_test(row=10, column=1000):
    for i in range(row):
        for j in range(column):
            print(i, j)


# Задача 3. Создайте декоратор для нахождения метода суммы
def custom_format(func):
    def decorator(*args): # Передача любого кол-ва параметров декоратору
        for arg in args:
            print(f"{arg} + ", end='')
        print("\b\b= ", end='') # \b - возврат каретки на символ назад
        func(*args) # Передача параметров от декоратора в обернутую им функцию
    return decorator

@custom_format
def summa(a, b):
    print(a + b)

@custom_format
def sum4(a, b, c, d):
    print(a + b + c + d)

# Задача 4. Создайте декоратор с параметрами
def greetings(hello):
    def our_greetings(func):
        def decorator():
            print(f'{hello}, {func()}')
        return decorator
    return our_greetings

@greetings('Привет')
def get_name():
    return input("Как тебя зовут?\n")

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

# Бот реагирует на отправленный текст "Привет" и отвечает "Привет, имя и фамилия пользователя" и т. д.
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