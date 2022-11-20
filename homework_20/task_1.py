"""
Описать объект на ваше усмотрение.
Экземпляр объекта может быть лишь один в системе.
Хочу увидеть паттерн синглтон но статическое поле инстанс хочу видеть приватным.
"""


class PC:
    __instance = None
    _ram = None

    @property
    def ram(self) -> int:
        return self._ram

    @ram.setter
    def ram(self, ram: int):
        self._ram = ram

    def __new__(cls):
        if not hasattr(cls, "__instance"):
            cls.__instance = cls
        return cls.__instance


pc1 = PC()
pc2 = PC()

pc1.ram = 4

print(pc1)
print(pc2)
print(pc1.ram)
print(pc2.ram)
print(pc1 == pc2)
