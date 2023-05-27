import telebot
import os
import json

CFG = {
    'API_TOKEN': "<API_TOKEN>",
    'LOG_BOT': "log_bot.txt",
    'REPLIES_DIR': "hw8/replies"
}

def read_file(filename: str):
    with open(filename, mode='r', encoding='UTF-8') as file:
        return file.readline().replace('\n','')

bot = telebot.TeleBot(CFG['API_TOKEN'])

q_files = os.listdir(CFG['REPLIES_DIR'])
if q_files:
    print(f'Есть вопросы от пользователей ({len(q_files)} шт.)')
    for i in range(len(q_files)):
        retry_obj = json.loads(read_file(f"{CFG['REPLIES_DIR']}/{q_files[i]}"))
        print(f"Вопрос {i+1}: {retry_obj['question']}")
        answer = input('Ответ: ')
        bot.send_message(retry_obj['user_id'], answer, reply_to_message_id=retry_obj['message_id'])
        os.remove(f"{CFG['REPLIES_DIR']}/{q_files[i]}")
else:
    print('Вопросов от пользователей не поступало')