print('Задача 1. Датчик погоды')

state = int(input("На улице идёт дождь?"))
if state == 1:
    print("Пошёл дождь. Возьмите зонтик!")
else:
    print("Дождя нет!")

print('Задача 2. Поступление')

russian = int(input("Введите количество баллов по русскому языку: "))
math = int(input("Введите количество баллов по математике: "))
informatics = int(input("Введите количество баллов по информатике: "))

total_score = russian + math + informatics
if total_score >= 270:
    print("Поздравляю, ты поступил на бюджет!")
else:
    print("К сожалению, ты не прошёл на бюджет.")

print('Задача 3. Следим за расписанием')

day = input('Введите число: ')
if day % 2 == 0:
    print('Число чётное')
else:
    print('Число нечётное')

print('Задача 4. Калькулятор скидки')

sum = int(input("Введите стоймость первого товара: "))
sum += int(input("Введите стоймость второго товара: "))
sum += int(input("Введите стоймость третьего товара: "))

if sum > 10000:
    sum -= sum * 0.1

print(f"Итоговая сумма: {sum}")

print('Задача 5. Модуль числа')

num = int(input())
if num < 0:
    num = -num
print(num)

print('Задача 6. Игра в кубики')

guest_score = int(input("Кубик Кости: "))
owner_score = int(input("Кубик владельца: "))
if guest_score >= owner_score:
    print("Разность: ", guest_score - owner_score)
    print("Игрок платит")
else:
  print("Сумма: ", guest_score + owner_score)
  print("Владелец платит")

print('Задача 7. Хватит ли зарплаты')

hours = int(input("Введите отработанные часы: "))
credit = int(input("Введите остаток по кредиту: "))
food = int(input("Введите траты на еду: "))
salary = 200 * hours / 2 ** 3 + hours
if salary >= credit + food:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать больше!")

print('Задача 8. Максимальное число (по желанию)')

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 > num2 and num1 > num3:
    print("Максимальное число:", num1)
elif num2 > num3:
    print("Максимальное число:", num2)
else:
    print("Максимальное число:", num3)

