"""
Дана последовательность целых чисел.
Найти среднее арифметическое совершенных чисел и среднее геометрическое простых чисел.

Совершенное число - это число, сумма всех делителей которого, меньших его самого,
равна самому числу.
Например: 6 (1+2+3), 28 (1+2+4+7+14), 496 (1+2+4+8+16+31+62+124+248) и т.д.

---------------
Тестовые значения:
[1,4,7,9,4,2,6,9,4,9] ср.арифм.(6) = 6, ср.геом.(7,2) = 3.74
[6,34,76,12,45,28,2,9,32,0,5] ср.арифм.(6, 28) = 17, ср.геом.(2,5) = 3.16
"""
l = [6, 34, 76, 12, 45, 28, 2, 9, 32, 0, 5]

def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

def is_neutral(n):
    return n in [0, 1]

def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n%i == 0:
            s += i
    return n == s       # возвращает Bool

def sr_geom(l):
    res = 1
    for i in l:
        res *= i
    res **= 1/len(l)
    return round(res, 2)


perf_nums = []
prime_nums = []

for i in l:
    if is_neutral(i):
        continue
    if is_prime(i):
        prime_nums.append(i)
    elif is_perfect(i):
        perf_nums.append(i)

sr_arifm = sum(perf_nums)/len(perf_nums)
sr_g = sr_geom(prime_nums)

print('Среднее арифметическое: ', sr_arifm)
print('Среднее геометрическое: ', sr_g)
