'''
 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

number1 = input('Введите любое число: ')
number2 = input('Введите еще одно число, только не ноль!: ')

def my_division(number1, number2):
    try:
        number1, number2 = float(number1), float(number2)
        result = number1 / number2
    except ValueError:
        return 'Error', 'Ошибка при вводе чисел!'
    except ZeroDivisionError:
        return 'Деление на ноль невозможно!'
    return result

print(my_division(number1, number2))

