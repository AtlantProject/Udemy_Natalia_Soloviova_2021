"""
Дано два множества {1, 2, 3, 4, 5} и {4, 5, 6, 7, 8}. Найти:
- объединение множеств
- пересечение множеств
- симметричную разность множеств
- элементы из второго множества, входящие в первое, и удалить их из первого
- является ли второе множество супермножеством для {5, 7, 4} и {8, 4, 3}
- является ли второе множество правильным супермножеством для {5, 8, 4, 7, 6}
"""

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print('Union: ', s1 | s2)
print('Intersection: ', s1 & s2)
print('Sym difference: ', s1 ^ s2)

common_elems = s1 & s2
s1 -= common_elems
print('s1 uniq elements: ', s1)

tmp_s = {5, 7, 4}
print('s2 is superset for ', tmp_s, ': ', s2 >= tmp_s)

tmp_s = {8, 4, 3}
print('s2 is superset for ', tmp_s, ': ', s2 >= tmp_s)

tmp_s = {5, 8, 4, 7, 6}
print('s2 is right superset for ', tmp_s, ': ', s2 > tmp_s)