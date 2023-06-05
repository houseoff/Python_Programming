# Задача 1. Дан список элементов. 
# Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём
import numpy as np

def task1():
    size = 10
    numbers = np.random.randint(0, 11, size)

    print(f'Исходный массив: {numbers}')
    print(f'Кол-во уникальных элементов массива: {len(np.unique(numbers))}')

# Задача 2. Создайте двумерный массив размером 5х5. Определите, есть ли в нём одинаковые строки
def task2():
    size = (5, 5)
    numbers = np.random.randint(1, 5, size)
    axis = 1
    count_axis = 0
    print(numbers)

    result = np.corrcoef(numbers)
    for i in range(len(result)):
        if list(result[i]).count(1.) > 1:
            count_axis+=1
    if count_axis >= 1:
        print("В массиве есть одинаковые строки")
    else:
        print("В массиве нет одинаковых строк")

# Задача 3. Создайте двумерный массив случайного размера.
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива

def get_index_of_min(numbers, min, min_indexes_column):
    for i in range(len(numbers)):
        for j in min_indexes_column:
            if numbers[i][j] == min:
                print(f'Индекс элемента {min}: [{i}][{j}]')
                return
            elif numbers[j][i] == min:
                print(f'Индекс элемента {min}: [{j}][{i}]')
                return

def get_index_of_max(numbers, max, max_indexes_column):
    for i in range(len(numbers)):
        for j in max_indexes_column:
            if numbers[i][j] == max:
                print(f'Индекс элемента {max}: [{i}][{j}]')
                return
            elif numbers[j][i] == max:
                print(f'Индекс элемента {max}: [{j}][{i}]')
                return

def task3():
    size = (5, 5)
    numbers = np.random.randint(1, 101, size)
    print(numbers)

    maxx = max(numbers.max(0))
    minn = min(numbers.min(0))

    min_indexes_column = np.unique(numbers.argmin(0))
    max_indexes_column = np.unique(numbers.argmax(0))

    print(f'Максимум: {maxx}')
    print(f'Минимум: {minn}')
    get_index_of_max(numbers, maxx, max_indexes_column)
    get_index_of_min(numbers, minn, min_indexes_column)

    print(f'Элементы главной диагонали: {numbers.diagonal()}')

task3()