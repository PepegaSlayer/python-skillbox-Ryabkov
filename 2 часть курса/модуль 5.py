menu = input("Доступное меню: ").split(";")
print(f"Сейчас в меню есть: {', '.join(menu)}")

# следующая задача #

words = input("Введите строку: ").replace(".", "").split()
longest_word = max(words, key=len)
max_len = len(longest_word)
print(f'Самое длинное слово: "{longest_word}"')
print(f"Длина этого слова: {max_len}.")

# следующая задача #

path = input("Название файла: ")

if path[0] in "(@№$%^&*())":
    print("Ошибка: название начинается недопустимым символом.")
elif not(path.endswith(".txt") or path.startswith(".docx")):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("Файл назван верно.")

# следующая задача #

words = input("Введите строку: ")
print(f"Результат: {words.title()}")

# следующая задача #

while True:
    password = input("Придумайте пароль: ")
    if (len(password) >= 8 and 
        len([char for char in password if char.isupper()]) > 0 and 
        len([char for char in password if char.isdigit()]) >= 3):
        print("Это надёжный пароль.")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")

# следующая задача #

string = input("Введите строку: ")
encoded_string = []
count = 1
for i in range(len(string)):
    if i == len(string)-1:
        encoded_string.append(string[i] + str(count))
    elif string[i] == string[i+1]:
        count += 1
    else:
        encoded_string.append(string[i] + str(count))
        count = 1

encoded_string = ''.join(encoded_string)
print("Закодированная строка:", encoded_string)

# следующая задача #

ip = input("Введите IP: ")
ip_numbers = ip.split(".")
if len(ip_numbers) != 4:
    print("Адрес — это четыре числа, разделённые точками.")
else:
    ip = [x for x in ip_numbers if x.isdigit()]
    if len(ip) != 4:
        for i in ip_numbers:
            if i.isalnum() and (not(i.isdigit())):
                print("{} - это не целое число.".format(i))
    else:
        ip_numbers = []
        for numbers in ip:
            if int(numbers) > 255:
                print("{} превышает 255.".format(numbers))

            else:
                ip_numbers.append(numbers)
        if len(ip_numbers) == 4:
            print("IP-адрес корректен.")

# следующая задача #

string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

if len(string1) != len(string2):
    print("Строки разной длины, невозможно получить первую строку из второй с помощью циклического сдвига.")
else:
    for i in range(len(string1)):
        if string1 == string2:
            print("Первая строка получается из второй со сдвигом", i)
            break
        string2 = string2[1:] + string2[0]
    else:
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

# следующая задача #

def count_uppercase_lowercase(text):
    upper = len([char for char in text if char.isupper()])
    lower = len([char for char in text if char.islower()])
    return upper, lower


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)