# Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины
def task1():
    n = int(input("Введите число: "))
    print(f'Результат N + NN + NNN: {n + int(str(n) * 2) + int(str(n) * 3)}')

# Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в массиве последовательность
# из трёх элементов, совпадающая с введённым числом
def task2():
    from random import randint
    n = int(input('Введите число: '))
    lst = [randint(0, 9) for _ in range(10)]
    print(f"Исходный список: {lst}")

    for i in range(len(lst) - 2):
        if lst[i : i + 3] == [int(i) for i in str(n)]:
            print("Да")
            break
    else:
        print("Нет")
    
# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11
def is_mutually_simple(num1: int, num2: int):
    if num1 == 0 or num1 == 1: return False
    if num2 == 0 or num2 == 1: return False
    if num2 % num1 == 0: return False

    i = 2
    while i < num1:
        if num1 % i == 0 and num2 % i == 0:
            return False
        i += 1
    else:
        return True

def task3(start_numerator: int, end_denominator: int):
    if start_numerator == 0 or start_numerator >= end_denominator:
        print("Несократимых дробей не найдено")
    else:
        for i in range(start_numerator, end_denominator):
            for j in range(start_numerator + 1, end_denominator + 1):
                if is_mutually_simple(i, j) and i < j:
                    print(f'{i}/{j}')



