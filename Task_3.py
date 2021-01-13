'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

your_number = int(input('Введите произвольное целое число: '))

i = len(str(your_number))
print(f'В вашем числе {i} цифр')

result = 3 * your_number + 2 * (10 ** i) * your_number + (10 ** (2 * i) * your_number)
print(result)