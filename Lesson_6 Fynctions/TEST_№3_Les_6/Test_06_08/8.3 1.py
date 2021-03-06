"""
Дана последовательность из N целых чисел.
Сформировать последовательность, каждый элемент которой равен сумме цифр соответствующего
элемента исходной последовательности.
Найти сумму цифр в сформированной последовательности.

-----------------
Тестовые значения:
[44,576,17,2342,8,434,22,40,2366,97454,3,12]  -> [8, 18, 8, 11, 8, 11, 4, 4, 17, 29, 3, 3], s=70
"""
l = [44,576,17,2342,8,434,22,40,2366,97454,3,12]

def digit_sum(n):
    s = 0
    while n>0:
        s += n%10
        n //= 10
    return s

res = []
for elem in l:
    res.append(digit_sum(elem))

print(res)

s = 0
for elem in res:
    s += digit_sum(elem)

print(s)
