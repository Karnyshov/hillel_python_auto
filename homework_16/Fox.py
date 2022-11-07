"""
Опишите любую хорошо известную вам тему в виде классов.
Хочу видеть абстракцию и полиморфизм в обязательном порядке все остальные постулаты по желанию.
"""

from homework_16.Animal import Animal


class Fox(Animal):
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def ration(self) -> str:
        return "I eat meat!"

    def movement_type(self) -> str:
        return "I crawl!"


class YoungFox(Fox):
    def __init__(self, name, age):
        super().__init__(name, age)

    def ration(self) -> str:
        return "I eat meat and milk!"


fox = Fox("Finch", 4)
print(fox.ration())
print(fox.movement_type())

baby_fox = YoungFox("Jane", 1)
print(baby_fox.ration())
print(baby_fox.movement_type())
