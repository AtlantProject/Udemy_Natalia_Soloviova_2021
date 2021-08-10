# ДЗ 1

l = [2, -5, -7, 31, -8, 4, 9, -1, 5, 7]

l_max = max(l)
print(f"Max - {l_max}")

ind_l_max = l.index(l_max)
print(f"Индекс макимального значения - {ind_l_max}")

del l[ind_l_max + 1:]
print(l)
