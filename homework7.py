# Задача 1. Создайте пользовательский аналог метода map()
def custom_map(func, obj):
    return (func(i) for i in obj)

def task1():
    lst = [2, 3, 4, 5]
    print(list(custom_map(lambda x: x**3, lst)))

# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз
def retry(count):
    def our_repeat(func):
        def decorator(*args, **kwargs):
            for _ in range(1, count + 1):
                print(f"Попытка №{_}")
                print(func(*args, **kwargs))
        return decorator
    return our_repeat

@retry(5)
def custom_pow(num = 5, pow = 4):
    return num ** pow

custom_pow(6, 6)
