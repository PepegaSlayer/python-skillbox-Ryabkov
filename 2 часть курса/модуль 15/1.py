class File:
	def __init__(self, file_name, mode):
		self.file_name = file_name
		self.mode = mode
		self.file = None

	def __enter__(self):
		try:
			self.file = open(self.file_name, self.mode)
		except FileNotFoundError:
			self.file = open(self.file_name, 'w') # Если файл не существует, создаем новый в режиме записи
		return self.file

	def __exit__(self, exc_type, exc_value, traceback):
		if self.file:
			self.file.close()
		return True # Подавляем все исключения, связанные с файлами


def write_to_file(file_name, content):
	with File(file_name, 'r') as file:
		file.write(content)


write_to_file('example.txt', 'Hello, World!')