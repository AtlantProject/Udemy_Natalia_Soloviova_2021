"""
ДЗ № 3.4
Сколько решений имеет уравнение
¬((a ˄ ¬b) ˅ (¬a ˄ b)) ˅ (c ^ d) = 1

a   b   c   d   f
0   1   1   1
0   1   1   0
0   1   0   1
0   1   0   0
0   0   1   1
0   0   1   0
0   0   0   1
0   0   0   0
1   1   1   1
1   1   1   0
1   1   0   1
1   1   0   0
1   0   1   1
1   0   1   0   -
1   0   0   1
1   0   0   0

¬ - not   ˅ - or    ˄ - and
"""
a = 0
b = 1
c = 1
d = 1

f = not((a and not b) or (not a and b)) or (c and d) == 1

print(f)

'''
# Попытка решения в автоматическом режиме

events = {a: [0, 1],
          b: [0, 1],
          c: [0, 1],
          d: [0, 1]
          }

for key, values in events.items():
    if not((a and not b) or (not a and b)) or (c and d) == 1:
        print(key, values)

'''