text = input("Введите текст: ")
result = []
need = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
for char in text:
    if char in need:
        result.append(char)

print(f"Список гласных букв: {result}")
print(f"Длина списка: {len(result)}")

# следующая задача #

N = int(input("Введите длину списка: "))

result = [1 if (x % 2 != 1 or x == 0)
          else x % 5
          for x in range(N)]
print(result)

# следующая задача #

import random

first_athletes = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_athletes = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [max(first_athletes[index], second_athletes[index]) for index in range(20)]

print(f"Первая команда: {first_athletes}")
print(f"Вторая команда: {second_athletes}")
print(f"Победители тура: {winners}")

# следующая задача #

alphabet = "abcdefg"
print(f"1: {alphabet[:]}")
print(f"2: {alphabet[::-1]}")
print(f"3: {alphabet[::2]}")
print(f"4: {alphabet[1::2]}")
print(f"5: {alphabet[:1]}")
print(f"6: {alphabet[:-2:-1]}")
print(f"7: {alphabet[3:4]}")
print(f"8: {alphabet[len(alphabet)-3:]}")
print(f"9: {alphabet[3:5]}")
print(f"10: {alphabet[4:2:-1]}")

# следующая задача #

text = input("Введите строку: ")

print(f"Развёрнутая последовательность между первым и последним h: {text[text.rindex('h')-1:text.index('h'):-1]}")

# следующая задача #

print([[x for x in range(i, i+9, 4)] for i in range(1, 5)])

# следующая задача #

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

print([x for i in range(len(nice_list))
       for j in range(len(nice_list[i]))
       for x in nice_list[i][j]])

# следующая задача #

cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)]
encrypted_text = ""

users_text = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

for letter in users_text:
    if letter in cyrillic:
        new_letter = cyrillic[(cyrillic.index(letter) + shift) % len(cyrillic)]
        encrypted_text += new_letter
    else:
        encrypted_text += letter

print("Зашифрованное сообщение:", encrypted_text)