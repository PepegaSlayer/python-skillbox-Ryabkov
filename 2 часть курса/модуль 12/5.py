class Task:
	def __init__(self, name, priority):
		self.name = name
		self.priority = priority

	def __lt__(self, other):
		return self.priority < other.priority

	def __str__(self):
		return f"{self.name}"


class PriorityQueue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def insert(self, item):
		self.items.append(item)
		self.items = sorted(self.items)

	def delete(self):
		return self.items.pop(0)

	def __str__(self):
		result = ""
		prev_priority = None
		for task in self.items:
			if task.priority != prev_priority:
				if prev_priority is not None:
					result = result[:-2] + "\n" # remove the last comma and space
				result += f"{task.priority} - {task.name}, "
				prev_priority = task.priority
			else:
				result += f"{task.name}, "
		return result[:-2] # remove the last comma and space


# Пример использования
queue = PriorityQueue()

queue.insert(Task("сделать уборку", 4))
queue.insert(Task("помыть посуду", 4))
queue.insert(Task("отдохнуть", 1))
queue.insert(Task("поесть", 2))
queue.insert(Task("сдать ДЗ", 2))

print(queue)