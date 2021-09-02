'''
Тема 3: “Числовой тип данных”
1.	Написать программу для вычисления значения выражений. Проверить правильность
выполнения задания с помощью тестовых значений.
'''
import math
# from math import *

a = 100

y1 = ((1 + a + a**2) / (2*a + a**2) + 2 - (1 - a + a**2) / (2*a - a**2))**-1 * (5 - 2*a**2)

print(y1)

a = math.radians(60)
b = math.radians(60)
y = math.radians(60)
y2 = 1/4 * (math.sin(a + b - y) + math.sin(b + y - a) + math.sin(y + a - b) - math.sin(a + b + y))

print(y2)