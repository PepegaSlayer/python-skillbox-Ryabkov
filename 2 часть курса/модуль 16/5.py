def singleton(cls):
	"""Декоратор-определитель инициализации экземпляра класса."""

	def inner():
		if cls.__copy is None:
			cls.__copy = cls()
		return cls.__copy

	cls.__copy = None
	return inner


@singleton
class Example:
	pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)