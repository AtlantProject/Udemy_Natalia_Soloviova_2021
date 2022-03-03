"""
В созданном классе “Цилиндр” переопределить методы вычисления площади и вывода информации о фигуре.

Написать программу, демонстрирующую работу с классом: дано N цилиндров, вывести их среднюю площадь,
а также информацию о цилиндрах с площадью, равной средней площади (если таковые имеются).

"""
from math import pi


class Circle():
    def __init__(self, r):
        self.r = r

    def get_square(self, to_print=True):
        s = pi * self.r ** 2
        if to_print:
            print(f'Square: {s}')
        return s

    def get_circle_circumference(self, to_print=True):
        l = 2 * pi * self.r
        if to_print:
            print(f'Circumference: {l}')
        return l

    def print_info(self):
        print(f'radius = {self.r}')


class Rectangle():
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def get_rect_perimeter(self):
        p = 2 * (self.l + self.h)
        print(f'Perimeter: {p}')
        return p

    def get_square(self, to_print=True):
        s = self.l * self.h
        if to_print:
            print(f'Square: {s}')
        return s

    def print_info(self):
        print(f'sides: {self.l}, {self.h}')


class Cylinder(Circle, Rectangle):
    def __init__(self, r, h):
        Circle.__init__(self, r)
        Rectangle.__init__(self, self.get_circle_circumference(to_print=False), h)

    def get_volume(self):
        v = Circle.get_square(self, to_print=False) * self.h
        print(f'Volume: {v}')
        return v

    def print_info(self):
        print(f'base: {self.r}, height: {self.h}')

    def get_square(self):
        s = 2 * Circle.get_square(self, to_print=False) + Rectangle.get_square(self, to_print=False)
        print(f'Square: {s}')
        return s


# cylinders = [Cylinder(4, 7), Cylinder(2, 5), Cylinder(9, 3), Cylinder(5, 5)]
cylinders = [Cylinder(2, 5), Cylinder(2, 5), Cylinder(2, 5)]
s_cylinders = list(map(lambda c: c.get_square(), cylinders))
avg_s = sum(s_cylinders) / len(s_cylinders)

eq_avg_s = list(filter(lambda c: avg_s == c.get_square(), cylinders))

print('*'*50)
# print(s_cylinders)
print(f'Avg square: {avg_s}')
if not eq_avg_s:
    print('no such cylinders')
else:
    print('Cylinders with avg square:')
    for c in eq_avg_s:
        c.print_info()


