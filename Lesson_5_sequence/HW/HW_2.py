# ДЗ 1

l = [2, -5, -7, 31, -8, 4, 9, -1, -15, 5, 7]
print(l)

l_max = max(l)
print(f"Max - {l_max}")

l_min = min(l)
print(f"Min - {l_min}")

ind_l_max = l.index(l_max)
print(f"Индекс макимального значения - {ind_l_max}")

ind_l_min = l.index(l_min)
print(f"Индекс минимального значения - {ind_l_min}")

l_2 = l[:]
print(f"l_2 = {l_2}")

del l[ind_l_max:ind_l_min]
print(l)

l_2.sort()
print(f"l_2 sort = {l_2}")

l_2_max = max(l_2)
l_2_min = min(l_2)

ind_l_2_max = l_2.index(l_2_max)
ind_l_2_min = l_2.index(l_2_min)

del l_2[ind_l_2_min:ind_l_2_max]
print(l_2)
