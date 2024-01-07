class Unit:
    def __init__(self, name, health, attack_strength):
        self.name = name
        self.health = health
        self.attack_strength = attack_strength

    def attack(self, opponent):
        opponent.health -= self.attack_strength
        print(f"{self.name} атаковал {opponent.name}, уронив его на {opponent.health} здоровья")

    def defend(self):
        if self.health > 0:
            print(f"{self.name} отразил атаку, его здоровье: {self.health}")
        else:
            print(f"{self.name} уничтожен")

    def is_alive(self):
        return self.health > 0

def battle(unit1, unit2):
    while unit1.is_alive() and unit2.is_alive():
        random.choice([unit1, unit2]).attack(random.choice([unit1, unit2]))

    if unit1.is_alive():
        print(f"Победил {unit1.name}")
    elif unit2.is_alive():
        print(f"Победил {unit2.name}")
    else:
        print("Ничья")

def create_students():
    return [
        Unit("Миша", 50, 5),
        Unit("Лена", 60, 6),
        Unit("Леша", 45, 4),
        Unit("Егор", 55, 5),
        Unit("Олег", 55, 5),
        Unit("Женя", 45, 4),
        Unit("Сережа", 40, 4),
        Unit("Сеня", 40, 4),
        Unit("Степа", 40, 4),
        Unit("Илья", 35, 3),
    ]

def sort_students(students):
    students.sort(key=lambda x: x.health, reverse=True)
    return students

def print_students(students):
    for i in students:
        print(f"{i.name}, средняя оценка: {i.health}, атака: {i.attack_strength}")

def main():
    random.seed(1)
    students = create_students()
    sorted_students = sort_students(students)
    print_students(sorted_students)

    for i in range(len(sorted_students) - 1):
        battle(sorted_students[i], sorted_students[i + 1])

if __name__ == "__main__":
    main()