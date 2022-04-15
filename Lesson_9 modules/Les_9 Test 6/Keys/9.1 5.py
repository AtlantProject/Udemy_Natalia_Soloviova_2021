"""
Используя модуль random сформируйте случайным образом две матрицы A(m, n) и B(k, l).
В матрице A найдите максимальный элемент, находящийся на периметре матрицы,
а в матрице B - минимальный элемент вне периметра.
Вычислите среднее геометрическое найденных элементов.
"""
import random
from math import sqrt


def get_matrix(row_num, col_num):
    m = []
    for i in range(0, row_num):
        row = []
        for j in range(0, col_num):
            row.append(random.randrange(100))
        m.append(row)
    return m


def print_matrix(m):
    for row in m:
        print(row)
    print()


def get_max_on_perim(m, row_num, col_num):
    first_row = m[0]
    last_row = m[row_num-1]
    first_col = [row[0] for row in m]
    last_col = [row[col_num-1] for row in m]

    # print(first_row, last_row, first_col, last_col)

    max_elem = max(*first_row, *last_row, *first_col, *last_col)
    return max_elem


def get_min_out_perim(m, row_num, col_num):
    min_elem = 100
    for i in range(1, row_num-1):
        for j in range(1, col_num-1):
            if m[i][j] <  min_elem:
                min_elem = m[i][j]
    return min_elem


m = 5
n = 4
A = get_matrix(m, n)
print_matrix(A)
max_A = get_max_on_perim(A, m, n)
print(f'Max elem on perimeter (matrix A): {max_A}')

k = 6
l = 8
B = get_matrix(k, l)
print_matrix(B)
min_B = get_min_out_perim(B, k, l)
print(f'Min elem out of perimeter (matrix B): {min_B}')

sr_geom = sqrt(max_A * min_B)
print(f'Sr. geom. of {max_A} and {min_B} is {sr_geom:.2f}')
