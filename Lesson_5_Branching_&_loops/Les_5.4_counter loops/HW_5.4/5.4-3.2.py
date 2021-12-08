list = [i for i in range(1, 15)]
# print(n)
k = 0

for i in list:
    # print(f"i = {i}")
    for number in range(2, i//2+1):
        print(f"number = {number}")
        if i % number == 0:
            print(f"число {i} не является простым!")

        else:
            k += 1
            print(print(f"число {i} - простое!"))

if k == 0:
    print("Простых чисел нет")
else:
    print(k)








'''
    for i in range(2, n):
        print(i)
        if n % i == 0:
            print(f"{n} - Не натуральное простое число!")
        else:
            print(f"{n} - является натуральным простым числом")
'''

