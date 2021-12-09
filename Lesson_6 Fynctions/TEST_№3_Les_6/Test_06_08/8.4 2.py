"""
Вывести на экран последовательность из первых 100 простых чисел.
Найти сумму элементов полученной последовательности.
"""
res = []
count = 0

def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

i = 2
while count<100:
    if is_prime(i):
        res.append(i)
        count += 1
    i += 1

print(res, len(res))
print(sum(res))
