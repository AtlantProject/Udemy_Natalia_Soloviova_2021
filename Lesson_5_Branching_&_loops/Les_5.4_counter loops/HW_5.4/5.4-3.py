numbers = [i for i in range(1, 15)]
# print(n)
l = []

for n in numbers:
    for i in range(2, n):
        if n % i == 0:
            print(f"число {n} не является простым!")
            break
        else:
            print(print(f"число {n} - простое!"))









'''
    for i in range(2, n):
        print(i)
        if n % i == 0:
            print(f"{n} - Не натуральное простое число!")
        else:
            print(f"{n} - является натуральным простым числом")
'''

