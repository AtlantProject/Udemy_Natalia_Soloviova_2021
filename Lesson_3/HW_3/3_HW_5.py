"""
ДЗ № 3.5


c - Саша
v - Ваня
k - Коля
d - Дома    not d - не дома

2^4 = 16


каждый раз уменьшаем блоки 0 и 1 в два раза

c   v   k   d   f
0   0   0   0   -
0   0   0   1   -
0   0   1   0   -
0   0   1   1   -
0   1   0   0   -
0   1   0   1   -
0   1   1   0   -
0   1   1   1   -
1   0   0   0   -
1   0   0   1   -
1   0   1   0   -
1   0   1   1   -
1   1   0   0   -
1   1   0   1   -
1   1   1   0   -
1   1   1   1   -

2^3=8
c   v   k   f
0   0   0   -
0   0   1   -
0   1   0   -
0   1   1   -
1   0   0   -
1   0   1   -
1   1   0   -
1   1   1   -

"""
c = 1
v = 1
k = 1
# d = 1

f1c = (not k and v) or (k and not v)
f2v = (not c and k) or (c and not k)
f3k = (not v and c) or (v and not c)

f4 = (c and not v and not k) or (not c and v and not k) or (not c and not v and k)

f = f1c and f2v and f3k and f3k and f4
print('f =', f)

print('Саша: ', c)
print('Ваня: ', v)
print('Коля: ', k)


# Коля




