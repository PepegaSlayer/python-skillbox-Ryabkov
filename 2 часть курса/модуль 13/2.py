import os


def gen_files_path(directory='C:/'):
	for root, dirs, files in os.walk(directory):
		for file in files:
			yield os.path.join(root, file)


# Пример использования
for file_path in gen_files_path('C:/Users'):
	print(file_path)