import random


class Unit:
    def __init__(self, hp, name):
        self.hp = hp
        self.name = name

    def info(self):
        print("Оставшееся здоровье {}: {}".format(self.name, self.hp))

    def take_damage(self):
        self.hp -= 20
        self.info()


unit1 = Unit(100, "Воин 1")
unit2 = Unit(100, "Воин 2")
while unit1.hp > 0 and unit2.hp > 0:
    attacking_unit = random.choice([unit1, unit2])
    attacked_unit = random.choice([unit1, unit2])
    print("Атакует {}:".format(attacking_unit.name))
    attacked_unit.take_damage()
    if attacked_unit.hp <= 0:
        break

if unit1.hp > unit2.hp:
    print("Победу одержал {0}".format(unit1.name))
elif unit1.hp < unit2.hp:
    print("Победу одержал {0}".format(unit2.name))
else:
    print("Ничья")