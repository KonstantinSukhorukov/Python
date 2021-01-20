# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

# Следующие 5 строк раскомментировать не надо!
# with open('payroll.txt', 'w', encoding='utf-8') as f:
#     for i in range(1, 11):
#         name = input('Введите фамилию: ')
#         earning = input('Введите зарплату в рублях: ')
#         f.write('{} - {}\n'.format(name, earning))


with open('payroll.txt', encoding="utf-8") as f:
    lines = f.readlines()

earnings = []
for line in lines:
    try:
        name, earning = line.split('-')
        earnings.append(int(earning))
        if int(earning) < 20000:
            print(line, end='')
    except ValueError:
            continue
print('\nAverage earnings: ', sum(earnings) / len(earnings))