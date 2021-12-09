"""
Выберите любую документированную функцию и выведите на экран строки документации.
"""

def rect_paral_square(a, b, c):
    """
    Вычисляет площадь прямоугольного параллелепипеда с ребрами a, b, c
    :param a: значение ребра a
    :param b: значение ребра b
    :param c: значение ребра c
    :return: площадь s
    """
    s = 0

    def add_rect_square(i, j):
        nonlocal s
        s += i*j

    add_rect_square(a, b)
    add_rect_square(a, c)
    add_rect_square(c, b)
    return 2*s

print(rect_paral_square.__doc__)