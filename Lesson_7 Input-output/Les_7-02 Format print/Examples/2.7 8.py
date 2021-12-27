"""
Дан некоторый текст. Определить количество вхождений в него каждого символа.
"""

# text = "abcccced46@a"
text = input('Введите строку: ')
# print(text)

res = {}

for sym in text:
    if sym in res.keys():
        res[sym] += 1
    else:
        res[sym] = 1

for k, v in res.items():
    print(f'{k!r} - {v} раз(а)')
