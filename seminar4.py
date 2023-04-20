# Создайте кортеж. Запишите в него 10 случайных чисел
def task0():
    import random
    tpl = tuple(random.randint(0, 10) for _ in range(10))
    print(tpl)

# Создайте кортеж. Напишите метод, который по заданному индексу заменяет элемент в кортеже на случайный
def replace_tuple_element(tpl: tuple, idx: int, new_element: int):
    if 0 <= idx < len(tpl):
        tpl = tpl[:idx] + (new_element, ) + tpl[idx+1:]
    return tpl

def task1():
    from random import randint
    tpl = tuple(randint(0, 100) for _ in range(10))
    print(f"Исходный кортеж:   {tpl}")
    tpl_2 = replace_tuple_element(tpl, 9, randint(0, 100))
    print(f"Измененный кортеж: {tpl_2}")

# На вход подаются два числа. Напишите метод, который вернёт сумму, разность, произведение и частное этих чисел
def summ(first: int, second: int):
    return first + second

def prod(first: int, second: int):
    return first * second

def div(first: int, second: int):
    if second == 0:
        return None
    else:
        return first / second

def diff(first: int, second: int):
    return first - second

def task2():
    n = int(input("Введите первое число: "))
    m = int(input("Введите второе число: "))
    print(f"Сумма чисел {n} и {m}: {summ(n, m)}")
    print(f"Произведение чисел {n} и {m}: {prod(n, m)}")
    print(f"Частное от деления {n} и {m}: {div(n, m)}")
    print(f"Разность чисел {n} и {m}: {diff(n, m)}")

# Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов.
# Удалите из списка дубликаты уже имеющихся элементов. Определите, сколько элементов было удалено
def task3():
    from random import randint
    lst = [randint(1, 21) for _ in range(10)]
    lst_2 = list(set(lst))
    print(f"Исходный список: {lst}")
    print(f"Список из уникальных элементов: {lst_2}")
    print(f"Удалено элементов: {len(lst) - len(lst_2)}")

# Актёров разделили на списки по трём качествам «умные», «красивые», «сильные». 
# На главную роль нужен актёр обладающий всеми тремя качествами. Определите, сколько есть претендентов на главную роль
def task4():
    st_1 = {"Илья", "Фёдор", "Семён", "Олег", "Лев", "Антон", "Артём", "Боря", "Стас", "Марк", "Ян"}
    st_2 = {"Илья", "Георгий", "Лев", "Демьян", "Антон", "Владислав", "Боря", "Стас", "Макс", "Владимир"}
    st_3 = {"Фёдор", "Георгий", "Олег", "Демьян", "Артём", "Елисей", "Боря", "Стас", "Владимир"}
    print(f"Претенденты: {(st_1.intersection(st_2)).intersection(st_3)}")
