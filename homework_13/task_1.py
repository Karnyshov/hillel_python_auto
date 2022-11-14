"""
Describe class Zoo.
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
        self._area = int(area)
        self._visitors = int(visitors)
        self._animals = int(animals)
        self._price = int(price)

    def add_animal(self):
        self._animals += 1

    @classmethod
    def get_penguin_family(cls):
        return cls.penguin_family

    @property
    def area(self):
        return self._area

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

    @area.setter
    def area(self, area: int):
        assert type(area) == int, "Area should be integer"
        assert area >= 0, "Area cannot be less 0"
        self._area = area

    @address.setter
    def address(self, address):
        assert type(address) == str, "Address should be a string"
        assert len(address) > 0, "Address cannot be empty"
        self._address = address

    @visitors.setter
    def visitors(self, visitors: int):
        assert type(visitors) == int, "Visitors should be integer"
        assert visitors >= 0, "Visitors cannot be less 0"
        self._visitors = visitors

    @animals.setter
    def animals(self, animals: int):
        assert type(animals) == int, "Animals should be integer"
        assert animals >= 0, "Animals cannot be less 0"
        self._animals = animals

    @price.setter
    def price(self, price: int):
        assert type(price) == int, "Price should be integer"
        assert price >= 0, "Price cannot be less 0"
        self._price = price


zoo = Zoo("Street", 5, 200, 50, 25)

zoo.animals = 51
print(zoo.animals)

zoo.add_animal()
print(zoo.animals)

print(Zoo.get_penguin_family())
