"""
Написать функцию, которая принимает произвольное число чисел и преобразовывает их таким образом,
чтобы цифры каждого числа (по умолчанию) были записаны в обратном порядке.
Предусмотреть возможность по запросу пользователя выполнять преобразования только над нечетными числами.
"""


def reverse_num(n):
       """
       Функция выполняющая преобразование над числом

       :param n: число
       :return: возвращает преобразованное число
       """
       s = str(n)
       return int(s[::-1])

def foo(*args, only_odd=False):
       '''

       :param args: произвольные положительные числа
       :param only_odd: если False - то все числа преобразуются, если True - то только нечетные
       :return: возвращает список преобразованных чисел
       '''
       res = []
       for i in args:
              if not only_odd or (only_odd and i%2!=0):        # (only_odd and i%2!=0) это и есть условие нечетности
                     res.append(reverse_num(i))
       return res

print(foo(23423, 2342, 234, 5478, 688979, 9672))
print(foo(23423, 2342, 234, 5478, 688979, 9672, only_odd=True))

