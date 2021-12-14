"""
Написать функцию, которая принимает строку с разделенными дефисом словами
и возвращает эту же строку со словами отсортированными в алфавитном порядке.
Например, строка “green-red-yellow-black-white” должна быть преобразована
в строку “black-green-red-white-yellow”.
"""

s = 'green-red-yellow-black-white'

def transform_str(s):
       l = s.split("-")
       print(l)
       l.sort()
       print(l)
       return '-'.join(l)

print(transform_str(s))