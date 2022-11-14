"""
Опишите класс Car и класс Modification.
Хочу использовать модификации как декоратор для класса.
В классе Car должен быть интерфейс который позволяет вернуть все модификации машины.
"""

from homework_19.task_1.Modification import Modification


@Modification("EV")
class Car:
    def __init__(self, doors: int, color: str) -> None:
        self._doors = doors
        self._color = color

    def __key(self, key):
        return key.replace(f"{self.__class__.__name__}", "")

    def __str__(self):
        result = ""
        for key, value in self.__dict__.items():
            result += f"{self.__key(key)}: {value}\n"
        return result


toyota = Car(4, "red")
print(toyota)
