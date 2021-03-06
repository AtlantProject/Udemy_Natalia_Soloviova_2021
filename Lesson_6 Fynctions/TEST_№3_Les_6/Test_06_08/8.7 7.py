"""
Написать функцию, которая принимает произвольное число чисел и преобразовывает их таким образом,
чтобы цифры каждого числа (по умолчанию) были записаны в обратном порядке.
Предусмотреть возможность по запросу пользователя выполнять преобразования только над нечетными числами.
"""
def reverse_num(n):
    s = str(n)
    return int(s[::-1])

def foo(*args, only_odd=False):
    res = []
    for i in args:
        if not only_odd or (only_odd and i%2!=0):
            res.append(reverse_num(i))
    return res

print(foo(12,2345,323,4456,5687,62,734,81,91))
print(foo(12,2345,323,4456,5687,62,734,81,91, only_odd=True))
