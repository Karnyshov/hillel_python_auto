"""
Опишите класс Car и класс Modification.
Хочу использовать модификации как дескриптор для класса.
В классе Car должен быть интерфейс который позволяет вернуть все модификации машины.
"""


class Modification:
    def __init__(self, name=""):
        self._name = name

    def __get__(self, instance, owner):
        return self._name

    def __set__(self, instance, value):
        self._name = value


class Car:
    ev = Modification
    heater = Modification

    def __init__(self, model: str, color: str) -> None:
        self._model = model
        self._color = color

    def get_modifications(self) -> dict:
        attributes = vars(self)

        modifications = {key: values for key, values in attributes.items() if "_" not in key}
        return modifications


tesla = Car("Tesla", "Yellow")
tesla.ev = "EV"
tesla.heater = "AC"

print(tesla.get_modifications())
