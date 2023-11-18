print('Задача 1. Калькулятор опыта')

exp_points = int(input("Введите количество опыта: "))

if exp_points >= 5000:
    print("Ваш уровень: 4")
elif exp_points >= 2500:
    print("Ваш уровень: 3")
elif exp_points >= 1000:
    print("Ваш уровень: 2")
else:
    print("Ваш уровень: 1")

print('Задача 2. Функция')

X = int(input("Введите икс: "))
if X > 0:
    Y = X - 12
elif X == 0:
    Y = 5
else:
    Y = X ** 2

print("Игрек равен", Y)

print('Задача 3. Поступление')

place = int(input("Введите место в списке поступающих: "))
score = int(input("Введите количество баллов за экзамены: "))

if place <= 10:
    print("Поздравляем, Вы поступили!")
    if score >= 290:
        print("Бонусом Вам будет начисляться стипендия")
    else:
        print("Но Вам не хватило баллов для стипендии")
else:
    print("К сожалению, вы не поступили.")

print('Задача 4. Опять двойка')

rating = int(input('Что получил по математике? '))
if rating == 2 or rating == 3:
    print('Плохо. Марш учиться!')
elif rating == 4 or rating == 5:
    print('Молодец! Можешь отдохнуть.')

print('Задача 5. Вася хочет выигрывать')

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))

if number1 == number2 == number3:
    print(3)
elif number1 == number2 or number2 == number3 or number1 == number3:
    print(2)
else:
    print(0)

print('Задача 6. Новоселье')

cost = float(input("Введите стоимость квартиры в миллионах: "))
area = float(input("Введите площадь квартиры: "))

if area >= 100 and cost <= 10:
  print("Квартира подходит по первому варианту")
elif area >= 80 and cost <= 7:
  print("Квартира подходит по второму варианту")
else:
  print("К сожалению, квартира не подходит ни по одному из вариантов")

print('Задача 7. Почта')

hour = int(input("Введите время в часах (число от 0 до 23): "))

if (8 <= hour < 10) or (12 <= hour < 14) or (15 <= hour < 18) or (20 <= hour < 22):
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")

if (10 <= hour < 12) or (14 <= hour < 15) or (18 <= hour < 20) or (hour < 8) or (hour >= 22):
    print("Посылку получить нельзя")
else:
    print("Можно получить посылку")



