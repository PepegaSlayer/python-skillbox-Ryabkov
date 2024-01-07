class Element:
	def __init__(self, name):
		self.name = name

	def __add__(self, other):
		if isinstance(other, Element):
			if self.name == "Вода" and other.name == "Воздух" or self.name == "Воздух" and other.name == "Вода":
				return Storm()
			elif self.name == "Вода" and other.name == "Огонь" or self.name == "Огонь" and other.name == "Вода":
				return Steam()
			elif self.name == "Вода" and other.name == "Земля" or self.name == "Земля" and other.name == "Вода":
				return Mud()
			elif self.name == "Воздух" and other.name == "Огонь" or self.name == "Огонь" and other.name == "Воздух":
				return Lightning()
			elif self.name == "Воздух" and other.name == "Земля" or self.name == "Земля" and other.name == "Воздух":
				return Dust()
			elif self.name == "Огонь" and other.name == "Земля" or self.name == "Земля" and other.name == "Огонь":
				return Lava()
			else:
				return None
		else:
			return None


class Water(Element):
	def __init__(self):
		super().__init__("Вода")


class Air(Element):
	def __init__(self):
		super().__init__("Воздух")


class Fire(Element):
	def __init__(self):
		super().__init__("Огонь")


class Earth(Element):
	def __init__(self):
		super().__init__("Земля")


class Storm(Element):
	def __init__(self):
		super().__init__("Шторм")


class Steam(Element):
	def __init__(self):
		super().__init__("Пар")


class Mud(Element):
	def __init__(self):
		super().__init__("Грязь")


class Lightning(Element):
	def __init__(self):
		super().__init__("Молния")


class Dust(Element):
	def __init__(self):
		super().__init__("Пыль")


class Lava(Element):
	def __init__(self):
		super().__init__("Лава")


# Примеры использования
water = Water()
air = Air()
result = water + air
print(result.name)  # Шторм

fire = Fire()
earth = Earth()
result = fire + earth
print(result.name)  # Лава

water = Water()
fire = Fire()
result = water + fire
print(result.name)  # Пар

air = Air()
earth = Earth()
result = air + earth
print(result.name)  # Пыль