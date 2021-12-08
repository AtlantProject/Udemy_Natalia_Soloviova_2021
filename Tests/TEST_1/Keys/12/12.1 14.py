"""
Дана байтовая строка. Заменить в ней все вхождения первого символа на знак доллара $,
кроме самого первого символа. Например, строка b’restart’ должна превратиться в строку b’resta$t’.
"""

byte_str = b'restart'

first_symb = byte_str[0:1]
print(first_symb)

new_str = first_symb + byte_str[1:].replace(first_symb, b'$')
print(new_str)