# Задача 1. Создайте пользовательский аналог метода map()
def custom_map(func, obj):
    return (func(i) for i in obj)

def task1():
    lst = [2, 3, 4, 5]
    print(list(custom_map(lambda x: x**3, lst)))

# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз
def retry(count):
    def our_repeat(func):
        def decorator(*args, **kwargs):
            for _ in range(1, count + 1):
                print(f"Попытка №{_}")
                print(func(*args, **kwargs))
        return decorator
    return our_repeat

@retry(5)
def custom_pow(num = 5, pow = 4):
    return num ** pow

# Задача 3. Добавьте в телеграм-бота игру "Угадай число". Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов
from random import randint
from telebot import types
import telebot
import requests
import re

API_TOKEN = "<API_TOKEN>"
GAME_PARAMS = {
    'in_game': False,
    'count_of_trying': 0,
    'number': 0
}
CATS_NUMS = (100, 101, 102, 103, 200, 201, 202, 203, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422, 423, 424, 425, 426, 429, 431, 444, 450, 451, 497, 498, 499, 500, 501, 502, 503, 504, 506, 507, 508, 509, 510, 511, 521, 522, 523, 525, 599)

def default_game_params():
    GAME_PARAMS['in_game'] = False
    GAME_PARAMS['count_of_trying'] = 0
    GAME_PARAMS['number'] = 0

def new_inline_keyboard(btn_names: list, row_wight=1):
    markup = types.InlineKeyboardMarkup(row_width=row_wight)
    for i in range(len(btn_names)):
        markup.add(types.InlineKeyboardButton(btn_names[i], callback_data=f'btn{i+1}'))
    return markup

bot = telebot.TeleBot(API_TOKEN)

# Общаемся с ботом с помощью декораторов. Код ниже отправляет сообщение при вызове команд help, start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = new_inline_keyboard(['👋 Поздороваться', '☀️ Подглядеть погоду', '🐱 Посмотреть на котика', '🎲 Сыграть в игру'])
    bot.send_message(message.from_user.id, """Приветствую! Я тест-бот, написанный на Python. \
Я пока ещё туповат, но разработчик, который меня создал, надеюсь, сделает меня умным)\
""", reply_markup=markup)

@bot.callback_query_handler(lambda x: x.data == 'btn1')
def send_hello(message):
    bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}")

@bot.callback_query_handler(lambda x: x.data == 'btn2')
def send_weather(message):
    try: 
        request = requests.get('http://wttr.in/?0T')
        text = request.text
    except:  text = "К сожалению, высшие силы не желают Вам раскрывать планы природы. Попробуйте обратиться к ним позднее"
    finally: bot.send_message(message.from_user.id, text)

@bot.callback_query_handler(lambda x: x.data == 'btn3')
def send_cat(message):
    try:
        request = requests.get(f'https://http.cat/{CATS_NUMS[randint(0, len(CATS_NUMS))]}')
        bot.send_photo(message.from_user.id, request.content)
    except:
        bot.send_message(message.from_user.id, "Я сожалею, но котики сейчас не хотят, чтобы на них смотрели. Попробуйте посмотреть на них позже")

@bot.callback_query_handler(lambda x: x.data == 'btn4')
def new_game(message):
    if GAME_PARAMS['in_game']:
        bot.send_message(message.from_user.id, "Вы уже в игре! Введите число: ")
    else:
        GAME_PARAMS['number'] = randint(1, 1000)
        GAME_PARAMS['in_game'] = True
        bot.send_message(message.from_user.id, "Cыграем в игру \"Угадай число\". Я загадал число от 1 до 1000. Чем быстрее угадаешь, тем ты круче. Поехали!")
        bot.send_message(message.from_user.id, "Введи число: ")

@bot.message_handler(func=lambda message: re.match("\d+", message.text) and GAME_PARAMS['in_game'])
def in_game(message):
    user_num = int(message.text)
    if 0 < user_num < 1001:
        if user_num == GAME_PARAMS['number']:
            if GAME_PARAMS['count_of_trying'] == 1:
                bot.send_message(message.from_user.id, f"Отлично! Ты отгадал с первой попытки! Я действительно загадал число {GAME_PARAMS['number']}")
            else:
                bot.send_message(message.from_user.id, f"Ура! Ты угадал! Я действительно загадал число {GAME_PARAMS['number']}. Кол-во попыток: {GAME_PARAMS['count_of_trying']}")
            default_game_params()
        else:
            bot.send_message(message.from_user.id, f"Ты пока не угадал. Моё число {'меньше' if GAME_PARAMS['number'] < user_num else 'больше'} твоего")
            GAME_PARAMS['count_of_trying'] += 1
            bot.send_message(message.from_user.id, "Введи число: ")
    else:
        bot.send_message(message.from_user.id, f"Твоё число ({user_num}) находится вне диапозона от 1 до 1000 включительно")
        bot.send_message(message.from_user.id, "Введи число: ")

bot.polling()
