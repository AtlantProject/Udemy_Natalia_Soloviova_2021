"""
Написать функцию, вычисляющую площадь прямоугольного параллелепипеда с ребрами a, b и c.
Данная функция должна содержать внутри себе еще одну функцию, вычисляющую площадь прямоугольника.
Решить задачу для случаев, когда общая площадь определена как глобальная и как локальная переменная.
Внести изменения в функции таким образом, чтобы общая площадь могла использоваться как нелокальная переменная.

------------
Тестовые значения:
2,4,6 -> 88
5,8,2 -> 132
1,6,8 -> 124
"""
# глобальная переменная
s = 0

def rect_paral_square(a, b, c):

    def rect_square(i, j):
        return i * j

    global  s
    s = 2*(rect_square(a, b) + rect_square(a, c) + rect_square(c, b))


rect_paral_square(2, 4, 6)
print(s)
rect_paral_square(5, 8, 2)
print(s)
rect_paral_square(1, 6, 8)
print(s)
