# Дан список случайных элементов. Проверьте, что все его элементы уникальны
def task1():
    from random import randint
    lst = [randint(0, 10) for _ in range(5)]
    print("Исходный список:", lst)
    if len(lst) == len(set(lst)):
        print("Список состоит из уникальных элементов")
    else:
        print("Список содержит повторяющиеся значения")
    
# Даны два случайных пятизначных числа. Определить, состоят ли они из одних и тех же цифр
def task2():
    from random import randint
    n1 = randint(9999, 99999)
    n2 = randint(9999, 99999)
    print("Исходные числа:", n1, "и", n2)

    set1 = set(str(n1))
    set2 = set(str(n2))
    if (len(set1) != len(set2)) or (len(set1 - set2) != 0):
        print(f"Числа {n1} и {n2} состоят из разных цифр")
    else:
        print(f"Числа {n1} и {n2} состоят из одинаковых цифр {list(set1)}")

# Напишите программу вычисления арифметического выражения, заданного строкой.
# Используйте операции +, -, *, /. Приоритет операций стандартный
def task3():
    expr = input("Введите выражение: ")
    expr = expr.replace('-', "+-").replace('/', "*1/")
    print(expr.split("*"))
    lst = expr.split("*")
    for idx in range(len(lst)):
        if isinstance(lst[idx], str) and '/' in lst[idx]:
            i, j = lst[idx].split("/")
            lst[idx] = int(i) / int(j)
        if isinstance(lst[idx], str) and '+' in lst[idx]:
            sublst = lst[idx].split("+")
            lst[idx] = 0
            for k in range(len(sublst)):
                lst[idx] += int(sublst[k])
    result = 1
    print(lst)
    for i in lst:
        if isinstance(i, str):
            result *= int(i)
        else:
            result *= i

    print(result)

# Имеется 1000 рублей. Бык стоит – 100 рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги, если всего надо купить 100 голов скота?
def task4():
    budget = 1000
    bulls_price = 100
    cow_price = 50
    calf_price = 5

    max_bulls_count = budget // bulls_price
    max_cow_count = budget // cow_price
    max_calf_count = budget // calf_price

    for bull in range(max_bulls_count + 1):
        for cow in range(max_cow_count + 1):
            for calf in range(max_calf_count + 1):
                if bull + cow + calf == 100 and\
                   bull * bulls_price + cow * cow_price + calf * calf_price == 1000:
                    print(f"{bull} {cow} {calf}")

