"""
Класс Liquid.

Методы:

edit_density - редактировать плотность жидкости
calc_v - вычислить объем жидкости заданной массы
calc_m - вычислить массу жидкости заданного объема
print_info - вывести информацию о жидкости
"""

class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def edit_density(self, val):
        self.density = val

    def calc_v(self, m):
        v = round(m / self.density, 2)
        print(f'The volume of {m} kg of {self.name} is {v} m^3.')
        return v

    def calc_m(self, v):
        m = v * self.density
        print(f'The weight of {v} m^3 of {self.name} is {m} kg.')
        return m

    def print_info(self):
        print(f'Liquid {self.name!r} (density = {self.density} kg/m^3).')


__author__ = 'Natalia S.'

if __name__ == "Liquid":
    print(f'Module {__name__!r} (author: {__author__}) was imported.')