# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('text.txt', 'w') as f:
    while True:
        line = input('Введите строку: ')
        if line == '':
            break
        f.write(line + '\n')

# Рекомендуемый текст для ввода:
# The last time you walked out
# With the suitcase in your hand
# I was too dumb to know that it was over
# 'Cause something else had just begun