import random


class Human:
	def __init__(self, name, house):
		self.name = name
		self.satiety = 50
		self.house = house

	def eat(self):
		self.satiety += 10
		self.house.food -= 10

	def work(self):
		self.satiety -= 10
		self.house.money += 50

	def play(self):
		self.satiety -= 20

	def go_shopping(self):
		self.house.food += 50
		self.house.money -= 50

	def live_day(self):
		dice = random.randint(1, 6)
		if self.satiety < 20:
			self.eat()
		elif self.house.food < 10:
			self.go_shopping()
		elif self.house.money < 50:
			self.work()
		elif dice == 1:
			self.work()
		elif dice == 2:
			self.eat()
		else:
			self.play()


class House:
	def __init__(self):
		self.food = 50
		self.money = 0


house = House()
person1 = Human("Alice", house)
person2 = Human("Bob", house)

for day in range(365):
	person1.live_day()
	person2.live_day()

print(f"{person1.name}'s final satiety: {person1.satiety}")
print(f"{person2.name}'s final satiety: {person2.satiety}")
print(f"Food left in the house: {house.food}")
print(f"Money left in the house: {house.money}")