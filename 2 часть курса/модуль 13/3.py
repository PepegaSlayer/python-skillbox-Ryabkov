import os


def get_python_files(directory='C:/'):
	python_files = []
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith('.py'):
				file_path = os.path.join(root, file)
				python_files.append(file_path)
	return python_files


def count_non_empty_non_comment_lines(file_path):
	with open(file_path, 'r') as f:
		lines = f.readlines()
		non_empty_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
		return len(non_empty_lines)


# Пример использования, вместо Users мб любая другая директория
python_files = get_python_files('C:/Users')
for file_path in python_files:
	num_lines = count_non_empty_non_comment_lines(file_path)
	print(f'{file_path}: {num_lines} non-empty non-comment lines')