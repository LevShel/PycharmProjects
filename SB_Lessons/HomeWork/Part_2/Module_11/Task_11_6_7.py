# Задача 7. Матрицы
# Контекст
# Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам поручили разработать
# класс Matrix для обработки и анализа данных. Ваш класс должен предоставлять функциональность
# для выполнения основных операций с матрицами, таких как сложение, вычитание, умножение
# и транспонирование. Это будет полезно для обработки и структурирования больших объёмов
# данных, которые используются в обучении нейронных сетей.
# Задача
# 1.	Создайте класс Matrix для работы с матрицами.
# Реализуйте методы:
# o	сложения,
# o	вычитания,
# o	умножения,
# o	транспонирования матрицы.
# 2.	Создайте несколько экземпляров класса Matrix и протестируйте реализованные операции.

class Matrix:
    def __init__(self, rows=None, cols=None, data=None):
        self.rows = rows if rows else int(input('Num of rows: '))
        self.cols = cols if cols else int(input('Num of cols: '))
        self.matrix = data if data else []

    def data(self):
        for row in range(self.rows):
            col_data = input(f'Enter {row + 1} row: ')
            row = list(col_data.split())
            self.matrix.append(row)
        return self.matrix

    def print_info(self):
        max_length = max(len(str(item)) for row in self.matrix for item in row)
        for row in self.matrix:
            print(' '.join(str(item).center(max_length) for item in row))

    def __add__(self, other):
        summa = []
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                new_row.append(self.matrix[row][col] + other.matrix[row][col])
            summa.append(new_row)
        return Matrix(self.rows, self.cols, summa)

    def __sub__(self, other):
        raznost = []
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                new_row.append(self.matrix[row][col] - other.matrix[row][col])
            raznost.append(new_row)
        return Matrix(self.rows, self.cols, raznost)

    def __mul__(self, other):
        proizvedenie = []
        for row in range(self.rows):
            new_row = []
            for col in range(other.cols):
                data = 0
                for i in range(self.cols):
                    data += self.matrix[row][i] * other.matrix[i][col]
                new_row.append(data)
            proizvedenie.append(new_row)
        return Matrix(self.rows, self.cols, proizvedenie)


# # # Создание экземпляров класса Matrix
m1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
m2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])

# # # Тестирование операций
print("Матрица 1:")
m1.print_info()
# 1    2    3
# 4    5    6
print("Матрица 2:")
m2.print_info()
# 7    8    9
# 10    11    12

print("Сложение матриц:")
result = m1.__add__(m2)
result.print_info()
# 8    10    12
# 14    16    18

print("Вычитание матриц:")
result = m1.__sub__(m2)
result.print_info()
# -6    -6    -6
# -6    -6    -6

print("Матрица 3:")
m3 = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
m3.print_info()
# 1    2
# 3    4
# 5    6

print("Умножение матриц:")
result = m1.__mul__(m3)
result.print_info()
# 22    28
# 49    64

# print("Транспонирование матрицы 1:")
# print(m1.transpose())
# 1    4
# 2    5
# 3    6
