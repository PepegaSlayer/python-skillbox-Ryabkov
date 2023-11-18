print('Задача 1. Тестовое задание')

for rows in range(0, 6):
  row = ""
  for column in range(0, 11, 2):
    row += str(column + rows) + "\t"
  print(row)
  
print('Задача 2. Лестница')

count = int(input("Введите число: "))
for rows in range(1, count + 1):
  for columns in range(1, rows + 1):
    print(rows, end=" " )
  print("\n")

print('Задача 3. Рамка')

height = int(input("Введите высоту рамки: "))
width = int(input("Введите ширину рамки: "))
print(" -" * width + " -")
for rows in range(height):
    print("|" + " " * (2 * width + 1) + "|")
print(" -" * width + " -")

print('Задача 4. Простые числа')

N = int(input("Введите количество чисел: "))
result = 0
for i in range(N):
  num = int(input("Введите число: "))
  flag = True
  for j in range(2, num // 2 + 1):
    if num % j == 0:
      flag = False;
      break;
  if flag:
    result += 1  
print(f"Количество простых чисел в последовательности: {result}")

print('Задача 5. Наибольшая сумма цифр')

N = int(input("Введите кол-во чисел: "))
max_num = 0
max_summ = 0
for i in range(N):
  sum = 0
  digit = 0
  number = int(input("Введите число: "))
  temp = number
  while temp > 0:
      digit = temp % 10
      sum += digit
      temp //= 10
  if sum > max_summ:
      max_summ = sum
      max_number = number
print(f"Наибольше по сумме цифр число {max_number} с суммой {max_summ}")

print('Задача 6. Пирамидка')

height = int(input("Введите высоту пирамиды: "))
for rows in range(1, height+1):
    print(" "*(height-rows) + "#"*(2*rows-1))

print('Задача 7. Пирамидка 2')

height = int(input("Введите количество уровней пирамиды: "))
num = 1
for i in range(1, height+1):
    spaces = " "*(height-i)
    print(f"{spaces}", end="")
    for j in range(i):
        print(f"{num:2d} ", end="")
        num += 2
    print()

print('Задача 8. Яма ')

N = int(input("Введите число: "))
max_string = ""
for i in range(N, 0, -1):
    max_string += str(i)
max_length = len(max_string)

for i in range(1, N + 1):
    line = ""
    for j in range(N, N - i, -1):
        line += str(j)
    line += "." * (max_length - len(line))
    print(line + line[::-1])
