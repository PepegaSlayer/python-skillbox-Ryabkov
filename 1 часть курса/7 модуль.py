print('Задача 1. Должники')

count = 0;
for i in range(10):
    num = int(input("Введите номер человека: "))
    if num > 0 and num % 2 == 0:
        count += 1
print(f"Одновременно четными и положительными являются номера {count} человек")

print('Задача 2. Посчитай чужую зарплату...')

salary = 0
for i in range(1,13):
    salary += int(input(f"Введите зарплату за {i} месяц: "))
print(f"Среднегодовая зарплата сотрудника: {salary // 12}")

print('Задача 3. Факториал')

N = int(input("Введите число: "))
result = 1
for i in range(N,0,-1):
  result *= i
print(f"Факториал числа {N} равен {result}")

print('Задача 4. Успеваемость в классе')

C_stud = 0
B_stud = 0
A_stud = 0
N = int(input("Введите кол-во учеников: "))
for i in range(N):
    score = int(input("Введите оценку: "))
    if score == 3:
      C_stud += 1
    elif score == 4:
      B_stud += 1
    else:
      A_stud += 1
if C_stud > B_stud and C_stud > A_stud:
    print("Больше троечников")
elif B_stud > A_stud:
    print("Хорошистов больше")
else:
    print("больше всего отличников")

print('Задача 5. Отрезок')

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
sum = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        count += 1
print(f"{sum / count} среднее арифметическое чисел кратных 3, на отрезке от {a} до {b}")

print('Задача 6. Замечательные числа')

for i in range(10, 100):
  if ((i % 10) * (i // 10)  * 3) == i:
      print(i)

print('Задача 7. Пропавшая карточка')

count = int(input("Введите количество карточек: "))
sum_numbers = 0
for i in range(count - 1):
    number = int(input("Введите номер оставшейся карточки: "))
    sum_numbers += number

sum_indices = count * (count + 1) // 2

missing_card = sum_indices - sum_numbers
print(f"Потерялась карточка номер: {missing_card}")

