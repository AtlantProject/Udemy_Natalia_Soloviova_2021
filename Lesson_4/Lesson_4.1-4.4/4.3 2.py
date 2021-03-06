"""
Написать программу расчета y и z по формулам, приведенным ниже.
Определить разность между значениями  y и z в каждом случае.

y = V(2b+2*V(b^2 - 4)) / (v(b^2-4) + b + 2)

z = 1 / v(b+2)

-------------------
Тестовые значения:
b         Y           Z           Y - Z
10      0.289       0.289           0
50      0.139       0.139           0
100     0.099       0.099           0
"""

import math

b = 100

y = math.sqrt(2*b + 2*math.sqrt(b**2 - 4))/(math.sqrt(b**2 - 4) + b + 2)
print('y={:.2f}'.format(y))

z = 1 / math.sqrt(b + 2)
print('z={:.2f}'.format(z))

print('y-z={:.2f}'.format(y-z))