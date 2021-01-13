# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def umnojenie_v_spiske(n1, n2):
    return n1 * n2

moi_spisok = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(umnojenie_v_spiske, moi_spisok))