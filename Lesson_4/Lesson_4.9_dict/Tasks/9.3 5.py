"""
Дан словарь {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}.
Создать новый словарь, который будет содержать только имя и зарплату сотрудника,
а затем удалить эти значения из исходного словаря.
"""

d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}

new_d = {}
new_d['name'] = d.pop('name')
new_d['salary'] = d.pop('salary')


# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
print(d)
print(new_d)

