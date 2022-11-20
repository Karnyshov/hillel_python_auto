"""
У вас есть Market.
Хочу что бы ваш Market давал мне необходимый товар по приметам.
Market класс должен содержать метод возвращающий товар.
Соответственно могут быть следующие товары: Apple, Banana, Cellery, Strawbarry.
Каждый из этих продуктов имеет общего родителя Product который абстрактный класс. (фабричный метод)
"""
from abc import abstractmethod, ABC


class Product(ABC):

    @abstractmethod
    def cooking_type(self):
        ...
