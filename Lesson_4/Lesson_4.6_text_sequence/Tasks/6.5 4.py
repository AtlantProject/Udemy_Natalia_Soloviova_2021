"""
Дана строка, состоящая только из слов без знаков препинания.
Проверить, является ли данная строка палиндромом.

-------------------
Тестовые примеры:
1. Лёша на полке клопа нашёл
2. А роза упала на лапу Азора
3. А роза упала на лапу Азорy (изменен последний символ - не палиндром)
4. Эта строка не палиндром
"""

s = "Эта строка не палиндром"
s = s.lower()
s = s.replace(' ', '')

rev_s = s[::-1]

print(s)
print(rev_s)

print('Палиндром: ', s == rev_s)


