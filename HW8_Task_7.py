# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __str__(self):
        if self.a == 0 and self.b == 0:
            return f'z = 0'
        elif self.a == 0:
            return f'z = {self.b}i'
        elif self.b == -1:
            return f'z = {self.a} - i'
        elif self.b == 1:
            return f'z = {self.a} + i'
        elif self.b == 0:
            return f'z = {self.a}'
        elif self.b < 0 and self.b != -1:
            return f'z = {self.a} - {abs(self.b)}i'
        else:
            return f'z = {self.a} + {self.b}i'


    def __add__(self, other):
        print(f'Сумма {self} и {other} равна: ')
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)


    def __mul__(self, other):
        print(f'Произведение {self} и {other} равно: ')
        a = self.a * other.a - (self.b * other.b)
        b = (self.b * other.a) + (self.a * other.b)
        return ComplexNumber(a, b)


z_1 = ComplexNumber(3, -1)
z_2 = ComplexNumber(-5, 3)
z_3 = ComplexNumber(-1, 1)
z_4 = ComplexNumber(7, -2)
z_5 = ComplexNumber(5, 11)
z_6 = ComplexNumber(1, -1)
z_7 = ComplexNumber(0, -3)
z_8 = ComplexNumber(3, 0)

print(z_1)
print(z_2)
print(z_3)
print(z_4)
print(z_5)
print(z_6)
print(z_7)
print(z_8)

print(z_1 + z_2)
print(z_1 * z_2)
print(z_3 + z_4)
print(z_3 * z_4)
print(z_2 + z_5)
print(z_2 * z_5)
print(z_3 + z_6)
print(z_3 * z_6)
print(z_7 + z_8)
print(z_7 * z_8)
print(z_2 + z_4)

print(z_1 * z_1)
print(z_2 * z_2)
print(z_3 * z_3)
print(z_4 * z_4)
print(z_5 * z_5)
print(z_6 * z_6)
print(z_7 * z_7)
print(z_8 * z_8)