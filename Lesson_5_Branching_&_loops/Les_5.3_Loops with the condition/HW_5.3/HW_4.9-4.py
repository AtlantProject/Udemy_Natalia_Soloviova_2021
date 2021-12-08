# Факториал
n = int(input("Введите целое положительное число - "))

import math

res = math.factorial(n)
print(f"Факториал числа {n} при исп. модуля math равен {res}.")

# используя циклы с условием

# while i <= n+1:
#     print(f"i = {i}")
#     n_factorial = i*n_factorial
#     print(n_factorial)
#     i += i

# Формула n! = 1 * … * (n-2) * (n-1) * n
# Перевернутая формула n! = n * (n-1) * (n-2) * … * 1

factorial_1 = 1
while n > 1:
    factorial_1 = factorial_1 * n
    n = n - 1
print(f"Вычисление факториала при помощи цикла while - {factorial_1}.")

# Вычисление факториала с помощью цикла for:
n_2 = 3
factorial_2 = 1
for i in range(2, n_2 + 1):
    factorial_2 *= i

print(f"Вычисление факториала при помощи цикла for - {factorial_2}.")

