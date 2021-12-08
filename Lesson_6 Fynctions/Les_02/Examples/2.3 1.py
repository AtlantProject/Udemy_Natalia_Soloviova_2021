"""
Написать функцию, принимающую некоторое целое число и вычисляющую по умолчанию
сумму его четных цифр. Предусмотреть возможность изменения поведения функции таким образом,
чтобы она также могла вычислять сумму нечетных цифр.

-------------
Тестовые значения:
N = 9874023, even_sum=14, odd_sum = 19
N = 38271, even_sum=10, odd_sum = 11
N = 123456789, even_sum=20, odd_sum = 25
"""

def digits_sum(N, even=True):
    s = 0
    while N>0:
        cur_digit = N%10
        if even and cur_digit%2 == 0:
            s += cur_digit
        elif not even and cur_digit%2 != 0:
            s += cur_digit
        N //= 10
    return s

print(digits_sum(9874023))
print(digits_sum(38271))
print(digits_sum(123456789))

print(digits_sum(9874023, even=False))
print(digits_sum(38271, even=False))
print(digits_sum(123456789, even=False))