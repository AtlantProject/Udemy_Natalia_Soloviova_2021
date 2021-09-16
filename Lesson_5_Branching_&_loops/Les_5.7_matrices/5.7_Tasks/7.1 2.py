"""
Вычислить количество положительных элементов квадратной матрицы,
расположенных по ее периметру и на диагоналях.

---------
главная диагональ i == j
побочная диагональ i + j + 1 == N

первая строка   0,i
последняя строка    N-1, i

первый столбец  i, 0
последний столбец   i, N-1
"""

matrix = [[1, -4, 6, 5],
          [-6, 3, 0, -8],
          [2, 9, -4, 2],
          [-3, 6, -1, 9]]

k = 0
N = len(matrix)

for i in range(0, N):
    if matrix[i][i] > 0:
        k += 1
    if matrix[i][N-i-1] > 0:
        k += 1
    if 0 < i < N-1:
        if matrix[0][i] > 0:
            k += 1
        if matrix[N-1][i] > 0:
            k += 1
        if matrix[i][0] > 0:
            k += 1
        if matrix[i][N-1] > 0:
            k += 1

if N % 2 != 0 and matrix[N//2][N//2] > 0:
    k -= 1

print(k)
