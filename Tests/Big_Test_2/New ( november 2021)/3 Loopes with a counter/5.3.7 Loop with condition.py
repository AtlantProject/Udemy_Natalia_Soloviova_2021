'''
Тема 3: “Циклы со счетчиком”

1.	Определить, сколько раз последовательность из N произвольных чисел меняет знак
(т.е. после положительного элемента идет отрицательный и наоборот).

---------------
Тестовые значения:
[4, -2, 3, -5, -8, 0, 6, -4, 2, 5, 7, -9, -3, -7]

'''

l = [4, -2, 3, -5, -8, 0, 6, -4, 2, 5, 7, -9, -3, -7]

count = 0

for i in range(0, len(l) - 1):  # последний элемент последовательности не включаем в диапазон, т.к. его не с чем сравнивать
    if (l(i) >= 0 and l(i+1) < 0) or (l(i) < 0 and l(i + 1) >= 0):