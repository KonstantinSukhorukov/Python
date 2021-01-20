# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print('Ручка пишет и рисует')

class Pencil(Stationary):
    def draw(self):
        print('Карандаш делает скетчи и заштриховывает')

class Handle(Stationary):
    print('Маркер пишет на белой доске и стирается губкой')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
marker = Handle('Маркер')

pen.draw()
pencil.draw()
marker.draw()
