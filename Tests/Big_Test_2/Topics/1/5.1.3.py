n = [2, 4, 6, 7, 45, 3, 5, 56, 8, 3, 2, 4, 5, 7, 6, 43, 3]
min = max = n[0]

for i in range(0, len(n)):
    if i > max:
        max = n[i]
    if i < min:
        min = n[i]

print(f"min = {min}")
print(f"max = {max}")

k = 0
sum = 0
if n.index(min) < n.index(max):
    for i in range(n.index(min), n.index(max)+1):
        sum += i
        k += 1
    print(f"sum / k = {sum / k}")
