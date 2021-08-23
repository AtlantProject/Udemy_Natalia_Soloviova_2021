"""
Даны два списка чисел, содержащие 10 и 15 элементов соответственно.
Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания,
а все остальные - в порядке убывания.
"""

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18]

s1 = set(l1)
s2 = set(l2)

print(s1, s2)

common_elem = s1.intersection(s2)   #s1 & s2
sorted_common_elem = sorted(common_elem)
print('Общие элементы в порядке возрастания: ', sorted_common_elem)

other_elem = s1.symmetric_difference(s2)    #s1 ^ s2
sorted_other_elem = sorted(other_elem, reverse=True)
print('Разные элементы в порядке убывания: ', sorted_other_elem)

