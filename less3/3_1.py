# Создать декоратор с аргументами. Который будет вызывать функцию,
# определенное кол-во раз, будет выводить кол-во времени
# затраченного на выполнение данной функции и её название.


from datetime import datetime


def decorator(func):
    def wrapper(*args, **kwargs):
        for i in range(1, 11):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(f"The function '{func.__name__}' runs -{i}- times, result = {result}")
            print(f"It takes {datetime.now() - start}")
    return wrapper


@decorator
def exponent(a, b):
    return a**b


ex = exponent(2, 3)

