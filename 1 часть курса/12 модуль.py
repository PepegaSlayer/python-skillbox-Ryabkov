print('Задача 1. Сумма чисел')

def summa_n(N):
  sum = 0
  for i in range(N + 1):
      sum += i
  return sum


N = int(input("Введите число: "))
print(f"Я знаю, что сумма чисел от 1 до {N} равна {summa_n(N)}")

print('Задача 2. Функция в функции')

def test():
    N = int(input("Введите число: "))
    if N > 0:
        positive()
    else:
        negative()


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


test()print('Задача 3. Апгрейд калькулятора')

def make_list_of_digits(number):
  result = []

  while number > 0:
      result.append(number % 10)
      number //= 10

  return result


def max_num(number):
  max_digit = 0
  for x in make_list_of_digits(number):
      if x > max_digit:
        max_digit = int(x)
  print(f"Самая большая цифра числа это {max_digit}")


def min_num(number):
  min_digit = 10

  for x in make_list_of_digits(number):
      if x < min_digit:
          min_digit = int(x)
  print(f"Самая маленькая цифра числа это {min_digit}")

def sum_num(number):
  sum_digit = 0
  for x in make_list_of_digits(number):
      sum_digit += int(x)
  print(f"Сумма цифр числа равна {sum_digit}")


N = int(input("Введите число (0 - Это выход): "))
while N != 0:
  answer = input("Введите номер действия:\n1) Сумма цифр\n2) Максимальная из цифр\n3) Минимальная из цифр\n")
      
  if answer == "1":
    sum_num(N)
  elif answer == "2":
    max_num(N)
  elif answer == "3":
    min_num(N)
  else:
    print("Неверное действие")
  N = int(input("Введите число (0 - Это выход): "))

print('Задача 4. Число наоборот')

def reverse(N):
  N = str(N)[::-1]
  N = int(N)
  print(f"Число наоборот: {N}")


N = 1
while N != 0:
  N = int(input("Введите число: "))
  reverse(N)
if N == 0:
  print("Программа завершена!")

print('Задача 5. Текстовый редактор')

def count_letters(sentence, K, N):
  countK = 0
  countN = 0
  for letter in sentence:
      if letter == K:
          countK += 1
      if letter == N:
          countN += 1
  print(f"Количество цифр {K}: {countK}")
  print(f"Количество букв {N}: {countN}")


text = input("Введите текст: ")
K = input("Какую цифру ищем? ")
N = input("Какую букву ищём? ")
count_letters(text.lower(), K, N)

print('Задача 6. НОД')

def max_devide(a, b):
  if b == 0:
      return a
  else:
      return max_devide(b, a % b)


first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
print(f"Наибольший общий делитель чисел это: {max_devide(first, second)}")

print('Задача 7. Недоделка')

import random


def rock_paper_scissors():
  choices = ['камень', 'ножницы', 'бумага']
  comp = random.SystemRandom().choice(choices)
  user = input('Введите камень, ножницы или бумага: ')
  if user in choices:
      print(f'Компьютер выбрал: {comp}')
      if user == comp:
          print('Ничья')
      elif (user == 'камень' and comp == 'ножницы') or (user == 'ножницы' and comp == 'бумага') or (user == 'бумага' and comp == 'камень'):
          print('Вы победили')
      else:
          print('Вы проиграли')
  else:
      print('Неверный ввод. Пожалуйста, введите камень, ножницы или бумага.')


def guess_the_number():
    guessing = random.randint(1, 10)
    while True:
        answer = int(input("Угадайте число, которое загадал компьютер(От 1 до 10): "))
        if answer != guessing:
            print("Вы не угадали, попробуйте еще раз.")
        else:
            print(f"Поздравляем! Вы назвали угадали число {answer}")
            break


def mainMenu():
    choice = int(input('Выберите игру:\n1) Камень.Ножницы.Бумага.\n2) Угадай число.\nВаш выбор: '))
    if choice == 1:
        print()
        rock_paper_scissors()
    elif choice == 2:
        print()
        guess_the_number()
    else:
        print('Неправильный выбор. Выберите игру.')


mainMenu()
