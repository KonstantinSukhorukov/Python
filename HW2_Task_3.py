'''
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
'''

month = int(input('Введите номер месяца: '))

# Способ 1й, через if

if month <= 0 or month >= 13:
    print('Incorrect month')
    # month = int(input('Введите номер месяца: '))
elif month >= 3 and month <= 5:
    print('Spring')
elif month >= 6 and month <= 8:
    print('Summer')
elif month >= 9 and month <= 11:
    print('Autumn')
else:
    print('Winter')

# Способ 2й, через list

seasons_list = ['', 'Winter', 'Winter', 'Spring',  'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
i = int(input('Введите номер месяца: '))
print(seasons_list[i])

# Способ 3й, через словарь

seasons_dictionary = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter'
}

month = int(input('Введите номер месяца: '))
print(seasons_dictionary[month])