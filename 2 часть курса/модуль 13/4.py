class ListNode:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = ListNode(data)
		if not self.head:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node

	def get(self, index):
		if index < 0:
			return None
		current = self.head
		for i in range(index):
			if current.next:
				current = current.next
			else:
				return None
		return current.data

	def remove(self, index):
		if index < 0 or not self.head:
			return
		if index == 0:
			self.head = self.head.next
			return
		current = self.head
		for i in range(index - 1):
			if current.next:
				current = current.next
			else:
				return
		if current.next:
			current.next = current.next.next

	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next

	def __repr__(self):
		return '[' + ' '.join(str(data) for data in self) + ']'


# Пример использования
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)