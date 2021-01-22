# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение ( __add__() ), вычитание ( __sub__() ), умножение ( __mul__() ),
# деление ( __truediv__() ). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.
# Сложение . Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание . Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение . Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление . Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order() , принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n***** ..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n** .
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n***** .

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Sum of cells is: ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return 'Разность клеток: ' + str(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше, чем во второй, или столько же, вычитание невозможно!'

    def __mul__(self, other):
        return 'Product of multiplication of cells is: ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'True division of cells is: ' + str(round(self.nums / other.nums))

cell_1 = Cell(1000)
cell_2 = Cell(1020)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(50))
print()

cell_1 = Cell(87)
cell_2 = Cell(31)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(20))