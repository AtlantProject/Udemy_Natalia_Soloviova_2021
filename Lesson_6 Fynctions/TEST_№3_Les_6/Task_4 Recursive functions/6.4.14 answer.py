"""
Напишите рекурсивную функцию, вычисляющую сумму чисел следующей последовательности:
n + (n-2) + (n-4) ….  (n-x),
где (n-x) последнее положительное число последовательности.
Например, для n=6 сумма будет равна 12, а для n=10 сумма равна 30.
"""
def foo(n):
    if n <= 0:
        return 0
    return n + foo(n - 2)

print(foo(6))
print(foo(10))