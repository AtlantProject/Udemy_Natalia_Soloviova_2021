"""
Дана последовательность чисел. Проверить, являются ли все элементы
последовательности нечетными числами.
"""
l = [1, 3, 9, 7, 11, 5]

for num in l:
    if num % 2 == 0:
        print('No')
        break
else:
    print('Yes')
