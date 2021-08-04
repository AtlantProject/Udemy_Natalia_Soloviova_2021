"""
Дан фрагмент таблицы истинности. Какая из трех приведенных функций соответствует этому фрагменту:
1. (¬ X1 ˅ X2) ˄ ¬ X3 ˅ X4
2. (¬ X1 ˄ X2) ˅ (¬X3 ˄ X4)
3. ¬ X1 ˅ X2 ˅ (X3 ˄ X4)

x1  x2  x3  x4  F
1   1   0   0   1
0   1   1   1   1
1   0   0   1   0

¬ - not   ˅ - or    ˄ - and
"""
x1 = 1
x2 = 0
x3 = 0
x4 = 1

f1 = (not x1 or x2) and not x3 or x4
f2 = (not x1 and x2) or (not x3 and x4)
f3 = not x1 or x2 or (x3 and x4)

print('f1=', f1)
print('f2=', f2)
print('f3=', f3)