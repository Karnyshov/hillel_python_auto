"""
Опишите класс Car и класс Modification.
Хочу использовать модификации как декоратор для класса.
В классе Car должен быть интерфейс который позволяет вернуть все модификации машины.
"""
from homework_19.task_1.Modification import Modification


@Modification("EV")
class Car:
    def __init__(self, doors: int, color: str):
        self._doors = doors
        self._color = color


car = Car(4, "red")
# setattr(car, "_mod", "EV")

print(vars(car))
