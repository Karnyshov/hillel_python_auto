"""
Реализовать декоратор который замеряет время выполнения функции и выводит в консоль после того как функция отработала.
Для замера можете использовать скажем функцию которая перебирает в цикле 10к значений
и возвращает список из их квадратов.
"""

import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        result = function(*args)
        end_time = time.perf_counter() - start_time
        return f"{result}\n{end_time}"
    return wrapped


@time_of_function
def squares():
    return [x**2 for x in range(100000)]


print(squares())
