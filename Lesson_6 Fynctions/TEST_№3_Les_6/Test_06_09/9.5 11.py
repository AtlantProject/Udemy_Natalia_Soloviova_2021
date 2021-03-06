"""
Преобразуйте заданную последовательность чисел таким образом,
чтобы каждый элемент новой последовательности был равен произведению соответствующего элемента
исходной последовательности и его порядкового номера, возведенного в куб.
Решите задачу с использованием lambda-функций.

--------------
Тестовые значения:
[3,6,8,9,1,2]  -> [0, 6, 64, 243, 64, 250]
"""
l = [3,6,8,9,1,2]

res = list(map(lambda elem: elem*l.index(elem)**3, l))
print(res)
