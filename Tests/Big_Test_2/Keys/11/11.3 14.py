"""
Дана последовательность чисел. Проверить, есть ли в ней хотя бы одно число с делителями 2, 5 и 7.
Если да, вывести его на экран. Если нет, вывести соответствующее сообщение.
"""
l = [3, 6, 2, 8, 5, 4, 1, 7, 10]

for num in l:
    if num%2 == 0 and num%5 == 0 and num%7 == 0:
        print(num)
        break
else:
    print('no such numbers')