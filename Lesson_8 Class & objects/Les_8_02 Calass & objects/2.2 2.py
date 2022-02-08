"""
Определить класс “Вектор” со свойствами: 3 декартовы координаты (x, y, z), -
и методами: вывод вектора на экран, вычисление длины вектора и умножение вектора на число.

-------------
Тестовые значения:
(4, 12, 6) -> 14
(3, 7, 2) -> 7.87
"""
from math import sqrt


class Vector():
    x = 4
    y = 12
    z = 6

    def print(self):
        print(f'Vector({self.x}; {self.y}; {self.z})')

    def get_length(self):
        # len(v) = v(x^2 + y^2 + z^2)
        length = sqrt(self.x**2 + self.y**2 + self.z**2)
        return round(length, 2)

    def multiply(self, num):
        self.x *= num
        self.y *= num
        self.z *= num
        print('New vector: ')
        self.print()

v = Vector()
v.print()
print(f'Module: {v.get_length()}')
v.multiply(5)
v.multiply(3)