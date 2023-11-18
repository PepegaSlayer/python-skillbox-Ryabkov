print('Задача 1. Конвертация')

price = float(input('Введите стоимость покупки в евро: '))
rub = round((price * 1.25) * 60.87, 2)
if price > 0:
  print('Cтоимость покупки в рублях составила:', rub)

print('Задача 2. Грубая математика')

import math

end = int(input('Введите кол-во чисел: '))

for i in range(end):
    number = float(input('Введите число: '))
    if number > 0:
        log_x = math.ceil(number)
        print('x =', log_x, '\tlog(x) =', math.log(log_x))
    elif number < 0:
        exp_x = math.floor(number)
        print('x =', exp_x, '\texp(x) =', math.exp(exp_x))
    else:
        print('0')

print('Задача 3. Аналог Steam')

time = 1
size = int(input("Укажите размер файла для скачивания: "))
speed = int(input("Какова скорость вашего соединения? "))
download = speed
while download < size:
    percent = round(download / size, 2) * 100
    print(f"Прошло {time} сек. Скачано {download} из {size} Мб ({int(percent)}%)")
    time += 1
    download += speed
print(f"Прошло {time} сек. Скачано {size} из {size} Мб (100%)")
print(f"Скачивание заняло {time} секунд")

print('Задача 4. Первая цифра')

X = float(input('Введите число: '))
print(int(X * 10) % 10)

print('Задача 5. Вот это объёмы!')

import math

R = float(input('Введите радиус планеты: '))
earth = 10.8321 * (10 ** 11)
another_planet = round(4 * math.pi / 3 * (R ** 3), 3)
answer = 'Объём планеты Земля {0} в {1} раз.'

if another_planet < earth:
    print(answer.format('больше', round(earth / another_planet, 3)))
else:
    print(answer.format('меньше', round(another_planet / earth, 3)))

print('Задача 6. Ход конём')

print('Введите местоположение коня:')
horse_x = float(input('X: '))
horse_y = float(input('Y: '))
print('Введите местоположение точки на доске:')
table_x = float(input('X: '))
table_y = float(input('Y: '))

hx_square = int(horse_x * 10)
hy_square = int(horse_y * 10)
tx_square = int(table_x * 10)
ty_square = int(table_y * 10)

print(f'Конь в клетке ({hx_square}, {hy_square}). Точка в клетке ({tx_square}, {ty_square}).')
if abs((horse_x - table_x) * (horse_y - table_y)) == 2:
    print('Нет, конь не может ходить в эту точку.')
else:
    print('Да, конь может ходить в эту точку.')

print('Задача 7. За что?')

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(f"Наибольшее число: {((num1 + num2) + abs(num1 - num2)) / 2}")