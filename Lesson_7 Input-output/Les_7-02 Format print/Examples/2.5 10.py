"""
Найти среднее арифметическое делителей числа N.

---------------
Тестовые значения:
n=28  res=9.33
n=16  res=6.2
n=107 res=54
"""

# N = 107
N = int(input('Введите число N: '))
# print(N)

deliteli = []

for i in range(1, N+1):
    if N%i == 0:
        deliteli.append(i)

print('Делители числа {}: {}'.format(N, ', '.join(list(map(str, deliteli)))))
res = sum(deliteli)/len(deliteli)
print('Среднее арифметическое найденных делителей: {:.2f}'.format(res))