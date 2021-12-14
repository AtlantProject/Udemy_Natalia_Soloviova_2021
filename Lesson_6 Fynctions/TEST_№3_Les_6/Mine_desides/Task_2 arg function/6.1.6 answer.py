"""
Написать функцию, которая принимает произвольное число чисел,
вычисляет их среднее арифметическое и возвращает только те числа,
которые меньше полученного среднего арифметического.

--------------
Тестовые примеры:
1,2,3,4,5,6,7,8,9  -> sr.arifm.=5
3,6,1,9,5   -> sr.arifm.= 4.8
"""

def foo(*args):
       res = []
       sr_ar = sum(args)/len(args)
       print(sr_ar)

       for num in args:
              if num < sr_ar:
                     res.append(num)
       return res

print(foo(1,2,3,4,5,6,7,8,9))
print(foo(3,6,1,9,5))
