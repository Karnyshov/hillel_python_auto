"""
Есть список из элементов [1, 2, 3, 4, 5].
Реализовать логику которая будет возбуждать ошибку если у нас есть уже 10 элементов в списке
и мы пытаемся добавить еще одного.
"""


def test_error():
    lst = [1, 2, 3, 4, 5]

    for x in range(7):
        if len(lst) > 10:
            raise Exception("List cannot be greater than 10")
        lst.append(x)
        print(lst)

    return lst


test_error()
