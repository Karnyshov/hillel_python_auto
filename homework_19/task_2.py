"""
Создайте итератор принимающий последовательность и умеющий перебирать значения по заданному диапазону.
CustomIterator(sequence, start_index, end_index)
"""


class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self._sequence = sequence
        self._start_index = start_index
        self._end_index = end_index
        self._current = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < self._end_index:
            result = self._sequence[self._current]
            self._current += 1
            return result
        else:
            raise StopIteration


custom = CustomIterator([1, 2, 3, 4, 5, 6], 1, 3)
iterator = iter(custom)

for item in custom:
    print(item)
