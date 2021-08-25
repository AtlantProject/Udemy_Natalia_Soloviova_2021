"""
Дан словарь {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}.
Переименовать ключ ‘city’ в ‘location’.
"""

d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}

d['location'] = d.pop('city')
print(d)
