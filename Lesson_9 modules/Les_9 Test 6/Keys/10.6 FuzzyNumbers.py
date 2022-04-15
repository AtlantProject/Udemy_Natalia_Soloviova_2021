"""
Class 'FuzzyNumbers'
"""
from Pair import Pair


class FuzzyNumbers(Pair):
    def __init__(self, A, a, B, b):
        super().__init__(A, B)
        self.a = a
        self.b = b

    def sum(self):
        l = (self.A - self.a) + (self.B - self.b)
        c = self.A + self.B
        r = (self.A + self.a) + (self.B + self.b)
        print(f'A({self.A - self.a}, {self.A}, {self.A + self.a}) + '
              f'B({self.B - self.b}, {self.B}, {self.B + self.b}) = '
              f'C({l}, {c}, {r})')
        return l, c, r

    def minus(self):
        l = (self.A - self.a) - (self.B - self.b)
        c = self.A - self.B
        r = (self.A + self.a) - (self.B + self.b)
        print(f'A({self.A - self.a}, {self.A}, {self.A + self.a}) - '
              f'B({self.B - self.b}, {self.B}, {self.B + self.b}) = '
              f'C({l}, {c}, {r})')
        return l, c, r

    def mult(self):
        l = (self.A - self.a) * (self.B - self.b)
        c = self.A * self.B
        r = (self.A + self.a) * (self.B + self.b)
        print(f'A({self.A - self.a}, {self.A}, {self.A + self.a}) * '
              f'B({self.B - self.b}, {self.B}, {self.B + self.b}) = '
              f'C({l}, {c}, {r})')
        return l, c, r

    def div(self):
        l = (self.A - self.a) / (self.B - self.b)
        c = self.A / self.B
        r = (self.A + self.a) / (self.B + self.b)
        print(f'A({self.A - self.a}, {self.A}, {self.A + self.a}) / '
              f'B({self.B - self.b}, {self.B}, {self.B + self.b}) = '
              f'C({l:.2f}, {c:.2f}, {r:.2f})')
        return l, c, r


__author__ = 'Natalia S.'
if __name__ == "FuzzyNumbers":
    print(f'Module {__name__!r} (author: {__author__}) was imported.')