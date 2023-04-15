# Дан список, заполненный случайными числами от 0 до 10. Определите, является ли сумма всех элементов чётной
def task0():
    import random
    lst = [random.randint(0, 10) for i in range(5)]
    print(f"Исходный список: {lst}")
    print("Сумма элементов четная" if sum(lst) % 2 == 0 else "Сумма элементов четная")

# В списке хранятся сведения о количестве осадков, выпавших за каждый день июня.
# Определите в какой период выпало больше осадков: в первой или второй половине июня
def task1():
    import random
    lst = [random.randint(0, 25) for i in range(30)]
    part1 = sum(lst[:int(len(lst)/2)])
    part2 = sum(lst[int(len(lst)/2):])
    print(f"Исходный список: {lst}")
    if part1 > part2:
        print(f"Кол-во осадков в первой половине июня больше ({part1}), чем во второй ({part2})")
    elif part1 < part2:
        print(f"Кол-во осадков во второй половине июня больше ({part1}), чем в первой ({part2})")
    else:
        print(f"Кол-во осадков в первой и второй половинах одинаково ({part1})")

# Задача 2. Напишите программу, которая позволит пользователю
# заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета
def task2():
    form = dict(
            Имя = input("Ваше имя: "), 
            Возраст = input("Ваш возраст: "), 
            Хобби = input("Ваше хобби: "), 
            Любимое_животное = input("Ваше любимое животное: "))
    
    print("Заполненная анкета: ")
    for key, value in form.items():
        print(f"{key}: {value}")

# Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел
def task3_1():
    import random
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    n = int(input("Введите длину пароля: "))

    print(f"Полученный пароль: ", end='')
    for i in random.sample(symbols, n):
        print(i, end='')

def task3_2():
    import random
    import string
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    symbols = s1 + s2 + s3 + s4
    n = int(input("Введите длину пароля: "))
    print(f"Полученный пароль: ", end='')
    for i in range(n):
        print(symbols[random.randint(0, len(symbols) - 1)], end='')

# Ручка стоит – 5 рублей, карандаш – 3 рубля, ластик – 4 рубля.
# Кассир последовательно вводит в программу позиции из чека «ручка», «карандаш», «ластик».
# Ввод заканчивается, когда введено слово «стоп». Определите сумму чека
def task4():
    dct = {'ручка': 5, 'карандаш': 3, 'ластик': 4}
    n = ''
    summa = 0
    while n != 'стоп':
        n = input("Введите товар: ").strip().lower()
        if n in dct.keys():
            summa += dct[n]
    print(f"Сумма чека: {summa}")