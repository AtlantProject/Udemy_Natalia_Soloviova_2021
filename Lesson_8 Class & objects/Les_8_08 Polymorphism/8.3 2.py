"""
В созданном классе “Равносторонний треугольник” переопределить  проверку,
является ли треугольник равносторонним, а также методы вычисления углов и
вывода сведений о фигуре.

Написать программу, демонстрирующую работу с классом:
дано N треугольников, проверить каждый их них, является ли он равносторонним,
и вывести равносторонний треугольник с наибольшим периметром.

"""
from math import acos, degrees, sqrt, pi


class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_info(self):
        return f'\u25b3ABC ({self.a}, {self.b}, {self.c})'

    def exists(self):
        if (self.a + self.b > self.c) \
                and (self.a + self.c > self.b) \
                and (self.b + self.c > self.a):
            print(f'{self.get_info()} exists.')
            return True

        print(f'{self.get_info()} does not exist.')
        return False

    def get_sides(self):
        print(f'Sides: {self.a}, {self.b}, {self.c}')
        return self.a, self.b, self.c

    def get_angles(self):
        ac = acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))
        ab = acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))
        cb = acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))

        print(f'\u2220CAB: {ac:.2f} Rad, {degrees(ac):.2f} Grad')
        print(f'\u2220ABC: {ab:.2f} Rad, {degrees(ab):.2f} Grad')
        print(f'\u2220BCA: {cb:.2f} Rad, {degrees(cb):.2f} Grad')

        return ac, ab, cb

    def get_perimeter(self, to_print=True):
        p = self.a + self.b + self.c
        if to_print:
            print(f'Perimeter: {p}')
        return p

    def get_square(self):
        p = self.get_perimeter(to_print=False) / 2
        s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f'Square: {s:.2f}')
        return s

    def is_equilateral(self):
        is_eq = self.a == self.b == self.c
        print(f'Is equilateral: {is_eq}')
        return is_eq


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)

    def is_equilateral(self):
        print('Is is equilateral.')
        return True

    def get_angles(self):
        angle = pi/3
        print(f'\u2220CAB == \u2220ABC == \u2220BCA: {angle:.2f} Rad, {degrees(angle):.2f} Grad')

    def get_info(self):
        return f'\u25b3ABC: side = {self.a}'


tr = [Triangle(2, 5, 6), Triangle(2, 2, 2), Triangle(5, 2, 4), Triangle(7, 7, 7), Triangle(7, 3, 6), Triangle(4, 4, 4)]

p_max = 0
tr_p_max = None

for i in range(0, len(tr)):
    if tr[i].is_equilateral():
        tr[i] = EquilateralTriangle(tr[i].get_sides()[0])
        print(f'Triangle {tr[i].get_info()} is equilateral.')
        p = tr[i].get_perimeter()
        if p > p_max:
            p_max = p
            tr_p_max = tr[i]

print('*'*50)
print(f'Max perimeter: {p_max}')
print(f'Equilateral Triangle with max perimeter: {tr_p_max.get_info()}')

print()
print(tr[0].get_info())
tr[0].is_equilateral()
tr[0].get_angles()
print(tr[1].get_info())
tr[1].is_equilateral()
tr[1].get_angles()


