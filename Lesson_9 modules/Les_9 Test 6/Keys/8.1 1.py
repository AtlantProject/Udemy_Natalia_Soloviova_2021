"""
Выведите на экран справку о модуле texttable и его содержимое.
Самостоятельно ознакомьтесь с возможностями данного модуля.
"""
import texttable

help(texttable)
print('+'*100)
print(dir(texttable))
print('+'*100)

# специальные атрибуты

print(f"Name - {texttable.__name__}")
print('+'*100)
print(texttable.__doc__)
print('+'*100)
print(texttable.__file__)

# дополнительные атрибуты

print(f"Author - {texttable.__author__}")
print('+'*100)
# print(f"Author - {texttable.__copyright__}")
print(f"Author - {texttable.__credits__}")
print('+'*100)
print(f"Author - {texttable.__license__}")
print('+'*100)
print(f"Author - {texttable.__version__}")
print('+'*100)
# print(f"Author - {texttable.__maintainer__}")
# print(f"Author - {texttable.__email__}")
# print(f"Author - {texttable.__status__}")