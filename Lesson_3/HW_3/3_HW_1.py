'''
ДЗ № 3.1
Укажите значение логических переменных K, L, M, N,
при которых значение логического выражения
(НЕ K ИЛИ M) ИЛИ (НЕ L ИЛИ M ИЛИ N)
будет ложным.
2^4=16
K   L   M   N   f
0   1   1   1   +
0   1   1   0   +
0   1   0   1   +
0   1   0   0   +
0   0   1   1   +
0   0   1   0   +
0   0   0   1   +
0   0   0   0   +
1   1   1   1   +
1   1   1   0   +
1   1   0   1   +
1   1   0   0   -
1   0   1   1
1   0   1   0
1   0   0   1
1   0   0   0
'''

K = 1
L = 1
M = 0
N = 0

f = (not K or M) or (not L or M or N)
print(f)
