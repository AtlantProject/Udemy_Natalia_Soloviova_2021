"""
В файле mtrxs.txt хранятся матрицы A(n, m) и B(m, k).
При этом в первой строке хранятся числа n и m, затем построчно матрица A,
затем строка со значениями m и k, и далее построчно матрица B.
Найти матрицу C=A*B и записать ее в файл rez.txt в том же формате.

----------
Ответ:
180 44
120 54
104 25
"""
input_file_name = 'mtrxs.txt'
output_file_name = 'rez.txt'

def read_matrix(rows_num, f):
    m = []
    for i in range(0, rows_num):
        line = f.readline()
        nums = list(map(int, line.split()))
        m.append(nums)
    return m

with open(input_file_name, 'r') as f:
    n, m = f.readline().split()     # n, m - strings
    A = read_matrix(int(n), f)
    m, k = f.readline().split()     # m, k - strings
    B = read_matrix(int(m), f)

print(A)
print(B)

C = []

for i in range(0, int(n)):
    row = []
    for j in range(0, int(k)):
        c_ij = 0
        for l in range(0, int(m)):
            c_ij += A[i][l]*B[l][j]
        row.append(c_ij)
    C.append(row)

print(C)

lines = [f'{n} {k}\n']
for row in C:
    line = ' '.join(map(str, row))
    lines.append(f'{line}\n')

with open(output_file_name, 'w') as f:
    f.writelines(lines)
