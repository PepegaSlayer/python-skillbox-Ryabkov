print('Задача 1. Космическая еда')

i = 1;
for mass in range(100, 0, -4):
  print(f"{i} месяц, осталось {mass} кг гречки")
  i += 1;

print('Задача 2. Долги')

count = int(input("Введите количество должников: "))
credit = 0
for i in range(0, count, 5):
    print(f"Должник с номером {i}")
    credit += int(input("Сколько должны? "))
print(f"Общая сумма долга: {credit}")

print('Задача 3. Таймер для микроволновых печей')

reverse_timer = int(input("Задайте время до обнуления таймера: "))
for i in range(reverse_timer, -1, -1):
    if i == 0:
        print("Ваша еда готова, осторожно горячo!")
        break
    answer = int(input("хотите ли сейчас остановить разогрев или нет?(0 - нет, 1 - да)"))
    if answer == 1:
        print("Ваша еда готова, можете забрать")
        print(f"таймер прерван на {i} секунде")
        break

print('Задача 4. Отрезок')

start, end, devide = map(int, input("Введите три числа через пробел: ").split(' '))
count = 0
sum = 0
for i in range(start, end + 1):
    if i % devide == 0:
        sum += i
        count += 1
print(f"Среднее арифметическое чисел: {sum / count}")

print('Задача 5. Функция')

start = int(input("Введите начало отрезка: "))
end = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))
for x in range(end, start-1, step):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print(f"В точке {x} функция равна {y}")

print('Задача 6. Стипендия')

educational_grant = int(input("Введите стипендию: "))
expenses = int(input("Введите расходы на проживание: "))
needings = 0
for month in range(1, 11):
    needings += expenses - educational_grant
    print("{} месяц траты {:.2f} не хватает {:.2f}".format(month, expenses, needings))
    expenses += expenses * 0.03
print("Нужно попросить у родителей {:.2f} рублей".format(needings))

print('Задача 7. Сумма ряда')

count = int(input("Введите число элементов: "))
sum = 0
for index in range(count):
  sum += (-1) ** index * (0.5) ** index
print(f"{sum} - сумма ряда из {count} элементов")

print('Задача 8. Кинотеатр')

boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
answer = ''
if (boys > 2 * girls) or (girls > 2 * boys):
    print('Нет решения.')
elif boys >= girls:
    k = boys - girls
    answer = 'BGB' * k + 'BG' * (girls - k)
else:
    k = girls - boys
    answer = 'GBG' * k + 'GB' * (boys - k)
print(answer)