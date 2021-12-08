"""
Написать функцию, которая принимает один аргумент, который в дальнейшем будет умножаться на заданное число.
"""
def fucn_compute(n):
    return lambda x: x*n

res = fucn_compute(2)
print(res(15))  # = 30
print(res(20))  # = 40

res = fucn_compute(3)
print(res(15))  # = 45
print(res(20))  # = 60
