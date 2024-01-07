file_name = "people.txt"
log_file_name = "errors.log"

names_length = 0
line_number = 0

error_log = []

try:
	with open(file_name, "r", encoding="utf-8") as people_file:
		for i_line in people_file:
			line_number += 1

			if i_line.endswith("\n"):
				i_line = i_line.strip()

			if len(i_line) >= 3:
				names_length += len(i_line)
			else:
				names_length += len(i_line)
				error_message = ("Ошибка: менее трёх символов в строке {}.".format(line_number))

				raise ValueError(error_message)

except FileNotFoundError:
	print("Такого файла не существует")
finally:
	with open(log_file_name, "w", encoding="windows-1251") as error_file:
		error_file.write("\n".join(error_log))
	print("Общее количество символов: {}".format(names_length))

# Следующая задача #

import random

try:
    file_name = 'out_file.txt'
    user_numbers = []

    with open(file_name, 'w') as file:
        file.write("")

    while True:
        user_input = int(input('Введите число: '))
        user_numbers.append(user_input)

        if sum(user_numbers) >= 777:
            break

        if random.randint(1, 13) == 1:
            raise Exception('Вас постигла неудача!')

    print('Вы успешно выполнили условие для выхода из порочного цикла!')

except Exception as e:
    raise

finally:
    with open(file_name, 'r') as file:
        file.write("\n".join(map(str, user_numbers)))
        print('\nСодержимое файла out_file.txt:')
        print(file.read())

# Следующая задача #

def validate_registration(registration):
    fields = registration.split()
    if len(fields) != 3:
        raise IndexError('НЕ присутствуют все три поля')

    name = fields[0]
    email = fields[1]
    age = fields[2]

    if not name.isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')

    if '@' not in email or '.' not in email:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и точку')

    try:
        age = int(age)
        if age < 10 or age > 99:
            raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')
    except ValueError:
        raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')


with open('registrations.txt', 'r', encoding="utf-8") as file:
    good_log = open('registrations_good.log', 'a', encoding="utf-8")
    bad_log = open('registrations_bad.log', 'a', encoding="utf-8")

    for line in file:
        try:
            validate_registration(line)
            good_log.write(line)
        except (IndexError, NameError, SyntaxError, ValueError) as e:
            bad_log.write(f'{line.rstrip()}        {e}\n')

    good_log.close()
    bad_log.close()

# Следующая задача #

import os

while True:
	try:
		username = input("Введите ваше имя или никнейм: ")
		if username.isalpha():
			break
		else:
			raise ValueError
	except ValueError:
		print("Неправильный ввод! Пожалуйста, убедитесь, что вводите только буквенные символы.\n")

while True:
	print('\n1. Посмотреть текущий текст чата.'
		  '\n2. Отправить сообщение.'
		  '\n3. Выйти из чата.')
	action_choice = int(input('Выберите действие: '))
	if action_choice == 1:
		try:
			if not os.path.exists('history_chat.txt') or os.stat('history_chat.txt').st_size == 0:
				raise FileNotFoundError
			else:
				with open('history_chat.txt', 'r', encoding='utf-8') as chat_text:
					print(f'\nТекущий текст чата:\n{chat_text.read()}')
		except FileNotFoundError:
			print('--> Чат пуст. Начните общение.')
	elif action_choice == 2:
		try:
			with open('history_chat.txt', 'a', encoding='utf-8') as message_record:
				print(f'\n{username} напишите сообщение:')
				user_message = input('--> ')
				if user_message.strip() == '':
					raise ValueError
				else:
					message_record.write(f'{username}: {user_message}\n')
		except ValueError:
			print('Сообщение не может быть пустой строкой!')
	elif action_choice == 3:
		os.truncate('history_chat.txt', 0)
		break
	else:
		print('Ошибка! Выберите одно из доступных действий.')

# Следующая задача #

import math


def calculate_square_root(number):
	try:
		if number <= 0:
			raise ValueError("Из этого числа невозможно взять корень")
		result = f"Квадратный корень числа {number} равен {math.sqrt(number)}"

	except ValueError as ve:
		return f"Ошибка: {ve}"
	except Exception as e:
		return f"Произошла ошибка: {e}"
	else:

		return result


try:
	number = float(input("Введите число: "))
	result = calculate_square_root(number)
	print(result)
except ValueError:
	print("Вы ввели неправильные данные")