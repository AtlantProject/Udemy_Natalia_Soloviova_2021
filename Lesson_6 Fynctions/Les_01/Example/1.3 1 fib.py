"""
Написать функцию, которая выводит ряд Фибоначчи до заданной границы N.
Например, для N = 15 ряд будет выглядеть следующим образом:
0, 1, 1, 2, 3, 5, 8, 13.
"""
def fib(N):
    a, b = 0, 1
    while a < N:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(15)

fib(25)
