#  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
#  speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
#  которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} has stopped!'.format(self.name))

    def turn(self, direction):
        print('{} is turning {}'.format(self.name, direction))

    def indicate_speed(self):
        print('{} current speed is {}'.format(self.name, self.speed))

class TownCar(Car):
    def indicate_speed(self):
        super().indicate_speed() # модифицируем старый класс и использование функции indicate_speed
        if self.speed > 60:
            print('Alert!! {} speed exceeds allowed maximum!'.format(self.name))

class SportsCar(Car):
    pass

class WorkCar(Car):
    def indicate_speed(self):
        print('{} current speed is {} '.format(self.name, self.speed))
        if self.speed > 40:
            print('Alert!! {} speed exceeds allowed maximum!'.format(self.name))

class PoliceCar(Car):
    pass

sports_car = SportsCar(220, 'Cherry Red', 'Ferrari', False)
town_car = TownCar(150, 'Brisbane Gray', 'Ford Mondeo', False)
work_car = WorkCar(80, 'Green', 'Hyundai Porter', False)
police_car = PoliceCar(205, 'Blue-and-White', 'Range Rover', True)

sports_car.indicate_speed()
town_car.indicate_speed()
work_car.indicate_speed()
police_car.indicate_speed()

sports_car.turn('right')
work_car.turn('left')
town_car.go(90)
police_car.stop()