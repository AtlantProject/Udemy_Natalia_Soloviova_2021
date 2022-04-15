"""
Модуль Alcohol.

Методы:

edit_strength - редактировать крепость алкоголя.
calc_v - вычислить объем жидкости заданной массы и содержащегося в ней алкоголя
calc_m - вычислить массу жидкости заданного объема и содержащегося в ней алкоголя
print_info - вывести информацию об алкоголе.
"""

from Liquid import Liquid


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength        # max = 1 (100%)

    def edit_strength(self, val):
        self.strength = val

    def calc_v(self, m):
        v = super().calc_v(m)
        v_alc = round(v * self.strength, 2)
        print(f'The volume of alcohol in {m} kg of {self.name} is {v_alc} m^3.')
        return v, v_alc

    def calc_m(self, v):
        m = super().calc_m(v)
        m_alc = round(m * self.strength, 2)
        print(f'The weight of alcohol in {v} m^3 of {self.name} is {m_alc} kg.')
        return m, m_alc

    def print_info(self):
        print(f'Liquid {self.name!r} (density = {self.density} kg/m^3, strength = {self.strength:.0%}).')


__author__ = 'Natalia S.'

if __name__ == "Alcohol":
    print(f'Module {__name__!r} (author: {__author__}) was imported.')