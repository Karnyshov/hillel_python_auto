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


def test_index_error(range_len: int):
    lst = [1, 2, 3, 4, 5]
    for x in range(range_len):
        try:
            lst.append(x)
            if len(lst) > 10:
                raise IndexError("List cannot be greater than 10")
        except IndexError as error:
            print(error)
            lst.pop(-1)
            return lst
    return lst


print(test_index_error(7))
