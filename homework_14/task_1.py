"""
Описать классы Dog и Mastif (хочу видеть наследование, сокрытие и инкапсуляцию).
"""


class Dog:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self.__bark = "BARK!"
    
    @property
    def barking(self) -> str:
        return self.__bark


class Mastiff(Dog):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)


dog = Mastiff("Bob", 4)
print(dog.barking)
