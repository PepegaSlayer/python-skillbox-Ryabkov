with open("number.txt", "r") as input_file:
   total = 0
   for line in input_file:
       for char in line:
           if char.isdigit():
               total += int(char)

with open("answer.txt", "w") as output_file:
   output_file.write(str(total))
# Следующая задача #

def reverse_lines(file_name):
    with open(file_name, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    for line in reversed(lines):
        print(line)

reverse_lines("zen.txt")

# Следующая задача #

import os

def count_files_and_directories(directory):
    directory_size = 0
    directory_count = 0
    file_count = 0

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            directory_count += 1
            directory_size += os.path.getsize(item_path)
        else:
            file_count += 1
            directory_size += os.path.getsize(item_path)

    return directory_count, file_count, directory_size / 1024

path = os.path.abspath(input(""))

if os.path.exists(path):
    if os.path.isdir(path):
        dir_count, files_count, size = count_files_and_directories(path)
        print("{} - кол-во подкаталогов, {} - кол-во файлов, {} КБ - размер файлов".format(dir_count, files_count, size))
    else:
        print("Это файл и его размер {}Кб".format(os.path.getsize(path) / 1024))
else:
    print("Такого пути не существует")

# Следующая задача #

import os
first_tour = open("first_tour.txt", "r")
second_tour = open("second_tour.txt", "a")
minimum_score = int(first_tour.readline())

second_tour_count = 0
people = 0
result = []
for line in first_tour:
	surname, name, score = line.split()
	score = int(score)
	if score > minimum_score:
		result.append(str("{0}) {1}. {2} {3}".format(str(second_tour_count+1), name[0].upper(), surname.title(), str(score))))
		people += 1

first_tour.close()

second_tour.write(str(people) + "\n")

for people in range(len(result)):
	second_tour.write(result[people] + "\n")

second_tour.close()

# Следующая задача #

text_file = open("text.txt", "r")
text = text_file.read()
text_file.close()

letters = {}
total_letters = 0

for char in text:
    if char.isalpha():
        total_letters += 1
        char = char.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

sorted_letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))

analysis_file = open("analysis.txt", "w")
for letter, count in sorted_letters:
    frequency = count / total_letters
    analysis_file.write(f"{letter} {frequency:.3f}\n")

analysis_file.close()

from collections import defaultdict

with open('voina-i-mir.txt', 'r', encoding='windows-1251') as file:
    text = file.read()

letter_counts = defaultdict(int)
total_letters = 0

for char in text:
    if char.isalpha():
        total_letters += 1
        letter_counts[char] += 1

sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

with open('letter_statistics.txt', 'w', encoding='utf-8') as file:
    for letter, count in sorted_letter_counts:
        frequency = count / total_letters
        file.write(f"{letter}: {frequency:.6f}\n")
