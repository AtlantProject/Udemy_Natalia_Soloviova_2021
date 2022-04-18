"""
Дана последовательность чисел. Найти минимальный и максимальный элементы последовательности
и подпоследовательность, расположенную между ними (сами элементы не включаются). Причем, если
минимальный элемент в исходной последовательности расположен раньше максимального, то элементы
в искомой подпоследовательность должны быть расположены в том же порядке, а если после - то
в обратном.
Найти среднее арифметическое элементов исходной и полученной последовательностей.

------------
Тестовые значения:
[2, 6, 0, 4, 1, 7, 5, 9, 3] -> [4, 1, 7, 5] -> 4.11, 4.25
[0, 6, 2, 4, 1, 7, 5, 3, 9] -> [6, 2, 4, 1, 7, 5, 3] -> 4.11, 4
[2, 6, 0, 1, 9, 7, 5, 3, 4] -> [1] -> 4.11, 1
[2, 6, 0, 9, 1, 7, 5, 3, 4] -> [] -> 4.11, -
[2, 6, 9, 3, 1, 7, 5, 0, 4] -> [5, 7, 1, 3] -> 4.11, 4
[2, 6, 9, 1, 0, 7, 5, 3, 4] -> [1] -> 4.11, 1
[2, 6, 9, 0, 1, 7, 5, 3, 4] -> [] -> 4.11, -
"""

def find_min_elem(l):
    min_elem = min(l)
    ind = l.index(min_elem)
    return min_elem, ind


def find_max_elem(l):
    max_elem = max(l)
    ind = l.index(max_elem)
    return max_elem, ind


def find_sub_l(l, ind1, ind2):
    # print(f'DEBUG - ind1={ind1}, ind2={ind2}')
    if ind1 < ind2:
        sub_l = l[ind1 + 1: ind2]
    else:
        sub_l = l[ind1 - 1: ind2: -1]  # bug fix: ind1 - 1.py
        # print(f'DEBUG - {l}')
        # print(f'DEBUG - {l[ind1-1]}, {l[ind2]}')
        # print(f'DEBUG - {sub_l}')
    return sub_l


def get_sr_arifm(l):
    # print(f'DEBUG - {l}')
    # print(f'DEBUG - {sum(l)}')
    # print(f'DEBUG - {len(l)}')
    # if len(l) > 0:
    return sum(l)/len(l)
    # return 0


l = [2, 6, 9, 0, 1, 7, 5, 3, 4]
min_elem, min_ind = find_min_elem(l)
max_elem, max_ind = find_max_elem(l)
print(f'Min: {min_elem} (index={min_ind})')
print(f'Max: {max_elem} (index={max_ind})')

sub_l = find_sub_l(l, min_ind, max_ind)
# print(f'DEBUG - {sub_l}')

sr_arifm_l = get_sr_arifm(l)
print(f'Sr. arifm. of {l} is: {sr_arifm_l:.2f}')
if len(sub_l)>0:
    sr_arifm_sub_l = get_sr_arifm(sub_l)
    print(f'Sr. arifm. of {sub_l} is: {sr_arifm_sub_l:.2f}')
else:
    print(f'{sub_l} is empty!')
