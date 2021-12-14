# Контрольная работа №3
# Тема 1: “Общие сведения о функциях”
# 3.	Написать функцию, которая принимает в качестве аргумента строку
# и подсчитывает в ней количество символов в верхнем и нижнем регистре

list = 'Контрольная работа №3' \
       'Тема 1: Общие сведения о функциях' \
       '3.	Написать функцию, которая принимает в качестве аргумента строку' \
       'и подсчитывает в ней количество символов в верхнем и нижнем регистре'

def str_count(s):
       upper_num = 0
       lower_num = 0

       for char in s:
              if char.isupper():
                     upper_num += 1
              elif char.islower():
                     lower_num += 1

       return {'upper_num': upper_num, 'lower_num': lower_num}

print(str_count(list))
print(str_count('jdnkJDFofjwoifj'))
print(str_count('GGGhhh'))