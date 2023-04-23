# Напишите программу, которая принимает на вход число N и выдаёт список факториалов для чисел от 1 до N
def subtask1(n: int):
    factorial = 1
    if n < 2: return factorial
    else:
        for i in range(1, n + 1):
            factorial *= i
    return factorial

def task1():
    n = int(input("Введите число: "))
    lst = []
    for i in range(1, n + 1):
        lst.append(subtask1(i))
    print(lst)

# Выведите таблицу истинности для выражения НЕ(X И Y) ИЛИ Z
def task2():
    print(f"x\ty\tz\tnot (x and y) or z")
    print(f"-\t-\t-\t------------------")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f"{x}\t{y}\t{z}\t{int(not (x and y) or z)}")

# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
def task3():
    string = input("Введите строку для поиска: ")
    substr = input("Введите искомую подстроку: ")
    for ch in substr:
        count = 0
        for i in range(len(string)):
            if string[i:i+len(ch)] == ch:
                count += 1
        print(f"'{ch}' - {count}")

# Дано число N. Создайте список с числами от -N до N. Сдвиньте все элементы списка на 2 позиции вправо
# Задача решена в общем виде: указывается число сдвигов. Если число сдвигов < 0 - сдвиг влево, иначе - сдвиг вправо
def task4():
    n = int(input("Введите число: "))
    shift = int(input("Введите число сдвигов: "))
    lst = [i for i in range(-n, n + 1)]
    len_lst = len(lst)
    print(f"Исходный список: {lst}")

    if shift < 0:
        shift = -shift
        print(f"Сдвиг влево на {shift} эл.: ", end='')
        shift %= len_lst
    elif shift == 0:
        print(f"Сдвиг на {shift} эл.:  ", end='')
    else:
        shift %= len_lst
        print(f"Сдвиг вправо на {shift} эл.: ", end='')
        shift = len_lst - shift
    
    print(lst[shift:] + lst[:shift])