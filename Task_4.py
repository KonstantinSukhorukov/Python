'''
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

your_number = int(input('Введите произвольное положительное целое число: '))

max_digit = 0



while your_number >= 10:
    remainder = your_number % 10
    if remainder == 9:
        max_digit = remainder
    elif max_digit <= remainder:
        max_digit = remainder
    else:
        max_digit = max_digit
    your_number = your_number // 10
remainder = your_number
if max_digit < remainder:
    max_digit = remainder
print(max_digit)
