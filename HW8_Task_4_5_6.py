# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники

# # Продолжить работу над первым заданием.
# # Разработать методы, отвечающие за приём оргтехники на склад и передачу
# # в определенное подразделение компании.
# # Для хранения данных о наименовании и количестве единиц оргтехники,
# # а также других данных, можно использовать любую подходящую структуру, например словарь.

# # Продолжить работу над вторым заданием.
# # Реализуйте механизм валидации вводимых пользователем данных.
# # Например, для указания количества принтеров, отправленных на склад,
# # нельзя использовать строковый тип данных.
# # Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# # максимум возможностей, изученных на уроках по ООП.

class Warehouse:

        def __init__(self):
            self._dict = {}

        def add_to(self, equipment):
            # добавляем в словарь обьект по его названию, в значении
            # будет список экземпляров этого оборудования
            self._dict.setdefault(equipment.group_name(), []).append(equipment)

        def extract(self, name):
            # извлекаем из значения обьект по названию группы.
            # дальше можно расширить поиск по серии, марки или еще чему либо
            if self._dict[name]:
                x = self._dict.setdefault(name).pop(0)
                print('{} отправляется заказчику'.format(x))

class Equipment:

        def __init__(self, name, serial_num, make, year,):
            self.name = name
            self.make = make
            self.year = year
            self.serial_num = serial_num
            self.group = self.__class__.__name__


        def group_name(self):
                return f'{self.group}'

        def __repr__(self):
            return f'{self.name} {self.serial_num} {self.make} {self.year}'

class Printer(Equipment):

        def __init__(self, name, serial_num, make, year):
            super().__init__(name, serial_num, make, year)
            self.name = name
            self.serial_num = serial_num
            self.make = make
            self.year = year

        def __repr__(self):
            return f'{self.name} {self.serial_num} {self.make} {self.year}'

        def action(self):
            return 'Принтер печатает'

class Scanner(Equipment):

        def __init__(self, name, serial_num, make, year):
            super().__init__(name, serial_num, make, year)
            self.name = name
            self.serial_num = serial_num
            self.make = make
            self.year = year

        def action(self):
            return 'Сканер сканирует'

class Xerox(Equipment):

        def __init__(self, name, serial_num, make, year):
            super().__init__(name, serial_num, make, year)
            self.name= name
            self.serial_num = serial_num
            self.make = make
            self.year = year

        def action(self):
            return 'Ксерокс Копирует'

sklad = Warehouse()
# создаем объекты и добавляем в словарь склад
scanner = Scanner('HP', 99811347, '321', 2016)
sklad.add_to(scanner)
scanner = Scanner('Canon', 10714135, '311', 2013)
sklad.add_to(scanner)
scanner = Scanner('Sony', 11909090, '330', 2015)
sklad.add_to(scanner)
printer = Printer('Epson', 16161617, '112', 2017)
sklad.add_to(printer)
xerox = Xerox('LG', 13232324, '400', 2017)
sklad.add_to(xerox)
# выводим словарь склад
print(sklad._dict)
# забираем со склада и выводим склад
sklad.extract('Scanner')
print()
print(sklad._dict)
