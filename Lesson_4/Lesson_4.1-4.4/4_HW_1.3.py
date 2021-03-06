"""
Написать программу расчета y и z по формулам, приведенным ниже.
Определить разность между значениями  y и z в каждом случае.

y = 2*sin^2(3Pi-2a)*cos^2(5Pi+2a)

z = 1/4 - 1/4 * sin(5/2 * Pi - 8a)

-------------------
Тестовые значения:
Grad        Rad         Y           Z           Y - Z
a = 0       0           0           0           0
a = 30      0.52       0.38         0.38        0
a = 60      1.05       0.38         0.38        0
a =90       1.57       0.000..      0.000..     0
a = 180     3.14        0           0           0
"""

import math

y = (math.log2(8) + math.log2(18))/(2*math.log2(2) + math.log2(3))

print('y={:.3f}'.format(y))
