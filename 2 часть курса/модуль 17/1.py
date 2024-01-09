floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

# Создание новых списков с помощью генераторов
cubed_rounded_floats = [round(x ** 3, 3) for x in floats]
filtered_names = [name for name in names if len(name) >= 5]
product_of_numbers = 1
for num in numbers:
    product_of_numbers *= num

print(cubed_rounded_floats) # [1928.712, 64.972, 193.463, 9.028, 29.839, 86.902, 1331.331]
print(filtered_names) # ['William', 'Richards', 'Joy']
print(product_of_numbers) # 68198352