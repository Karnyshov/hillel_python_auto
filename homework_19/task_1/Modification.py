"""
Опишите класс Car и класс Modification.
Хочу использовать модификации как декоратор для класса.
В классе Car должен быть интерфейс который позволяет вернуть все модификации машины.
"""


class Modification:
    def __init__(self, name: str):
        self.__name = name

    def __call__(self, class_obj):
        setattr(class_obj, f"_{class_obj.__name__}_modification", self.__name)
        return class_obj
