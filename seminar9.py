# Задание 1. Проверьте, существует ли связь между данными, приведёнными в таблице.
# Выполните задание с помощью библиотеки NumPy
import numpy as np

def task1():
    nums_f = [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
    nums_s = [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
    nums_t = [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]

    matrix = [nums_f, nums_s, nums_t]
    result = np.corrcoef(matrix)
    print(result)

# В результате выполнения функции corrcoef возвращается таблица с коэфициентами корреляции

#           nums_f        nums_s      nums_t
#           -----------   ----------  ----------
# nums_f    1             0.90175619  0.87896031 
# nums_s    0.90175619    1           0.98700897 
# nums_t    0.87896031    0.98700897  1



# Задача 2. Дан массив случайных чисел. Создайте его с помощью NumPy. Определите его среднее арифметическое
# На ввод подаётся число. Определите ближайший по значению к нему элемент массива

def task2():
    size = 10
    numbers = np.random.randint(10, 100, size)
    mean = np.mean(numbers)
    print(f'Исходный массив: {numbers}')
    print(f'Среднее арифметическое: {mean}')

    num = int(input("Введите число: "))
    dist = [np.abs(i - num) for i in numbers]
    print(f'Ближайший элемент к {num}: {numbers[dist.index(min(dist))]}')


# Зздача 3. Задайте квадратную матрицу, состоящую из случайных чисел.
# Найдите самый встречающийся элемент в этой матрице
def task3():
    size = (4, 4)
    numbers = np.random.randint(1, 10, size)
    uniq_elements, uniq_counts = np.unique(numbers, return_counts=True) # возвращает массив уникальных элементов и массив количеств каждого элемента
    max_count = max(uniq_counts)

    print(f'Исходный массив: {numbers}')
    print('Частовстречающиеся элементы')
    for i in range(len(uniq_counts)):
        if (uniq_counts[i] == max_count):
            print(f"Элемент {uniq_elements[i]} встречается {uniq_counts[i]} раз(а)")

# Задача 4. Дан двумерный массив, заполненный нулями и единицами. Определить, есть ли в нём нулевые столбцы
def task4():
    size = (3, 10)
    numbers = np.random.randint(0, 2, size)
    axis = 0
    count_axis = 0
    print(numbers)

    result = numbers.any(axis=axis) # содержит ли столбец (axis=0) хотя бы одну единицу 
    # result = ~result - операция инверсии списка
    for i in range(len(result)):
        if not result[i]:
            print(f'Найден нулевой столбец: {i+1}')
            count_axis += 1
    if (count_axis == 0):
        print('Нулевых столбцов не найдено')

task4()



