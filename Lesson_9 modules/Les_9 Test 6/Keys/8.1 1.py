"""
Выведите на экран справку о модуле texttable и его содержимое.
Самостоятельно ознакомьтесь с возможностями данного модуля.
"""
import texttable

help(texttable)
print('+'*100)
print(dir(texttable))
print('+'*100)

print(f"Name - {texttable.__name__}")
print('+'*100)
print(texttable.__doc__)
print('+'*100)
print(texttable.__file__)
