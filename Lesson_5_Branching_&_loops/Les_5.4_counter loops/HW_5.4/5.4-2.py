n = int(input("Введите целое положительное число - "))
# n = 6
l = []

for i in range(1, n+1):
    # print(i)
    if n % i == 0:
        l.append(i)
if len(l) == 2:
    print(f"{n} - является натуральным простым числом")
else:
    print(f"{n} - Не натуральное простое число!")
print(l)

# Вариант 2
print("Вариант 2")
for i in range(2, n):
    if n % i == 0:
        print(f"число {n} не является простым!")
        break
    else:
        print(print(f"число {n} - простое!"))