import time


class LoggerDecorator:
	def __init__(self, func):
		self.func = func

	def __call__(self, *args, **kwargs):
		start_time = time.time()
		arguments = ", ".join([repr(a) for a in args])
		result = self.func(*args, **kwargs)
		end_time = time.time()
		execution_time = end_time - start_time

		print(f"Вызов функции {self.func.__name__}")
		print(f"Аргументы: ({arguments}), {kwargs}")
		print(f"Результат: {result}")
		print(f"Время выполнения: {execution_time:.10f} секунд")

		return result


@LoggerDecorator
def complex_algorithm(arg1, arg2):
	# Здесь выполняется “сложный” алгоритм
	result = 0
	for i in range(arg1):
		for j in range(arg2):
			with open('test.txt', 'w', encoding='utf8') as file:
				file.write(str(i + j))
				result += i + j
	# Можете попробовать вынести создание файла из циклов и проверить, сколько времени алгоритм будет работать в этом
	# случае
	return result


result = complex_algorithm(10, 50)