from __future__ import annotations


# from abc import ABC, abstractmethod
# class Warrior(ABC):
class Warrior:
    DAMAGE_PER_HIT = 20
    __hp = 100

    def __init__(self, name):
        self.__name = name
        # self.__hp = self.HP_INIT

    def __del__(self):
        print('Goodbye, warrior', self.get_name())

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def show_hp(self):
        print('Warrior', self.get_name(), 'has', self.get_hp(), 'hp left')

    def decrease_hp(self, amount):
        self.__hp -= amount

    def hits(self, whom: Warrior) -> bool:
        print(self.__name, "hits", whom.get_name())
        whom.decrease_hp(self.DAMAGE_PER_HIT)
        whom.show_hp()
        return True
