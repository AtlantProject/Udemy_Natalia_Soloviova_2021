"""
Написать функцию, принимающую некоторую информацию о геометрической фигуре и
рассчитывающую площадь данной фигуры.


- Ромб с диагоналями d1 и d2 (s = (d1*d2) / 2)
- Квадрат со стороной c (s=c2)
- Трапеция с основаниями a,b и высотой h (s = ½ *(a+b)*h)
- Круг с радиусом r (s=Pi*r2)

------------------
Тестовые значения:
figure_type = 'rhombus', d1=10, d2=8        -> S = 40
figure_type = 'square', a=5                 -> S = 25
figure_type = 'trapezoid', a=12, b=3, h=6   -> S = 45
figure_type = 'circle', r=18                -> S = 1017
figure_type = 'unknown', a=1, b=2, c=3      -> invalid data
"""
from math import pi


def square(figure_type, **kwargs):
    if figure_type=='rhombus':
        return kwargs['d1']*kwargs['d2']/2

    if figure_type=='square':
        return kwargs['a']**2

    if figure_type=='trapezoid':
        return 1/2*(kwargs['a']+kwargs['b'])*kwargs['h']

    if figure_type=='circle':
        return pi*kwargs['r']**2

    return 'invalid data'


print(square(figure_type='rhombus', d1=10, d2=8))
print(square(figure_type='square', a=5))
print(square(figure_type='trapezoid', a=12, b=3, h=6))
print(square(figure_type='circle', r=18))
print(square(figure_type='unknown', a=1, b=2, c=3))