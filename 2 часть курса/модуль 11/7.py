class Matrix:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.data = [[0 for _ in range(cols)] for _ in range(rows)]

	def add(self, matrix):
		if self.rows != matrix.rows or self.cols != matrix.cols:
			return "Матрицы разного размера"
		else:
			result = Matrix(self.rows, self.cols)
			for i in range(self.rows):
				for j in range(self.cols):
					result.data[i][j] = self.data[i][j] + matrix.data[i][j]
			return result

	def subtract(self, matrix):
		if self.rows != matrix.rows or self.cols != matrix.cols:
			return "Матрицы разного размера"
		else:
			result = Matrix(self.rows, self.cols)
			for i in range(self.rows):
				for j in range(self.cols):
					result.data[i][j] = self.data[i][j] - matrix.data[i][j]
			return result

	def multiply(self, matrix):
		if self.cols != matrix.rows:
			return "Невозможно умножить матрицы"
		else:
			result = Matrix(self.rows, matrix.cols)
			for i in range(self.rows):
				for j in range(matrix.cols):
					for k in range(self.cols):
						result.data[i][j] += self.data[i][k] * matrix.data[k][j]
			return result

	def transpose(self):
		result = Matrix(self.cols, self.rows)
		for i in range(self.rows):
			for j in range(self.cols):
				result.data[j][i] = self.data[i][j]
		return result

	def __str__(self):
		return '\n'.join([' '.join([str(col) for col in row]) for row in self.data])


# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())