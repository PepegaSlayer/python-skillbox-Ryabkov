class MyDict(dict):
	"""
    Класс MyDict унаследован от стандартного класса dict. Переопределяет метод get для возврата 0, если ключ отсутствует.
    """

	def get(self, key, default=0):
		"""
        Возвращает значение по ключу, если ключ присутствует, иначе возвращает 0.
        """
		return super().get(key, default)


# Пример использования
my_dict = MyDict({'a': 1, 'b': 2})

# Вывод значений
print(my_dict.get('c'))  # Вывод: 0
print(my_dict.get('a'))  # Вывод: 1
print(my_dict.get('b'))  # Вывод: 2