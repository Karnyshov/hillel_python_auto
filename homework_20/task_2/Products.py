"""
У вас есть Market.
Хочу что бы ваш Market давал мне необходимый товар по приметам.
Market класс должен содержать метод возвращающий товар.
Соответственно могут быть следующие товары: Apple, Banana, Celery, Strawberry.
Каждый из этих продуктов имеет общего родителя Product который абстрактный класс. (фабричный метод)
"""
from homework_20.task_2.Product import Product


class Celery(Product):

    _name = "Celery"
    _color = "White"
    _taste = "Bitter"

    def cooking_type(self) -> str:
        return "Chop"


class Apple(Product):

    _name = "Apple"
    _color = "Green"
    _taste = "Sweet"

    def cooking_type(self) -> str:
        return "Slice"


class Banana(Product):
    _name = "Banana"
    _color = "Yellow"
    _taste = "Sweet"

    def cooking_type(self) -> str:
        return "Slice"


class Strawberry(Product):
    _name = "Strawberry"
    _color = "Red"
    _taste = "Sweet"

    def cooking_type(self) -> str:
        return "Wash & Eat"
