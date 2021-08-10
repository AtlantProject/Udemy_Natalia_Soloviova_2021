"""
Дан список из 10 элементов. Удалить все элементы,
расположенные перед минимальным элементом списка.
"""

l = [2, -50, -7, -3, -8, 4, -9, -1, 5, 7]

min_l = min(l)
print('Min: ', min_l)

ind_min_l = l.index(min_l)
print('Index min: ', ind_min_l)

del l[0: ind_min_l]
print(l)
