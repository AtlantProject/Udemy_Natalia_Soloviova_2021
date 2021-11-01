# Тема 1: “Ветвления”
# 3.	Дан массив целых чисел. Найти его минимальный и
# максимальный элементы. Если минимальный элемент расположен
# раньше максимального, найти среднее арифметическое всех элементов
# между ними, а если после - заменить данные элементы на их
# среднее геометрическое.

l = [1, 3, 6, 7, 8, 0, 2, 9, 5, 23, 234, 233, 4112]

l_max = max(l)
l_min = min(l)

l_max_ind = l.index(l_max)
l_min_ind = l.index(l_min)

if l_min_ind < l_max_ind:
    sub_l = l[l_min_ind+1:l_max_ind]
    print(sub_l)
    res = sum(sub_l) / len(sub_l)
    print(f"Среднее арифмитическое - {round(res, 2)}")
else:
    sub_l = l[l_max_ind+1:l_min_ind]
    sr_geom = 1
    for i in sub_l:
        sr_geom *= i
        # nVx = x^(1/n)
        sr_geom **= 1/len(sub_l)
        sr_geom = round(sr_geom, 2)
    print(f"Среднее геометрическое - {sr_geom}")
    l[l_max_ind+1:l_min_ind] = [sr_geom]*len(sub_l)
    print(f"Новая последовательность {l}")

