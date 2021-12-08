"""
Дана точка M с координатами (x, y). Определить месторасположение этой точки в декартовой системе координат:
- является началом координат
- лежит на одной из координатных осей
- расположена в одном из координатных углов
"""

m = (0, 0)

if m[0] == 0 and m[1] == 0:
    print('Начало координат')
elif m[0] == 0:
    print('Лежит на оси OY')
elif m[1] == 0:
    print('Лежит на оси OX')
else:
    print('Лежит в одном из координатных углов')