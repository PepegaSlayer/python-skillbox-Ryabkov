import time


def delay_execution(seconds):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			time.sleep(seconds) # Ждем заданное количество секунд
			return func(*args, **kwargs)

		return wrapper

	return decorator


def some_function():
	print('Выполнение функции с задержкой...')


delayed_some_function = delay_execution(3)(some_function)


delayed_some_function()