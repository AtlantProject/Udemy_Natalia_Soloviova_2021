l = [11, 21, 24, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
min = l[0]
count = []
for i in range(1, len(l)):
    if l[i] < min:
        min = l[i]
        if l[i] == min:
            count.append(l[i])
print(count)
print(min, len(count))
