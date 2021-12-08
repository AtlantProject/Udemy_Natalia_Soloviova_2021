'''
l = [11, 21, 24, 3, 3, 3, 4, 5, -2, -2, -34, 6, 6, 7, 8, 9, 10, 10]
min = l[0]
k = 0
for i in range(1, len(l)):
    if l[i] < min:
        min = l[i]
        k = i
        # if l[i] == min:
        #     count.append(l[i])
print(k)
print(min, len(count))
'''
l = [11, 21, 24, 3, 3, 3, 4, 5, -2, -2, -34, -34, 6, 6, 7, 8, 9, 10]
# l = [-1, -2, -3, -4]
k = 0   # счетчик элементов
# min = "нет min элемента"
print(f"длина списка - {len(l)}")
for i in l:
    if i > 0:
        if k == 0:
            min = i
            k = 1
            # print(f"min - {min}")
            # print(f"k (счетчик) = {k}")
        elif k != 0:
            if i < min:
                min = i
            elif i == min:
                k += 1

if k == 0:
    print("В последовательности нет положительных элементов!")
else:
    print(f"min = {min}, k = {k}")



