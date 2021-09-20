"""
Найти сумму элементов матрицы, лежащих выше главной диагонали.

---------------
элемент расположен на главной диагонали, если i == j
"""
matrix = [[1, 4, 6],
          [6, 3, 0],
          [2, 9, 4]]

sum = 0

for i in range(0, len(matrix)):
    print(f"i = {i}")
    for j in range(i+1, len(matrix[i])):
        print(f"j = {j}")
        sum += matrix[i][j]

print(sum)
