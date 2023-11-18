print('Задача 1. Я стал новым пиратом!')

pirates = 0
for count in range(10):
    answer = input("Пират крикнул:  ")
    if answer == "Карамба" or word == "карамба":
        pirates += 1
print(f"В команду попали {pirates} новых пирата")

print('Задача 2. Кривой мессенджер')

number = 0
sentence = input("Введите текст: ")
for char in sentence:
    number += 1
    if char == "*":
        print(f"Символ «*» стоит на позиции {number}")
        break

print('Задача 3. Театр')

row = int(input("Введите кол-во рядов: "))
columm = int(input("Введите кол-во сидений ряду: "))
distance = int(input("Введите кол-во метров между рядами: "))
for x in range(row):
    print("=" * columm + " " + "*" * distance + " " + "=" * columm)

print('Задача 4. Марсоход 2')

x = 8
y = 10
while True:
  operator_call = input(f"[Программа]: Марсоход находится на позиции {x}, {y}, введите команду:\n[Оператор]: ")
  if operator_call == "A" and x > 0:
      x -= 1
  elif operator_call == "W" and y < 20:
      y += 1
  elif operator_call == "S" and y > 0:
      y -= 1
  elif operator_call == "D" and x < 15:
      x += 1

print('Задача 5. Великий и могучий')

sentence = input("Введите текст: ")
words = sentence.split(" ")
max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)
print(f"Самое длинное слово, {max_len} букв")

print('Задача 6. Коровы')
cowsheds= input("Введите строку из 10 коровников: ")
index = 0
milk = 0
for cowshed in cowsheds:
    index += 1
    if cowshed == "b":
        milk += number * 2
print(milk)

print('Задача 7. Метод бутерброда')

word = input('Введите зашифрованое слово: ')
first_part = ""
second_part = ""
index = 0
for letter in word:
  index += 1
  if (index % 2 == 1):
    first_part += letter
  else:
    second_part = letter + second_part
print('Расшифрованое слово', first_part + second_part)

print('Задача 8. Древний палиндром')

string = input("Введите строку: ")

is_palindrome = True
for i in range(len(string)//2):
    if string[i] != string[-i-1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром!")