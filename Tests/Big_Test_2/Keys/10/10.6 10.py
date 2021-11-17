"""
Найти среднее арифметическое делителей числа N.

---------------
Тестовые значения:
n=28  res=9.33
n=16  res=6.2
n=107 res=54
"""

N = 107

deliteli = []

for i in range(1, N+1):
    if N%i == 0:
        deliteli.append(i)

print(deliteli)
res = sum(deliteli)/len(deliteli)
print(round(res, 2))