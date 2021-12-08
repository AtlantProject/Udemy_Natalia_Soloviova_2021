'''
n = int(input("Введите целое положительное число - "))
pr = True   # изначально число простое
# while pr == True:
for i in range(2, n//2 + 1):
    if n % i == 0:
        print(f"Число {n} не является простым.")
        pr = False
    # elif pr != True:
    #     print(f"Число {n} не является простым.")
    else:
        print(f"Число {n} -- простое!!!")
    i += i


# Код из интернета
a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")
'''

# Модифицированный Код из интернета
n = int(input("Введите число: "))
pr = True
for i in range(2, n // 2+1):
    # print(i)
    if n % i == 0:
        pr = False
if pr == False:
    print("Число не является простым")
else:
    print("Число простое")