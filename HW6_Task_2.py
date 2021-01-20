# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
# width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
# для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def required_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass

new_road = Road(5000, 20)
print(new_road.required_mass(), 'тонн')

new_road = Road(8000, 18)
print(new_road.required_mass(), 'тонн')

new_road = Road(11000, 32)
print(new_road.required_mass(), 'тонн')