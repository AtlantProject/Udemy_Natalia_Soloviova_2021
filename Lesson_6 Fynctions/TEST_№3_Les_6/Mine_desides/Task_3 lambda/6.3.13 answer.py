"""
Дан список игроков команды, причем для каждого игрока указаны его имя,
фамилия и игровой рейтинг (по шкале от 1 до 10, где 10 - наивысший балл).
Отсортируйте список игроков по фамилии, а затем по их рейтингу от лучшего к худшему и наоборот.
Решите задачу с использованием lambda-функций.

------------
Тестовые значения:
[{'name': 'Antony', 'last name': 'Bloom', 'raiting': 9},
 {'name': 'Alon', 'last name': 'Riddler', 'raiting': 10},
 {'name': 'Greg', 'last name': 'Mc Queen', 'raiting': 4},
 {'name': 'Michael', 'last name': 'Anders', 'raiting': 6}]
"""

players = [{'name': 'Antony', 'last name': 'Bloom', 'raiting': 9},
           {'name': 'Alon', 'last name': 'Riddler', 'raiting': 10},
           {'name': 'Greg', 'last name': 'Mc Queen', 'raiting': 4},
           {'name': 'Michael', 'last name': 'Anders', 'raiting': 6}]

res = sorted(players, key=lambda item: item['last name'])
print(res)

res = sorted(players, key=lambda item: item['raiting'], reverse=True)
print(res)

res = sorted(players, key=lambda item: item['raiting'])
print(res)