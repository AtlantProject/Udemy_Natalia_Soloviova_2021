"""
Определить класс “Дробь” со свойствами: числитель и знаменатель, -
и методами: вывод дроби на экран, определение обратной дроби и сокращение дроби.
"""
class Fraction():
    numerator = 9
    denominator = 39

    def print(self):
        print('\u0332'.join(f'{self.numerator}  '))
        print(f'{self.denominator}')

    def get_reversed(self):
        print('The reversed fraction of')
        self.print()
        print('is: ')
        rev_fr = Fraction()
        rev_fr.numerator = self.denominator
        rev_fr.denominator = self.numerator
        rev_fr.print()

    def reduce(self):
        a = self.numerator
        b = self.denominator
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a

        if a != 1:
            print('The fraction')
            self.print()
            print('after reduction is: ')
            self.numerator //= a
            self.denominator //= a
            self.print()
        else:
            print('The fraction')
            self.print()
            print("can't be reduced!")


f1 = Fraction()
f1.print()
f1.get_reversed()
f1.reduce()