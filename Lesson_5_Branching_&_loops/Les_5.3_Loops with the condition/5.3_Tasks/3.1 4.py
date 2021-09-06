"""
Дан список: [1452, 11.23, 1+2j, True, 'hello, python!',
(0, -1), [5, 12], {'class': 'v', 'section': 'A'}].
Вывести на экран значение и тип данных для каждого элемента списка.
"""
l = [1452, 11.23, 1+2j, True, 'hello, python!', (0, -1), [5, 12], {'class': 'v', 'section': 'A'}]

i = 0
while i<len(l):
    elem = l[i]
    print(elem, type(elem))
    i += 1
