'''
1.	Дана байтовая строка. Заменить в ней все вхождения первого символа на знак доллара $,
 кроме самого первого символа.
Например, строка b’restart’ должна превратиться в строку b’resta$t’.
'''
'''
s = b'restart'
r_count = s.count(b'r')
print(r_count)
r_iter = 'r' * int(r_count)

print(r_iter)

s = s.replace(b'r', b'$', -1)
print(s)
'''
b_str = b'restart'
# находим первый символ строки
first_symbol = b_str[0:1]
print(first_symbol)

# Меняем символы на "$"
new_str = first_symbol + b_str[1:].replace(first_symbol, b'$')
print(new_str)