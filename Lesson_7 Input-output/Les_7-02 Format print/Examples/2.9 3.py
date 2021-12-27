"""
Дан массив целых чисел. Найти его минимальный и максимальный элементы.
Если минимальный элемент расположен раньше максимального, найти среднее арифметическое всех элементов между ними,
а если после - заменить данные элементы на их среднее геометрическое.

--------------------
Тестовые значения:
[3,4,6,2,2,6,1,5,8,4,31]    ср.арифм: 5.667
[31,4,6,2,2,6,1,5,8,4,3]  ср.геом: 3.565
"""

# l = [31,4,6,2,2,6,1,5,8,4,3]
l = input('Введите список чисел: ')
l = list(map(int, l.split()))
# print(l)

max_l = max(l)
min_l = min(l)

max_l_ind = l.index(max_l)
min_l_ind = l.index(min_l)

if min_l_ind < max_l_ind:
    sub_l = l[min_l_ind+1: max_l_ind]
    res = sum(sub_l)/len(sub_l)
    print('Среднее арифметическое: {:.2f}'.format(res))
else:
    sub_l = l[max_l_ind+1:min_l_ind]
    sr_geom = 1
    for i in sub_l:
        sr_geom *= i
    # nVx = x^(1/n)
    sr_geom **= 1/len(sub_l)
    sr_geom = round(sr_geom, 2)

    l[max_l_ind+1:min_l_ind] = [sr_geom]*len(sub_l)
    print('Среднее геометрическое: {:.2f}\nПолученный список чисел: {}'.format(sr_geom, l))
