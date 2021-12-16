"""
Добавьте строки документации в каждую из написанных функций.
"""

# глобальная переменная
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
        s += i * j

    add_rect_square(a, b)
    add_rect_square(a, c)
    add_rect_square(c, b)
    return 2*s


print(rect_paral_square(2, 4, 6))
print(rect_paral_square(5, 8, 2))
print(rect_paral_square(1, 6, 8))