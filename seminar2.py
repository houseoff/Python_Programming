# Дано число N. Найти все его делители. Для каждого делителя укажите чётный он или нечётный
def task1():
    n = int(input("Введите число: "))

    for i in range(n, 0, -1):
        if n % i == 0:
            message = "(чётный)" if i % 2 == 0 else "(нечётный)"
            if i == 1:
                print(f"{i} {message}")
            else:
                print(f"{i} {message}", end=', ')

# Выведите таблицу истинности для выражения НЕ X ИЛИ Y
def task2():
    print(f"x\ty\tnot x or y")
    print(f"-\t-\t----------")
    for x in range(0, 2):
        for y in range(0, 2):
            print(f"{x}\t{y}\t{int(not x or y)}")

# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другую
def task3_1():
    string = input("Введите строку для поиска: ")
    substr = input("Введите искомую подстроку: ")
    return string.count(substr)

def task3_2():
    count = 0
    string = input("Введите строку для поиска: ")
    substr = input("Введите искомую подстроку: ")
    for i in range(len(string)):
        if string[i:i+len(substr)] == substr:
            count += 1
    print(count)

# Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81 и т.п.
def task4_1():
    n = int(input("Введите число: "))
    lst = [1] if n != 0 else []
    for i in range(1, n):
        if i % 2 != 0: lst.append(abs(lst[i - 1]) * -3)
        else: lst.append(abs(lst[i - 1]) * 3)
    print(lst)


def task4_2():
    n = int(input("Введите число: "))
    lst = []
    for i in range(n):
        lst.append((-3) ** i)
    print(lst)

# Найдите все числа до 10000, у которых количество делителей равно 10
def subtask5(n: int):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0: count += 1
    return count

def task5():
    for i in range(48, 10001):
        if subtask5(i) == 10:
            print(f"{i}\t", end='')