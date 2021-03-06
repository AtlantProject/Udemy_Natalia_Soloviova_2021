"""
Выполнить следующие действия:
- создать переменную А и присвоить ей значение 5.
Вывести на экран тип данных и идентификатор созданного объекта.
- создать переменную В и присвоить ей значение 12.
Вывести на экран тип данных и идентификатор созданного объекта.
- создать переменную С и присвоить ей значение 5.7.
Вывести на экран тип данных и идентификатор созданного объекта.
- присвоить переменной А значение 12. Проверить, изменился ли ее идентификатор,
и совпадает ли он с идентификатором переменной В. Почему?
- присвоить переменной А значение переменной С.
Проверить, изменился ли ее идентификатор, и совпадает ли он с идентификатором переменной С.
Почему?
- путем множественного присваивания создать переменные D, E и F и присвоить каждой из них значение 125.
Вывести на экран и сравнить между собой идентификаторы созданных объектов.
"""

A = 5
print(type(A))
print(id(A))

B = 12
print(type(B))
print(id(B))

C = 5.7
print(type(C))
print(id(C))

A = 12
print(type(A))
print(id(A))

A = 5.7
print(type(A))
print(id(A))

D, E, F = 125, 125, 125

print(type(D))
print(type(E))
print(type(F))

print(id(D))
print(id(E))
print(id(F))
