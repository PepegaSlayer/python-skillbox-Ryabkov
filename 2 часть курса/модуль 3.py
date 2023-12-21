a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a = list(set(a + b))
a = [x for x in a if x != 5]
a = a + c

print(f"Количество цифр 3 при втором объединении: {a.count(3)}")
print(f"Итоговый список: {a}")

def merge_sorted_lists(list1, list2):
    return sorted(list(set(list1 + list2)))

list1 = [1, 3, 5, 7, 9]
# list1 = [1,3] # Это на случай, когда один список короче другого
# list1 = [] # Это на случай, когда один список пустой
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(f"Вывод: {merged}")

shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
price = 0
count = 0

detail_name = input("Название детали: ")
detail_count = int(input("Количество деталей: "))

for names in shop:
    if names[0] == detail_name and count < detail_count:
        count += 1
        price += names[1]
print(f"Общая стоимость: {price}")

guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
action = ""

while action != "Пора спать":
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    action = input("Гость пришёл или ушёл? ")

    if action == "пришёл":
        guest_name = input("Имя гостя: ")
        if len(guests) <= 5:
            guests.append(guest_name)
        else:
            print("Прости, Гоша, но мест нет.")
    elif action == "ушёл":
        guest_name = input("Имя гостя: ")
        guests.remove(guest_name)
        print(f"Пока, {guest_name}!")
print("Вечеринка закончилась, все легли спать.")

violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56], ['Halo', 4.9],
                  ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76],
                  ['Blue Dress', 4.29], ['Clean', 5.83]]

songs_count = int(input("Сколько песен выбрать? "))
result_time = 0
for number in range(1, songs_count+1):
    name = input(f"Название {number} песни: ")
    for song in violator_songs:
        if song[0] == name:
            result_time += song[1]
print("Общее время звучания песен — {:.2f} минуты".format(result_time))

count = 0

n = int(input("Количество роликов: "))
roller_sizes = []
for i in range(n):
    size = int(input("Размер пары {}: ".format(i+1)))
    roller_sizes.append(size)

k = int(input("Количество людей: "))
foot_sizes = []
for i in range(k):
    size = int(input("Размер ноги человека {}: ".format(i+1)))
    foot_sizes.append(size)

for i in foot_sizes:
    if i in roller_sizes:
        count += 1
        roller_sizes.remove(i)

print("Наибольшее количество людей, которые могут взять ролики:", count)

n = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))

people = list(range(1, n+1))
i = 0

while len(people) > 1:
    i = (i + k - 1) % len(people)
    print("Выбывает человек под номером", people[i])
    people.pop(i)

print("Остался человек под номером", people[0])

numbers_count = int(input("Количество чисел: "))
sequence = []

for _ in range(numbers_count):
    sequence.append(int(input("Число: ")))

for i in range(len(sequence)):
    if sequence[i:] == sequence[i:][::-1]:
        print(f"Нужно приписать чисел: {i}")
        print(f"Сами числа: ", end="")
        print(*sequence[:i][::-1])
        break