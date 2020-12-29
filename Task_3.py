'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(number1, number2, number3):
    try:
        my_list = [number1, number2, number3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Повторите ввод чисел без ошибок'

print(my_func(3, 5, 2))
print(my_func(13.7, 15.9, 21.3))

