def print_sequence(start, end):
	if start <= end:
		print(start)
		print_sequence(start + 1, end)


num = int(input("Введите num: "))
print_sequence(1, num)

# Следующая задача #

def find_key(structure, my_key, depth=100):
	if depth is None or depth >= 1:
		if my_key in structure:
			return structure[my_key]
		else:
			for element in structure.values():
				if isinstance(element, dict):
					result = find_key(element, my_key, depth - 1)
					if result:
						break
			else:
				result = None
			return result
	else:
		return None


site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}
key = input('Введите искомый ключ: ')

yes_or_no = input("Хотите ввести максимальную глубину? Y/N: ").lower()
if yes_or_no == 'y':
	maximum_depth = int(input('Введите максимальную глубину: '))
	value_key = find_key(site, key, maximum_depth)
else:
	value_key = find_key(site, key)
print(f'Значение ключа: {value_key}')

# Следующая задача #

import copy


def replace_product_name(template, product_name):
    if isinstance(template, str):
        return template.replace('телефон', product_name).replace('iPhone', product_name)
    elif isinstance(template, dict):
        new_template = {}
        for key, value in template.items():
            new_template[key] = replace_product_name(value, product_name)
        return new_template
    else:
        return template


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}
num_sites = int(input("Сколько сайтов: "))
sites_list = [copy.deepcopy(site) for _ in range(num_sites)]

for i in range(num_sites):
    product_name = input("Введите название продукта для нового сайта: ")
    for j in range(i + 1):
        print(f"Сайт для {product_name}: ")
        print(replace_product_name(sites_list[j], product_name))

# Следующая задача #

def sum(*nums):
	res = 0
	for num in nums:
		try:
			res += sum(*num)
		except TypeError:
			res += num
	return res


print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))

# Следующая задача #

def func(arr):
	if not arr:
		return []
	return func(arr[:-1]) + ([arr[-1]] if not isinstance(arr[-1], list) else func(arr[-1]))


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(func(nice_list))

def qsort(arr):
	if len(arr) <= 1:
		return arr
	sep = arr[-1]
	left = []
	mid = []
	right = []
	for a in arr:
		if a < sep:
			left.append(a)
		elif a == sep:
			mid.append(a)
		else:
			right.append(a)
	return qsort(left) + mid + qsort(right)


x = [1, 2, 3, 5, 2, 3, -7, 3, 0, 0, 11, 6]

print(qsort(x))