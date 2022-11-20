"""
У вас есть Market.
Хочу что бы ваш Market давал мне необходимый товар по приметам.
Market класс должен содержать метод возвращающий товар.
Соответственно могут быть следующие товары: Apple, Banana, Cellery, Strawbarry.
Каждый из этих продуктов имеет общего родителя Product который абстрактный класс. (фабричный метод)
"""
from homework_20.task_2.Products import *


class Market:
    @staticmethod
    def get_product(name: str):
        if name == "Apple":
            return Apple()
        elif name == "Banana":
            return Banana()
        elif name == "Celery":
            return Celery()
        elif name == "Strawberry":
            return Strawberry()
        else:
            raise Exception("Unsupported product")


apple = Market.get_product("Apple")
print(apple.cooking_type())
