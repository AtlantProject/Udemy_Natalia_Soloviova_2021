"""
Создать класс “Квадрат”, свойства - длина стороны.
Предусмотреть в классе методы вычисления и вывода сведений о фигуре - диагональ, периметр, площадь.

Создать производный класс “Правильная квадратная призма”, свойство - высота.
Добавить в класс метод определения объема фигуры.
Написать программу, демонстрирующую работу с этими классами: дано N квадратов и M призм,
найти квадрат с максимальной диагональю и призму с минимальным объемом.
"""
from math import sqrt


class Square():
    def __init__(self, side):
        self.side = side

    def calc_diagonal(self):
        d = round(self.side * sqrt(2), 2)
        print(f'Diagonal: {d}')
        return d

    def calc_perimeter(self):
        p = 4 * self.side
        print(f'Perimeter: {p}')
        return p

    def calc_square(self):
        s = self.side ** 2
        print(f'Square: {s}')
        return s

    def get_square(self):
        return f'Square: side = {self.side}'

class RegualrSqPrism(Square):
    def __init__(self, side, height):
        super().__init__(side)
        self.height = height

    def calc_volume(self):
        v = self.side ** 2 * self.height
        print(f'Volume: {v}')
        return v

    def get_prism(self):
        return f'Regular square prisma: base side = {self.side}, height = {self.height}'


squares = [Square(4), Square(8), Square(2), Square(5), Square(3)]
prisms = [RegualrSqPrism(3, 5), RegualrSqPrism(2, 8), RegualrSqPrism(9, 4)]

max_diag_square = max(squares, key=lambda sq: sq.calc_diagonal())
min_vol_prism = min(prisms, key=lambda pr: pr.calc_volume())

print('*'*50)
print(f'The square with max diagonal: {max_diag_square.get_square()}')
print(f'The prism with min volume: {min_vol_prism.get_prism()}')
