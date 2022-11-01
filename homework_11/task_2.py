"""
Создайте функцию которая способна вернуть квадраты четных элементов для диапазона от 0 до 1000000000 включительно.
Решение должно отрабатывать и не фризить ваш комп.
"""


def square_item(length: int):
    squared = []
    counter = 0

    while counter < length:
        if counter % 2 == 0:
            squared.append(counter ** 2)
            yield squared
        counter += 1

    return squared


generator = square_item(1000000000)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
