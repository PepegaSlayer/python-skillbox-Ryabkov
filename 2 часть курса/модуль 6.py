violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
duration = 0

songs_count = int(input("Сколько песен выбрать? "))

for _ in range(songs_count):
    song = input("Название песни: ")
    if song in violator_songs:
        duration += violator_songs[song]
    else:
        print("Такой песни нет")

print("Общее время звучания песен: {:.2f} минут".format(duration))

# Следующая задача #

data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

#  1 Пункт
print(data.keys())
print(data.values())

#  2 Пункт
data['ETH']['total_diff'] = 100

# 3 пункт
data['tokens'][0]['fst_token_info']["name"] = "doge"

# 4 пункт
data["ETH"]["totalOut"] += data["tokens"][0].pop("total_out") + data["tokens"][1].pop("total_out")

# 5 пункт
data["tokens"][1]["sec_token_info"]["total_price"] = data["tokens"][1]["sec_token_info"].pop("price")

# Следующая задача #

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product in goods.keys():
    final_price = 0
    count = 0
    for choice in store[goods[product]]:
        count += choice["quantity"]
        final_price += choice["quantity"] * choice["price"]
    print("{0} — {1} штук, стоимость {2} рубля.".format(product, count, final_price))

# Следующая задача #

users_text = input("Введите текст: ")
pre_final = dict()
final = dict()

for char in users_text:
    if char in pre_final:
        pre_final[char] += 1
    else:
        pre_final[char] = 1

print("Оригинальный словарь частот: ")
for char in pre_final:
    print(char, ":", pre_final[char])

for char in pre_final.keys():
    if pre_final[char] in final:
        final[pre_final[char]].append(char)
    else:
        final[pre_final[char]] = [char]

print("Инвертированный словарь частот:")
for final_invert in final:
    print(final_invert, ":", final[final_invert])

# Следующая задача #

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


words_count = int(input("Введите количество пар слов: "))
synonyms = dict()

for _ in range(words_count):
    word1, word2 = input("пара слов(через '-'): ").lower().replace(" ", "").split("-")
    synonyms[word1] = word2

while True:
    word = input("Введите слово: ").lower()
    if word in synonyms.keys() or word in synonyms.values():
        if word in synonyms.keys():
            print("Синоним:", synonyms.get(word))
        else:
            print("Синоним:", get_key(synonyms, word))
        break
    else:
        print("Такого слова в словаре нет.")

# Следующая задача #

orders_count = int(input("Введите количество заказов: "))
orders = dict()

for order_number in range(1, orders_count+1):
    order = input("{}-й заказ: ".format(order_number)).split()
    if order[0] in orders:
        if order[1] in orders[order[0]]:
            orders[order[0]][order[1]] += order[2]
        else:
            orders[order[0]][order[1]] = order[2]
    else:
        orders[order[0]] = {order[1]: order[2]}

print("Итоговый заказ:")

for name in orders.keys():
    print(name, ":")
    for order in orders[name]:
        print(order, ":", orders[name][order])
    print("")

# Следующая задача #

array_1 = {1, 5, 10, 20, 40, 80, 100}
array_2 = {6, 7, 20, 80, 100}
array_3 = {3, 4, 15, 20, 30, 70, 80, 120}

# Это при помощи множеств
print(array_1 & array_2 & array_3)
print((array_1 - array_3) & (array_1 - array_2))

# Без помощи множеств
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

common_elements = []
for element in array_1:
    if element in array_2 and element in array_3:
        common_elements.append(element)
print(common_elements)

unique_elements = []
for element in array_1:
    if element not in array_2 and element not in array_3:
        unique_elements.append(element)
print(unique_elements)

# Следующая задача #

string = input("Введите строку: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

odd_count = 0
for count in char_count.values():
    if count % 2 != 0:
        odd_count += 1
    if odd_count > 1:
        print("Нельзя сделать палиндромом.")
        break
else:
    print("Можно сделать палиндромом.")