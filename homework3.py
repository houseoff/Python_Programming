# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи
def task1():
    n = int(input("Введите число: "))
    lst = [1, 1]
    if n > 2:
        for i in range(1, n):
            lst.append(lst[i] + lst[i - 1])
    print(lst[:n])

# В списке находятся названия фруктов. 
# Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва
def task2():
    dct = dict(
        a = ['абрикос', 'авокадо', 'апельсин', 'айва'],
        б = ['бананы', 'бергамот'],
        в = ['виноград'],
        г = ['грейпфрут', 'гуава'],
        д = ['']
    )
    letter = input("Введите букву: ")
    print(dct[letter])

# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Е
# сли фраза ему неизвестна, он выводит соответствующую фразу
def read_file(filename: str):
    with open(filename, encoding='utf-8') as f:
        text = f.readlines()
        return text

def to_dict(text: list):
    dct = {}
    for line in text:
        temp = tuple(line.replace('\n', '').split(':'))
        key, value = temp
        dct[key] = value
    return dct

def write_to_file(filename: str, str_for_write: str):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n{str_for_write}")

def task3():
    answers_file = 'bot_answers.txt'
    requests_file = 'bot_questions.txt'
    dict_requests = to_dict(read_file(requests_file))
    dict_answers = to_dict(read_file(answers_file))
    
    phrase = ''
    while phrase != 'выход':
        phrase = input("Введите фразу: ")
        for i in range(len(dict_requests)):
            if phrase.strip().lower() == dict_requests[str(i)]:
                print(f"{dict_answers[str(i)]}")
                break
        else:
            if phrase != 'выход':
                print("Я не нашел данную фразу. Хотите её добавить?")
                print('Введите "Да", если хотите добавить фразу и, в дальнейшем, ответ на неё')
                print('Введите "Нет", если хотите продолжить общение с ботом')
                answer = input("Ваш ответ: ").strip().lower()
                if answer == 'да':
                    new_request = "{0}:{1}".format(len(dict_requests), phrase)
                    new_answer = input("Введите ответ на фразу: ").strip().lower()
                    new_answer = "{0}:{1}".format(len(dict_requests), new_answer)
                    write_to_file(requests_file, new_request)
                    write_to_file(answers_file, new_answer)
                    print("Фраза успешно добавлена! Перезапустите меня, чтобы я обновился")
                    print('Для выхода из программы - напишите "выход"')
 
    



    
