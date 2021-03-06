'''
Нахождение транспонированной матрицы
'''

# Здесь проходим наоборот от 01 - Внешний цикл по столбцам
# Внутренний цикл - по строкам
# Делается это чтобы найти транспонированную матрицу
# 1 проходим по первым элемента столбцов и превращаем
# результат в 1-й строку и т.д.

m = [[7, -13, 16],
     [0, 4, 2],
     [-5, 11, 4]]

# Создаем переменную, в которой будем находить результат - транспонированную матрицу

transposed_m = []

# Вычисляем количество строк и столбцов в нашей изначальной матрице
# При этом количество строк - это просто длина нашего списка
# количество столбцов - можно рассчитать как длину первого элемента списка
# Так как все элементы нашей матрицы должны быть списками одинаковой длины


# Выполняем проход по столбцам нашей матрицы
for j in range(len(m[0])):
    transposed_row = []     # Обнуляется после добавления в transposed_m?
    print(f"transposed_row = {transposed_row}")
    print(f"j = {j}")
    for row in m:
        print(f"row = {row}")
        print(f"row[j] = {row[j]}")
        transposed_row.append(row[j])
        print(f"transposed_row = {transposed_row}")
    transposed_m.append(transposed_row)
    print(f"transposed_m= {transposed_m}")

print(f"Итог - transposed_m= {transposed_m}")   # Обнуляется после добавления в transposed_m?





