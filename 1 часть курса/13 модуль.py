print('Задача 1. Урок информатики 2')

def make_float(n):
  k = 0
  if n >= 1:
      while n >= 10:
          n /= 10
          k += 1
  else:
      while n < 1:
          n *= 10
          k -= 1
  print(f'Формат плавающей точки: х = ', round(n, 5), ' * 10 ** ', k)


n = float(input('Введите число: '))

make_float(n)

print('Задача 2. Функция максимума')

def max_3(a, b, c):
  return max(max(a, b), max(b, c))

print('Задача 3. Число наоборот 2')

def reverse_num(num):
    result = 0
    while num > 0:
      result = result * 10 + num % 10
      num = num // 10
    return result


n = int(input('Введите первое число: '))
k = int(input('Введите второе число: '))
print('Первое число наоборот:', reverse_num(n))
print('Второе число наоборот:', reverse_num(k))
print('Сумма:', reverse_num(n) + reverse_num(k))
print('Сумма наоборот:', reverse_num(reverse_num(n) + reverse_num(k)))

print('Задача 4. Недоделка 2')

def count_numbers(num):
  count = 0
  while num > 0:
    num = num // 10
    count += 1
  return count

def change_number(n):
  n = str(n)
  if len(n) > 1:
    return int(n[-1] + n[1:-1] + n[0])
  else:
    return int(n)

def main(): 
  first_n = int(input("Введите первое число: "))
  first_num_count = count_numbers(first_n);
  if first_num_count < 3:
      print("В первом числе меньше трёх цифр.")
  else:
      first_n = change_number(first_n)
      print('Изменённое первое число:', first_n)
  second_n = int(input("\nВведите второе число: "))
  second_num_count = count_numbers(second_n);
  if second_num_count < 4:
    print("Во втором числе меньше четырёх цифр.")
  else:
    second_n = change_number(second_n);
    print('Изменённое второе число:', second_n )
    print('\nСумма чисел:', first_n + second_n)

main()

print('Задача 5. Маятник ')

import math

start_amplitude = float(input('Введите начальную амплитуду: '))
stop_amplitude = float(input('Введите амплитуду остановки: '))

oscillations = math.ceil(-math.log(start_amplitude / stop_amplitude, 0.916))

print(f'Маятник считается остановившимся через {oscillations} колебаний')

print('Задача 6. Яйца')

def evaluate(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10


def compute_safe_depth(threshold):
  lower_limit = 0
  upper_limit = 4
  mid_point = (lower_limit + upper_limit) / 2

  while abs(evaluate(mid_point)) >= threshold:
      if abs(evaluate(lower_limit)) < abs(evaluate(upper_limit)):
          upper_limit = mid_point
      else:
          lower_limit = mid_point

      mid_point = (lower_limit + upper_limit) / 2
  return mid_point


def main_function():
    accept_danger_lvl = float(input('Введите максимально допустимый уровень опасности: '))
    result = compute_safe_depth(accept_danger_lvl)
    print('Приблизительная глубина безопасной кладки: ', result, 'm')


main_function()