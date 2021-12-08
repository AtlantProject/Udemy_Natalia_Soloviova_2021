"""
Дан список слов: ['snow', 'rain', 'wind', 'sun', 'clouds']. Выведите на экран:
- все слова, длина которых больше 3-х символов
- все слова, расположенные до слова длиной 3 символа
"""
l = ['snow', 'rain', 'wind', 'sun', 'clouds']

for elem in l:
    if len(elem)<=3:
        continue
    print(elem, end=' ')
print()

for elem in l:
    if len(elem)==3:
        break
    print(elem, end=' ')