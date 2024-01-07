def get_student_interests_and_surname_length(student_data):
    interests = set()
    surname_len = 0

    for student in student_data.values():
        if 'interests' in student:
            interests.update(student['interests'])
        if 'surname' in student:
            surname_len += len(student['surname'])

    return interests, surname_len


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

for student_id in students.keys():
    print(student_id, students[student_id]["name"])

interests, length = get_student_interests_and_surname_length(students)

print("Длина всех фамилий: {0}\nСписок интересов студентов: {1}".format(length, ", ".join(interests)))

# Следующая задача #

def check_prime(number):
	divider_count = 0
	if number == 1 or number == 0:
		return False

	for divider in range(2, round(number**0.5+1)):
		if number % divider == 0:
			return False

	return True


def extract_prime_indexed_elements(sequence):
	result = []
	for index, item in enumerate(sequence):
		if check_prime(index):
			result.append(item)

	return result


print(extract_prime_indexed_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(extract_prime_indexed_elements('О Дивный Новый мир!'))

# Следующая задача #

players = {
	("Ivan", "Volkin"): (10, 5, 13),
	("Bob", "Robbin"): (7, 5, 14),
	("Rob", "Bobbin"): (12, 8, 2)
}
result = []

for key, value in players.items():
	result.append(key + value)
print(result)

# Следующая задача #

import random

original_list = [random.randint(1, 10) for _ in range(10)]
print(original_list)

new_list = []
for x in range(0, 10, 2):
	new_list.append(tuple([original_list[x], original_list[x+1]]))

print(new_list)


new_list = [tuple([original_list[x], original_list[x+1]]) for x in range(0, 10, 2)]
print(new_list)

# Следующая задача #

def tpl_sort(tpl_for_sort):
	lst = list(tpl_for_sort)
	c = 0
	k = 1
	sz = len(lst)
	while True:
		c = 0
		for i in range(sz - k):
			if lst[i] > lst[i + 1]:
				lst[i], lst[i + 1] = lst[i + 1], lst[i]
				c += 1
		if c == 0:
			return tuple(lst)
		k += 1


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))

# Следующая задача #

contacts = {}

while True:
	action = input("Введите номер действия \n(1)Добавить контакт \n(2) Найти человека): ").lower()

	if action == "1":
		name, surname = input("Введите имя и фамилию нового контакта (через пробел): ").split()
		phone = input("Введите номер телефона: ")
		if (name, surname) in contacts:
			print("Такой человек уже есть в контактах.")
		else:
			contacts[(name, surname)] = phone
			print("Текущий словарь контактов:", contacts)

	elif action == "2":
		surname_to_find = input("Введите фамилию для поиска: ").capitalize()
		found_contacts = {f"{name} {surname}": phone for (name, surname), phone in contacts.items() if
						  surname.lower() == surname_to_find.lower()}
		if found_contacts:
			for contact, phone in found_contacts.items():
				print(contact, phone)
		else:
			print("Контакт с такой фамилией не найден.")

	else:
		print("Некорректное действие. Попробуйте снова.")

# Следующая задача #

def myzip(a, b):
	return ((a[i], b[i]) for i in range(min(len(a), len(b))))


e = "abcd"
b = (10, 20, 30, 40)
g = myzip(e, b)

print(g)
print(*g, sep='\n')