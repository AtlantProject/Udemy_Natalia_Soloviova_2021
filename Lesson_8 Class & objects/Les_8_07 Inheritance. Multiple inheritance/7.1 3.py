"""
Создать класс “Окружность”, свойство - радиус, методы - вычисление площади круга и длины окружности,
вывод информации о фигуре.

Создать класс “Прямоугольник”, свойства - длины сторон, методы -
вычисление периметра и площади прямоугольника, вывод информации о фигуре.

Создать производный от них класс “Цилиндр”, свойства - радиус основания и высота, методы -
вычисление объема цилиндра, вывод информации о фигуре.

Написать программу, демонстрирующую работу с классом:
дано N окружностей, M прямоугольников и K цилиндров, найти окружность с наибольшей площадью, прямоугольник
с наименьшим периметром и средний объем всех цилиндров.
"""
from math import pi


class Circle():
    def __init__(self, r):
        self.r = r

    def get_circle_square(self, to_print=True):
        s = pi * self.r ** 2
        if to_print:
            print(f'Square: {s}')
        return s

    def get_circle_circumference(self, to_print=True):
        l = 2 * pi * self.r
        if to_print:
            print(f'Circumference: {l}')
        return l

    def print_circle(self):
        print(f'radius = {self.r}')


class Rectangle():
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def get_rect_perimeter(self):
        p = 2 * (self.l + self.h)
        print(f'Perimeter: {p}')
        return p

    def get_rect_square(self):
        s = self.l * self.h
        print(f'Square: {s}')
        return s

    def print_rect(self):
        print(f'sides: {self.l}, {self.h}')


class Cylinder(Circle, Rectangle):
    def __init__(self, r, h):
        Circle.__init__(self, r)
        Rectangle.__init__(self, self.get_circle_circumference(to_print=False), h)

    def get_volume(self):
        v = self.get_circle_square(to_print=False) * self.h
        print(f'Volume: {v}')
        return v

    def print_cylinder(self):
        print(f'base: {self.r}, height: {self.h}')


circles = [Circle(4), Circle(2), Circle(6), Circle(8), Circle(1)]
rects = [Rectangle(3, 7), Rectangle(2, 7), Rectangle(19, 12)]
cylinders = [Cylinder(4, 7), Cylinder(2, 5), Cylinder(9, 3), Cylinder(5, 5)]

circle_max_s = max(circles, key=lambda c: c.get_circle_square())
rect_min_p = min(rects, key=lambda r: r.get_rect_perimeter())

cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
cylinders_v_avg = sum(cylinders_v) / len(cylinders_v)

print('*'*50)
print('Max square circle:', end=' ')
circle_max_s.print_circle()

print('Min perimeter rectrangle:', end=' ')
rect_min_p.print_rect()

print(f'Avg cylinders volume: {cylinders_v_avg:.2f}')

