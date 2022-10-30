"""
Реализовать декоратор который замеряет время выполнения функции и выводит в консоль после того как функция отработала.
Для замера можете использовать скажем функцию которая перебирает в цикле 10к значений
и возвращает список из их квадратов.
"""

import time


def time_of_function(function):
    def wrapped():
        start_time = time.perf_counter()
        result = function()
        end_time = time.perf_counter() - start_time
        print(end_time)
        return result
    return wrapped


@time_of_function
def squares():
    return [x**2 for x in range(100000)]


squares()
