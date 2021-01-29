#  Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#  name, surname, position (должность), income (доход).
#  Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
#  оклад и премия, например, {"wage": wage, "bonus": bonus}.
#  Создать класс Position (должность) на базе класса Worker.
#  В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#  и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры класса Position,
#  передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wages = income['wages']
        self._income_bonus = income['bonus']

class Position(Worker):

    def get_full_name(self):
        return f'{self.surname} {self.name} - {self.position}'

    def get_total_income(self):
        return self._income_wages + self._income_bonus

person_1 = Position('Natalia', 'Freiburg', 'Deputy Director', {'wages': 140000, 'bonus': 35000})
print(person_1.get_full_name())
print(person_1.get_total_income())

person_2 = Position('Евгений', 'Долгих', 'Исполнительный Директор', {'wages': 200000, 'bonus': 45000})
print(person_2.get_full_name())
print(person_2.get_total_income())

person_3 = Position('Александр', 'Пушкин', 'Поэт', {'wages': 70000, 'bonus': 25000})
print(person_3.get_full_name())
print(person_3.get_total_income())
