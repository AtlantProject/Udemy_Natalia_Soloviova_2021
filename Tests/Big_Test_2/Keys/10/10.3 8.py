"""
Дан некоторый текст. Определить количество вхождений в него каждого символа.
"""

text = "abcccced46@a"

res = {}

for sym in text:
    if sym in res.keys():
        res[sym] += 1
    else:
        res[sym] = 1

print(res)
