# Дано натуральное число N. 
# Напишите метод, который вернёт список простых множителей числа N и количество этих множителей
def task1():
    n = int(input("Введите число: "))
    lst = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n / i
            lst.append(i)
        else:
            i += 1

    print(f"Кол-во делителей числа: {len(lst)} {lst}")

# В первом списке находится информация об ассортименте мороженного, 
# во втором списке - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился
def task2():
    st_1 = {"Сливочное", "Бурёнка", "Вафелька", "Сладкоежка"}
    st_2 = {"Сливочное", "Вафелька", "Сладкоежка"}
    print(f"Закончилось: {st_1.difference(st_2)}")

# Выведите число π с заданной точностью. Точность вводится в виде десятичной дроби
def task3():
    from math import pi
    t = float(input("Введите точность: "))
    str_t = "{:.20f}".format(t)
    print("{:.{}f}".format(pi, str_t.find('1') - 1))

#  Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов
def read_file(filename: str):
    with open(filename, encoding='utf-8') as f:
        text = f.readline()
        return text

def parse_to_dict(expr: list):
    dct = {}
    for i in range(len(expr)):
        if   expr[i].count("x^") == 1: expr[i] = expr[i]
        elif expr[i].count('x')  == 1: expr[i] = expr[i] + "^1"
        else:                          expr[i] = expr[i] + "x^0"

        key =   expr[i].split("x^")[1]
        value = expr[i].split("x^")[0]
        if   value == '':  value = 1
        elif value == '-': value = -1

        if key in dct: dct[key] += int(value)
        else:          dct[key] =  int(value)

    return dct

def sum_expr(dict_1: dict, dict_2: dict):
    lst = []
    keys = list(set(list(dict_1.keys()) + list(dict_2.keys())))
    keys.sort(reverse=True)
    value = 0
    for key in keys:
        if key in dict_1 and key in dict_2: value = dict_1[key] + dict_2[key]
        elif key in dict_1:                 value = dict_1[key]
        else:                               value = dict_2[key]

        if   key == '0': lst.append("{}".format(value))
        elif key == '1': lst.append("{}x".format(value))
        else:            lst.append("{}x^{}".format(value, key))
    return lst

def print_expr(expr: list):
    result_str = ""
    for i in range(len(expr)):
        if i == 0:
            result_str += expr[i]
        else:
            if   expr[i].count('-') == 0: result_str += " + {}".format(expr[i])
            elif expr[i].count('-') == 1: result_str += " {} {}".format(expr[i][0], expr[i][1:])
    print(result_str)
      
def task4():
    expr1_file = 'expr_1.txt'
    expr2_file = 'expr_2.txt'

    expr_1 = read_file(expr1_file).replace("-", "+-").replace(" ", "").split("+")
    expr_2 = read_file(expr2_file).replace("-", "+-").replace(" ", "").split("+")

    expr_1 = list(filter(None, expr_1))
    expr_2 = list(filter(None, expr_2))

    dict_1 = parse_to_dict(expr_1)
    dict_2 = parse_to_dict(expr_2)

    

    result_lst = sum_expr(dict_1, dict_2)
    print_expr(result_lst)
