"""
Дан список имен. Найдите сумму длин имен списка после удаления всех имен,
начинающихся с маленькой буквы. Решите задачу с использованием lambda-функций.

--------------------
Тестовые значения:
['Alex', 'mary', 'Nonna', 'anna', 'michael', 'Andry']  ->  14
"""
names = ['Alex', 'mary', 'Nonna', 'anna', 'michael', 'Andry']
names = list(filter(lambda name: name[0].isupper(), names))
print(names)

# res = 0
# for n in names:
#     res += len(n)
#
# print(res)

# 2-ой вариант решения

s = ''.join(names)
print(len(s))
