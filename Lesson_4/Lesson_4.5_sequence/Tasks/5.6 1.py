"""
Дан список из 20 произвольных целых чисел.
Найти сумму элементов этого списка.

-------------------
Тестовые значения:
[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]  сумма: 90
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  сумма: 20
[10,20,30,40,50,60,70,80,90,100,0,1,2,3,4,5,6,7,8,9] сумма: 595
"""

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_l = sum(l)

print('Summa: ', sum_l)


