from math import sqrt

a = 1
b = -14
c = 15
# y = x**2
# находим дискриминант D
D = b**2 - 4*a*c
if D >= 0:
    y1 = (-b + sqrt(D)) / (2 * a)
    y2 = (-b - sqrt(D)) / (2 * a)
    print(round(y1, 2), round(y2, 2))
    if (y1 and y2) < 0:
        print("Корней нет")
    elif y1 >= 0 and y1 >= 0:
        x1 = sqrt(y1)
        x2 = -x1
        x3 = sqrt(y2)
        x4 = -x3
        print(x1, x2, x3, x4)
    elif y1 >= 0:
        x1 = sqrt(y1)
        x2 = -x1
        print(x1, x2)
    elif y2 >= 0:
        x1 = sqrt(y2)
        x2 = -x2
        print(x1, x2)
else:
    print("Корней нет")
