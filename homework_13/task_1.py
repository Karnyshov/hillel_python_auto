"""
Описать класс Zoo.
"""


class Zoo:

    penguin_family = ["Adam", "Jane"]

    def __init__(self, address: str,
                 area: int,
                 visitors: int,
                 animals: int,
                 price: int
                 ):
        self._address = address
        self._area = area
        self._visitors = visitors
        self._animals = animals
        self._price = price

    def add_animal(self):
        self._animals += 1

    @classmethod
    def get_penguin_family(cls):
        return cls.penguin_family

    @property
    def address(self):
        return self._address

    @property
    def visitors(self):
        return self._visitors

    @property
    def animals(self) -> int:
        return self._animals

    @property
    def price(self):
        return self._price

    @address.setter
    def address(self, address):
        self._address = address

    @visitors.setter
    def visitors(self, visitors: int):
        self._visitors = visitors

    @animals.setter
    def animals(self, animals: int):
        self._animals = animals

    @price.setter
    def price(self, price: int):
        self._price = price


zoo = Zoo("Street", 5, 200, 50, 25)

zoo.animals = 51
print(zoo.animals)

zoo.add_animal()
print(zoo.animals)

print(Zoo.get_penguin_family())
