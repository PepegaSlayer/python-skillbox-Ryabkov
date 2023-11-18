print('Задача 1. Кубы чисел')

n = int(input("Введите число N: "))
cube = 1
while cube <= N:
    print(cube ** 3)
    cube += 1

print('Задача 2. Коллекторы')

name = input("Введите имя: ")
credit = int(input("Введите сумму задолженности: "))
money = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
while money < credit:
    print("Маловато,", name, ". Давайте ещё раз.")
    money = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
print("Отлично, ", name, "! Вы погасили долг. Спасибо!")

print('Задача 3. Слишком большие числа')

count = 0
number = int(input("Введите число: "))
if number == 0:
    count = 1
while number != 0:
    count += 1
    number //= 10
print(count)

print('Задача 4. Поставьте оценку!')

new_review = 1
bad_review = 0
good_review = 0
while new_review != 0:
    estimation = int(input("Введите число: "))
    if new_review > 0:
      good_review += 1
    elif new_review < 0:
      bad_review += 1
print("Кол-во положительных чисел:", good_review)
print("Кол-во отрицательных чисел:", bad_review)

print('Задача 5. Обычный день на работе')

hours = 1
count_task = 0
shop = 0
while hours <= 8:
    print(hours, " час")
    count_task += int(input("Сколько задач решит Максим? "))

    shop += int(input("Звонит жена. Взять трубку? (1-да, 0-нет) "))
    hours += 1
print("Рабочий день закончился. Всего выполнено задач:", count_task)
if shop > 0:
    print("Нужно зайти в магазин")

print('Задача 6. Вклады')

X = int(input("Введите величину вклада: "))
P = int(input("Введите процентную ставку: "))
Y = int(input("Какая сумма необходима? "))
years = 0
while X < Y:
    X += X * (P / 100)
    years += 1
    X //= 1
print("Сумма ", Y," рублей достигнет через ", years, " лет")

print('Задача 7. Игра «Угадай число»')

import random
answer = random.randint(0, 11)
user_answer = 1
count = 0
while answer != user_answer:
    count += 1
    user_answer = int(input("Введите число: "))
    if user_answer < answer:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif user_answer > answer:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
print("Вы угадали! Число попыток:", count)

print('Задача 8. Игра «Компьютер угадывает число»')

attempts = 0
left = 1
right = 100

while True:
    attempts += 1
    mid = (left + right) // 2

    answer = int(
        input(f"Твое число равно, меньше или больше, чем число {mid}? (1 - равно, 2 - больше, 3 - меньше): "))

    if answer == 1:
        print(f"Для угадывания числа потрачено {attempts} попыток!")
        break
    elif answer == 2:
        left = mid + 1
    elif answer == 3:
        right = mid - 1

