import time
import functools
import logging
import datetime


def delay_execution(seconds):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			time.sleep(seconds) # Ждем заданное количество секунд
			return func(*args, **kwargs)

		return wrapper

	return decorator


def logging_decorator(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		try:
			print(f'Вызов функции: {func.__name__}')
			print(f'Документация функции: {func.__doc__}')
			return func(*args, **kwargs)
		except Exception as e:
			error_msg = f'Ошибка в функции {func.__name__}: {str(e)}\n'
			with open('function_errors.log', 'a', encoding="utf-8") as file:
				file.write(f'{datetime.datetime.now()}: {error_msg}')
			print(error_msg)

	return wrapper


@logging_decorator
@delay_execution(3)
def some_function():
	"""
    Это документация для функции some_function.
    """
	print('Выполнение функции с задержкой...')


@logging_decorator
@delay_execution(3)
def another_function():
	"""
    Это документация для функции another_function.
    """
	print(1 / 0) # Генерируем ошибку деления на ноль


some_function()
another_function()