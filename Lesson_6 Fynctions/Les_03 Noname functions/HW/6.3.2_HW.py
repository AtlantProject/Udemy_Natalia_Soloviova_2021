# 6.3.2 ДЗ сортировка списка словарей

l = [{'name': 'Ivanov', 'age': 22},
     {'name': 'Petrov', 'age': 34},
     {'name': 'Sidorov', 'age': 58},
     {'name': 'Kleptcov', 'age': 18}]

print(l)

l_sort = sorted(l, key=lambda i: i['age'])

print(l_sort)
