a = 93
b = 2.5
c = "my first program"

print("a - id= ", id(a), "type- ", type(a))
print("b - id= ", id(b), "type- ", type(b))
print("c - id= ", id(c), "type- ", type(c))

a = 2.5
print("a - id= ", id(a), "type- ", type(a))

X, Y, Z = 138, 138, 138

print(X, Y, Z)

print("X - id= ", id(X))
print("Y - id= ", id(Y))
print("Z - id= ", id(Z))

if id(X) == id(Y) and id(Z):
    print("id X,Y,Z совпадают!")
