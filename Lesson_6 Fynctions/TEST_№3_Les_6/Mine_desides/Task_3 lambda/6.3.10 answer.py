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

# 1-й вариант решения
res = 0
for name in names:
    res += len(name)
print(res)

# 2-й вариант решения
s = ''.join(names)      # Сложили имена в одну строку
print(s)
print(len(s))

