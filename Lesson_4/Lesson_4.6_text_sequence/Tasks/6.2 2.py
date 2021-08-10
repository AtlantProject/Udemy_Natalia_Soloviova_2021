"""
Дана строка, заканчивающаяся точкой.
Подсчитать, сколько слов в строке.
"""

s = "Ежевику для ежат ; Принесли два ежа."

s = s.replace(',', '')
s = s.replace(';', '')
s = s.replace(':', '')
s = s.replace('.', '')

l = s.split()
print(l)

count = len(l)
print('Count: ', count)

print(s)
