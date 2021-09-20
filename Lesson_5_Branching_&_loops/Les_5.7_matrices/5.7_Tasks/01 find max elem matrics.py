'''
Поиск максимального элемента матрицы
'''
# Во внешнем цикле проходим по строкам
# Во внутреннем цикле проходим по столбцам


m = [[1, 2, 3],
     [4, 5, 2],
     [8, 0, 3]]

max_elem = m[0][0]

# Обход матрицы через ИНДЕКСЫ (если нужен максимальный элемент С индексом)

i_max = j_max = 0   # i - индекс строки, j - индекс столбца

for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        if m[i][j] > max_elem:
            max_elem = m[i][j]
            i_max = i
            j_max = j

print(f"max_elem = {max_elem}")
print(f"i_max = {i_max}")
print(f"j_max = {j_max}")

# Обход матрицы через сами элементы (если нужен только максимальный элемент БЕЗ индексов)
# Код намного короче и его визуально удобнее воспринимать
# Индексы не запоминаем потому, что нам это не нудно

for row in m:
    for elem in row:
        if elem > max_elem:
            max_elem = elem

print(f"Max elem = {max_elem}")
