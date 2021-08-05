'''
ДЗ № 3.2
Найдите значения выражений
'''

f1 = 0 or 1 and not (0 or 1)
f2 = 1 or 0 and 1 and 1 and 0 or 1
f3 = ((1 or 0) and (1 and 1))
f4 = ((f1 or 0) or f2 and 1) and 0
print(f1)
print(f2)
print(f3)
print(f4)

#0 1 1 0