# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__() ), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.input])

    def __add__(self, other):
        result = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problem with matrices shape and compatability!'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                result += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Problem with matrices shape and compatibility!'
        return result

matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[11, 12], [13, 14], [16, 17]])

print(matrix_1,'\n')
print(matrix_2, '\n')

print(matrix_1 + matrix_2)
print(matrix_1.__add__(matrix_2))

matrix_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_2 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(matrix_1,'\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)
print(matrix_1.__add__(matrix_2))

matrix_1 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
matrix_2 = Matrix([[11, 12, 13, 15], [-11, -5, -17, 9]])
print(matrix_1,'\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)
print(matrix_1.__add__(matrix_2))

matrix_1 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
matrix_2 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(matrix_1,'\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)
print(matrix_1.__add__(matrix_2))
