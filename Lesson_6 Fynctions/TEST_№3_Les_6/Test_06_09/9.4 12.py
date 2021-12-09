"""
Дан список городов. Сгенерируйте еще один список, содержащий количество вхождений букв ‘a’ и ‘A’
в название каждого города. Решите задачу с использованием lambda-функций.

-------------
Тестовые значения:
['Moscow', 'NY', 'Tokio', 'Los Angeles', 'Paris', 'Venice', 'Amsterdam']
"""

l = ['Moscow', 'NY', 'Tokio', 'Los Angeles', 'Paris', 'Venice', 'Amsterdam']

res = list(map(lambda elem: elem.count('a')+elem.count('A'), l))
print(res)
