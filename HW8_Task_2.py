# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivisionByZero:

    def __init__(self, divisible, denominator):
        self.divisible = divisible
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divisible, denominator):
        try:
            return (divisible / denominator)
        except:
            return (f"Делить на ноль нельзя!")


div = DivisionByZero(10, 100)
print(type(div))
print(DivisionByZero.divide_by_zero(1, 8))
print(DivisionByZero.divide_by_zero(10, 0))
print(DivisionByZero.divide_by_zero(10, 0.1))
print(div.divide_by_zero(100, 0))
print(div.divide_by_zero(10, 100))

