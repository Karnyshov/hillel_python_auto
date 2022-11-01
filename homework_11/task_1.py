"""
Создать декоратор которые принтит в консоль имя функции которая была вызвана.
Функция при этом должна работать как и задумывалось.
К примеру создайте пару функции для арифметических операций суммирования и умножения.
При вызове этих функций должен возвращаться результат операции и предварительно выводиться в консоль имя функции которая
была вызвана.
"""


def func_name(function):
    def name(*args):
        return f"{function.__name__}\n{function(*args)}"
    return name


@func_name
def add(first: int, second: int) -> int:
    return first + second


@func_name
def subtraction(first: int, second: int) -> int:
    return first - second


print(add(2, 2))
print(subtraction(3, 2))
