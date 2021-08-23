"""
Дана строка, заканчивающаяся точкой.
Подсчитать, сколько слов в строке.
"""

s = b"Ezheviku dlya ezhat; Prinesli dva ezha."

s = s.replace(b',', b'')
s = s.replace(b';', b'')
s = s.replace(b':', b'')
s = s.replace(b'.', b'')

l = s.split()
print(l)

count = len(l)
print('Count: ', count)

