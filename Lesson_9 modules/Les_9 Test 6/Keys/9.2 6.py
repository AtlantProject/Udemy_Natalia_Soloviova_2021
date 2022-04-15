"""
Используя модуль random, сформируйте случайным образом последовательность,
состоящую из 20-ти нечетных чисел в диапазоне от 100 до 1000.
Удалите из полученной последовательности максимальный и минимальный элементы.
Найдите среднее арифметическое пяти наибольших элементов в преобразованной последовательности.
"""
import random

l = range(101, 1000, 2)
rand_l = random.sample(l, 20)
print(rand_l)

min_elem = min(rand_l)
max_elem = max(rand_l)
print(f'Min={min_elem}, max={max_elem}')
rand_l.remove(min_elem)
rand_l.remove(max_elem)
print(rand_l)

sorted_rand_l = sorted(rand_l, reverse=True)
print(sorted_rand_l)
sr_ar = sum(sorted_rand_l[:5])/5
print(f'Sr. arifm. of {sorted_rand_l[:5]} is {sr_ar:.2f}')