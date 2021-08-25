"""
Дан словарь {'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 6500}}.
Измените значение зарплаты Брэда с 6500 до 8500.
"""

d = {'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}}

print(d['emp3'])
print(d['emp3']['salary'])

d['emp3']['salary'] = 8500

print(d)
