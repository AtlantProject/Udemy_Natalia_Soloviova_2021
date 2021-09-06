"""
Написать программу, которая будет конвертировать значение температуры
из градусов Цельсия в Фаренгейты и наоборот.
Входные данные: 60C, 45F, ….
Результат: 140F, 7C, ….
Расчетные формулы:

c = (F-32) * 5/9
F = C * 9/5 + 32

______________
Тестовые значения:
60С     140F
90C     194F
100c    212F

45F     7.22С
90F     32.22С
125f    51.67С

50a     wrong value
"""

t = '50a'

suffix = t[-1]
val = int(t[:-1])

if suffix in ['C', 'c']:
    conv_val = val*9/5 + 32
    res = str(round(conv_val, 2)) + "F"
elif suffix in ['F', 'f']:
    conv_val = (val-32)*5/9
    res = str(round(conv_val, 2)) + "C"
else:
    res = 'wrong value'

print(t, ' is ', res)
