"""
Опишите любую хорошо известную вам тему в виде классов.
Хочу видеть абстракцию и полиморфизм в обязательном порядке все остальные постулаты по желанию.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def ration(self):
        ...

    @abstractmethod
    def movement_type(self):
        ...



