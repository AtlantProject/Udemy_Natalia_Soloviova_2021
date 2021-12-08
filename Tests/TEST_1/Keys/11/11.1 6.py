"""
Дан список, состоящий из 4х элементов: 'abc', 'xyz', 'aba', '1221'.
Проверить для каждого элемента выполнение следующих условий:
длина элемента больше 2х и первый и последний символ у него совпадают.
"""

l = ['abc', 'xyz', 'aba', '1221']

elem = l[0]
print(elem, len(elem) > 2 and elem[0] == elem[-1])

elem = l[1]
print(elem, len(elem) > 2 and elem[0] == elem[-1])

elem = l[2]
print(elem, len(elem) > 2 and elem[0] == elem[-1])

elem = l[3]
print(elem, len(elem) > 2 and elem[0] == elem[-1])


