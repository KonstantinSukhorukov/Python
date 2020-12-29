'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

# Способ I.
def my_power_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return 'Введите числа без ошибок!'
    return result

print(my_power_func(7, -3))
print(my_power_func(5.0, -1))
print(my_power_func(16, -4))
print(my_power_func(0.811, -6))


# Способ II.

def my_power_function(x, y):
    # y - отрицательное целое число
    try:
        x, y = float(x), int(y)
        result = x
        for i in range(abs(y) - 1):
            result = result * x
        return 1 / result
    except y == - 1:
        return 1 / x
    except ValueError:
        return 'Введите данные еще раз, без ошибок!'

print(my_power_function(7, -3))
print(my_power_function(5.0, -1))
print(my_power_function(16, -4))
print(my_power_function(0.811, -6))

