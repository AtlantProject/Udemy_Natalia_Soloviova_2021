x = int(input("Введите координату X - "))
y = int(input("Введите координату Y - "))

m = (x, y)

if m[0] == 0 and m[1] == 0:
    print("Начало координат")
elif m[0] == 0:
    print("лежит на координатной оси 0Y")
elif m[1] == 0:
    print("лежит на координатной оси 0X")
else:
    print("расположена в одном из координатных углов")
