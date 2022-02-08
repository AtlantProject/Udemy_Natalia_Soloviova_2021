"""
Измените класс “Вектор” следующим образом:
- добавьте статическое свойство - точка отсчета (x1, y1, z1), -
имеющее одинаковое значение для всех объектов класса;
- три существующие свойства - декартовы координаты (x, y, z) -
“превратите” в одно динамическое свойство - конец вектора (x2, y2, z2), -
устанавливаемое в новом методе определения вектора;
- внесите соответствующие изменения в методы класса.

-------------
Тестовые значения:
(4, 12, 6) -> 14
(3, 7, 2) -> 7.87
"""
from math import sqrt


class Vector():
    start_point = (1, 1, 5)

    def set(self, x, y, z):
        self.end_point = (x, y, z)
        # вычисляем координаты вектора, исходя из координат точек начала и конца
        self.x = x - Vector.start_point[0]
        self.y = y - Vector.start_point[1]
        self.z = z - Vector.start_point[2]

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


v1 = Vector()
v1.set(4, 12, 6)
v1.print()
print(f'Module: {v1.get_length()}')
v1.multiply(5)
v1.multiply(3)

print()
v2 = Vector()
v2.set(3, 7, 2)
v2.print()
print(f'Module: {v2.get_length()}')
v2.multiply(5)
v2.multiply(3)