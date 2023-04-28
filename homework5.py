import re
# Задайте список случайных чисел от 1 до 10
# Выведите все элементы больше 5, используя лямбда-функцию
def task1():
    from random import randint
    lst = [randint(0, 10) for _ in range(10)]
    print(f"Исходный список: {lst}")
    lst = list(filter(lambda x: x > 5, lst))
    print(f"Список с элементами больше 5: {lst}")

# Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность
# Порядок элементов менять нельзя
def get_sequences(lst: list):
    seq = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[i]:
                subseq = [lst[i], lst[j]]
                if subseq not in seq:
                    seq.append(subseq)
    print(seq)

def task2():
    from random import randint
    lst = [randint(0, 10) for _ in range(10)]
    print(f"Исходный список: {lst}")
    print(f"Всевозможные возрастающие последовательности из двух элементов")
    get_sequences(lst)

# Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке
# Удалите все повторяющиеся элементы
def task3():
    from random import randint
    lst = [randint(0, 10) for _ in range(10)]
    print(f"Исходный список: {lst}")
    modified_lst = list(filter(lambda x: lst.count(x) == 1, lst))
    duplicate = len(lst) - len(modified_lst)
    print(f"Кол-во повторяющихся значений: {duplicate}")
    if duplicate > 0:
        print(f"Список уникальных элементов: {list(set(lst))}")

# Создайте игру в крестики-нолики

def draw_field(field_data):
    print()
    print(f"    0     1     2")
    print(f"0   {field_data[0][0]}  |  {field_data[0][1]}  |  {field_data[0][2]}")
    print(f'  - {"- " * 2}- {"- " * 2}- {"- " * 2}')
    print(f"1   {field_data[1][0]}  |  {field_data[1][1]}  |  {field_data[1][2]}")
    print(f'  - {"- " * 2}- {"- " * 2}- {"- " * 2}')
    print(f"2   {field_data[2][0]}  |  {field_data[2][1]}  |  {field_data[2][2]}")
    print()

def is_win(field_data):
    for i in range(3):
        if field_data[i][0] == field_data[i][1] == field_data[i][2] == "X":
            return True
        elif field_data[0][i] == field_data[1][i] == field_data[2][i] == "X":
            return True
        elif field_data[i][0] == field_data[i][1] == field_data[i][2] == "O":
            return True
        elif field_data[0][i] == field_data[1][i] == field_data[2][i] == "O":
            return True
    else:
        if field_data[0][0] == field_data[1][1] == field_data[2][2] == "X":
            return True
        elif field_data[2][0] == field_data[1][1] == field_data[0][2] == "X":
            return True
        elif field_data[0][0] == field_data[1][1] == field_data[2][2] == "O":
            return True
        elif field_data[2][0] == field_data[1][1] == field_data[0][2] == "O":
            return True
    return False

def is_draw(field_data):
    count = 0
    for i in range(3):
        for j in range(3):
            if not re.match(r"[XO]", field_data[i][j]):
                count += 1
    if count == 0:
        return True
    else:
        return False

def change_player(current_player):
    if current_player == 1:
        return 2
    else:
        return 1
    
def change_chip(player_chip):
    if player_chip == "X":
        return "O"
    else:
        return "X"

def move_player(current_player, player_chip, field_data):
    while True:
        move = input(f'Ходит {current_player} игрок. Вы ходите "{player_chip}". Укажите номер ячейки: ')
        if re.match(r"^[0-2]{2}$", move):
            if re.match(r"^\s$", field_data[int(move[1])][int(move[0])]):
                field_data[int(move[1])][int(move[0])] = player_chip
                return True
            else:
                print(f'В ячейке {move} уже находится {field_data[int(move[1])][int(move[0])]}. Пожалуйста, повторите ход')
        else:
            print(f'Введено некорректное значение "{move}". Пожалуйста, повторите ход')

def task4(current_player, player_chip):
    field_data = [
        [" "," "," "], 
        [" "," "," "], 
        [" "," "," "]
    ]

    print('Игра "Крестики-нолики"')
    draw_field(field_data)
    moves_count = 1
    while not (is_win(field_data)):
        if is_draw(field_data):
            print("Ничья!")
            break
        print(f"Ход №{moves_count}")
        if moves_count != 1:
            current_player = change_player(current_player)
            player_chip = change_chip(player_chip)
        move_player(current_player, player_chip, field_data)
        draw_field(field_data)
        moves_count += 1
    else:
        print(f"Поздравляем {current_player} игрока с победой!")

# Двумерный массив размером 5х5 заполнен случайными нулями и единицами 
# Игрок может ходить только по полям, заполненным единицами
# Проверьте, существует ли путь из точки [0, 0] в точку [4, 4] (эти поля требуется принудительно задать равными единице)

# Говорю по-честному: код для этой задачи не мой) Я просто пытался разобраться, как работает данный код)
from collections import deque
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def print_matrix(field_data):
    print()
    print(f" 4     {field_data[4][0]}  |  {field_data[4][1]}  |  {field_data[4][2]}  |  {field_data[4][3]}  |  {field_data[4][4]}")
    print(f'     - {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}')
    print(f" 3     {field_data[3][0]}  |  {field_data[3][1]}  |  {field_data[3][2]}  |  {field_data[3][3]}  |  {field_data[3][4]}")
    print(f'     - {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}')
    print(f" 2     {field_data[2][0]}  |  {field_data[2][1]}  |  {field_data[2][2]}  |  {field_data[2][3]}  |  {field_data[2][4]}")
    print(f'     - {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}')
    print(f" 1     {field_data[1][0]}  |  {field_data[1][1]}  |  {field_data[1][2]}  |  {field_data[1][3]}  |  {field_data[1][4]}")
    print(f'     - {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}')
    print(f" 0     {field_data[0][0]}  |  {field_data[0][1]}  |  {field_data[0][2]}  |  {field_data[0][3]}  |  {field_data[0][4]}")
    print(f'     - {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}- {"- " * 2}')
    print()
    print(f"       0     1     2     3     4")
    print()

def is_valid(mat, visited, row, col):
	return (row >= 0) and (row < len(mat)) and (col >= 0) and (col < len(mat[0])) \
		   and mat[row][col] == 1 and not visited[row][col]

def find_shortest_path_length(mat, src, dest):
	i, j = src
	x, y = dest

	if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
		return -1

	(m, n) = (len(mat), len(mat[0]))
	visited = [[False for x in range(n)] for y in range(m)]
    
	q = deque()
	visited[i][j] = True
	q.append((i, j, 0))
	min_dist = -2
        
	while q:
		(i, j, dist) = q.popleft()
		if i == x and j == y:
			min_dist = dist
			break
		for k in range(4):
			if is_valid(mat, visited, i + row[k], j + col[k]):
				visited[i + row[k]][j + col[k]] = True
				q.append((i + row[k], j + col[k], dist + 1))

	if min_dist != -2:
		return min_dist
	else:
		return -1

def task5():
    from random import randint
    field = [
        [randint(0,1) for _ in range(5)],
        [randint(0,1) for _ in range(5)],
        [randint(0,1) for _ in range(5)],
        [randint(0,1) for _ in range(5)],
        [randint(0,1) for _ in range(5)],
    ]
    field[0][0] = field[4][4] = 1
    print_matrix(field)

    src = (0, 0)
    dest = (4, 4)

    min_dist = find_shortest_path_length(field, src, dest)

    if min_dist != -1:
        print("Самый короткий путь до пункта назначения:", min_dist)
    else:
        print("Нет пути к пункту назначения")
