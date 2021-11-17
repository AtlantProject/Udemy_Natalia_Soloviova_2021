'''
Тема 3: “Циклы со счетчиком”

2.	Дан некоторый текст. Определить количество вхождений в него каждого символа.

---------------
Тестовые значения:
"abcccced46@a"

'''

text = "abcccjdfch938hf9hjew9f29w320qdjw9hfced46@a"

res={}

for sym in text:
    if sym in res.keys():
        res[sym] += 1
    else:
        res[sym] = 1

print(res)
