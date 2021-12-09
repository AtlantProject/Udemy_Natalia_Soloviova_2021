"""
------------
Тестовые значения:
2,4,6 -> 88
5,8,2 -> 132
1,6,8 -> 124
"""
# нелокальная переменная

def rect_paral_square(a, b, c):
    s = 0

    def add_rect_square(i, j):
        nonlocal s
        s += i*j

    add_rect_square(a, b)
    add_rect_square(a, c)
    add_rect_square(c, b)
    return 2*s


print(rect_paral_square(2,4,6))
print(rect_paral_square(5,8,2))
print(rect_paral_square(1,6,8))