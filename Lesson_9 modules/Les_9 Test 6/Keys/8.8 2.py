"""
Выведите на экран значения специальных и дополнительных атрибутов модуля texttable.
Какие из атрибутов определены у модуля, а какие нет?
"""
import texttable


# специальные атрибуты

print(f'Name: {texttable.__name__}')
print(f'DOC: {texttable.__doc__}')
print(f'File: {texttable.__file__}')


# дополнительные атрибуты

print(f'Author: {texttable.__author__}')
# print(f'(C): {texttable.__copyright__}')
print(f'Credits: {texttable.__credits__}')
print(f'License: {texttable.__license__}')
print(f'Version: {texttable.__version__}')
# print(f'Maintainer: {texttable.__maintainer__}')
# print(f'Email: {texttable.__email__}')
# print(f'Status: {texttable.__status__}')