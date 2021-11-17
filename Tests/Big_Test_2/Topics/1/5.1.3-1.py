# l = [2, 4, 6, 7, 45, 3, 5, 56, 8, 3, 2, 4, 5, 7, 6, 43, 3]
# l = [3,4,6,2,2,6,1,5,8,4,31]
l = [31,4,6,2,2,6,1,5,8,4,3]

l_max = max(l)
l_min = min(l)

l_max_ind = l.index(l_max)
l_min_ind = l.index(l_min)

if l_min_ind < l_max_ind:
    sub_l = l[l_min_ind+1: l_max_ind]
    print(sub_l)
    res = sum(sub_l) / len(sub_l)
    print(f"Среднее арифмитическое - {round(res, 2)}")
else:
    sub_l = l[l_max_ind + 1: l_min_ind]
    sr_geom = 1
    for i in sub_l:
        sr_geom *= i
    # nVx = x^(1/n) - формула вычисления среднего геометрического
    sr_geom = sr_geom ** (1/len(sub_l))
    # sr_geom **= 1 / len(sub_l)
    sr_geom = round(sr_geom, 2)

    l[l_max_ind + 1: l_min_ind] = [sr_geom]*len(sub_l)
    print(f"Среднее геометрическое: {sr_geom}, {l}")

