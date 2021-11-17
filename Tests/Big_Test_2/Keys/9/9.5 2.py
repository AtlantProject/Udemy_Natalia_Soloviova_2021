"""
Выяснить, пересекаются ли параболы y = ax^2 + bx + c и y = dx^2 + ex + f.
Если да, найти точки пересечения.

----------------
Тестовые значения:
y = 2x^2 - x -3
y = x^2 - x + 1

(2,3), (-2, 7)
"""
import math

# ax^2 + bx + c == dx^2 + ex + f
# ax^2-dx^2 + bx - ex + c - f == 0
# x^2(a-d) + x(b-e) + (c-f) == 0
# A = a-d, B = b-e, C = c-f

a = 2
b = -1
c = -3
d = 1
e = -1
f = 1

# Ax^2 + Bx + C = 0
A = a - d
B = b - e
C = c - f

D = B**2 - 4*A*C
if D >= 0:
    x1 = (B + math.sqrt(D)) / (2 * A)
    y1 = a*x1**2 + b*x1 + c
    x2 = (B - math.sqrt(D)) / (2 * A)
    y2 = a * x2 ** 2 + b * x2 + c
    print(x1, y1)
    print(x2, y2)
else:
    print('Параболы не пересекаются')

