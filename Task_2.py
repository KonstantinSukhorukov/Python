'''
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

vremya_v_sekundax = int(input('Введите произвольное время в секундах, да побольше!: '))

hours = vremya_v_sekundax // 3600
remainder = vremya_v_sekundax % 3600
minutes = remainder // 60
seconds = remainder % 60

if hours < 10:
    hours = str(f'0{hours}')

if minutes < 10:
    minutes = str(f'0{minutes}')

if seconds < 10:
    seconds = str(f'0{seconds}')

print(f'{hours}:{minutes}:{seconds}')