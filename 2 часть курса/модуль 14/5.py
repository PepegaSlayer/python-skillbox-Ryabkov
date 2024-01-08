def memoize(func):
	cache = {}

	def memoized_func(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]

	return memoized_func


@memoize
def fibonacci(n):
	"""
	Рекурсивная функция для вычисления чисел Фибоначчи.

	Args:
	- n (int): номер числа Фибоначчи

	Returns:
	- int: значение числа Фибоначчи
	"""
	if n <= 1:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)


# Пример использования
n = 100
result = fibonacci(n)
print(f"{n}-е число фибоначчи это: {result}")