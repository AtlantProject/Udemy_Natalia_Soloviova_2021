"""
В созданном классе “Правильная квадратная призма” переопределить методы вычисления площади,
диагонали и вывода сведений о фигуре.

Написать программу, демонстрирующую работу с классом:
дано N призм, вывести призму с наибольшей площадью и наименьшей диагональю.

"""
from math import sqrt


class Square():
    def __init__(self, side):
        self.side = side

    def calc_diagonal(self, to_print=True):
        d = round(self.side * sqrt(2), 2)
        if to_print:
            print(f'Diagonal: {d}')
        return d

    def calc_perimeter(self):
        p = 4 * self.side
        print(f'Perimeter: {p}')
        return p

    def calc_square(self, to_print=True):
        s = self.side ** 2
        if to_print:
            print(f'Square: {s}')
        return s

    def get_info(self):
        return f'Square: side = {self.side}'

class RegualrSqPrism(Square):
    def __init__(self, side, height):
        super().__init__(side)
        self.height = height

    def calc_volume(self):
        v = self.side ** 2 * self.height
        print(f'Volume: {v}')
        return v

    def get_info(self):
        return f'Regular square prisma: base side = {self.side}, height = {self.height}'

    def calc_square(self):
        s = 2 * super().calc_square(to_print=False) + 4 * self.side * self.height
        print(f'Square: {s}')
        return s

    def calc_diagonal(self):
        d = sqrt(self.height ** 2 + super().calc_diagonal(to_print=False))
        print(f'Diagonal: {d}')
        return d


prisms = [RegualrSqPrism(3, 5), RegualrSqPrism(2, 8), RegualrSqPrism(9, 15)]
max_s_prism = max(prisms, key=lambda pr: pr.calc_square())
min_d_prism = min(prisms, key=lambda pr: pr.calc_diagonal())

print('*'*50)
print(f'The prism with max sqiare: {max_s_prism.get_info()}')
print(f'The prism with min diagonal: {min_d_prism.get_info()}')
