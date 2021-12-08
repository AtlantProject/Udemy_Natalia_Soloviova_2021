"""
Дан список слов. Отфильтровать список с использованием lambda-функции, оставив в нем только слова-палиндромы.

-------------
Тестовые значения:
('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom') -> (madam, mom)
"""
words = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')

res = list(filter(lambda word: word == word[::-1], words))
print(res)
