'''
Тема 5: “Условие else в циклах”
1.	2.	Дана последовательность чисел. Проверить, являются ли все элементы
последовательности нечетными числами.
---------------

'''
l = [1, 3, 9, 7, 11, 5]

for num in l:
    if num % 2 == 0:
        print("no")
        break
else:
    print("Yes")