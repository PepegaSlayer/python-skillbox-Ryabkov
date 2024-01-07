import random


# Определение пользовательских исключений
class KillError(Exception):
	pass


class DrunkError(Exception):
	pass


class CarCrashError(Exception):
	pass


class GluttonyError(Exception):
	pass


class DepressionError(Exception):
	pass


def one_day():
	karma = random.randint(1, 7)
	if random.randint(1, 10) == 1:
		raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
	return karma


# Открываем файл для записи лога
with open("karma.log", "w") as log_file:
	karma_total = 0
	# Бесконечный цикл для набора кармы
	while True:
		try:
			current_karma = one_day()
			karma_total += current_karma
			log_file.write(f"Добленное сегодня значение кармы: {current_karma}. Общее значение кармы: {karma_total}.\n")
			if karma_total >= 500:
				break
		except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
			log_file.write(f"Exception: {e.__class__.__name__}. Общее значение кармы: {karma_total}.\n")

# По завершении работы закрываем файл