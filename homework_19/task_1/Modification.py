"""
Опишите класс Car и класс Modification.
Хочу использовать модификации как декоратор для класса.
В классе Car должен быть интерфейс который позволяет вернуть все модификации машины.
"""


class Modification:
    def __init__(self, mod: str):
        self.mod = mod

    def __call__(self, class_obj):
        setattr(class_obj, "_mod_type", self.mod)
        return class_obj
