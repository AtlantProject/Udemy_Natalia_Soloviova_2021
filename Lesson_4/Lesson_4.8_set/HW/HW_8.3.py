a = 543731
b = 4472
c = 999999
d = 347623
e = 1000001

# s1 = set(a)
# s2 = set(b)
# s3 = set(c)
# s4 = set(d)
# s5 = set(e)

# a = str(a)
# print(f'Число преобразованное в строку: {a}')
# a = list(a)
# print(f'Строка преобразованная в список:    {a}')
# s1 = set(a)
# print(f'Список преобразованный в множество: {s1}')
s1 = set(list(str(a)))
s2 = set(list(str(b)))
s3 = set(list(str(c)))
s4 = set(list(str(d)))
s5 = set(list(str(e)))
print(s1, s2, s3, s4, s5)

print(f'Количество уникальных цифр:'
      f'\n\tдля числа {a} - {len(s1)} цифр. Max = {max(s1)}, min = {min(s1)};'
      f'\n\tдля числа {b} - {len(s2)} цифр.  Max = {max(s2)}, min = {min(s2)};'
      f'\n\tдля числа {c} - {len(s3)} цифр.  Max = {max(s3)}, min = {min(s3)};'
      f'\n\tдля числа {d} - {len(s4)} цифр.  Max = {max(s4)}, min = {min(s4)};'
      f'\n\tдля числа {e} - {len(s5)} цифр.  Max = {max(s5)}, min = {min(s5)};')


