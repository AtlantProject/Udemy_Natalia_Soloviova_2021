# Контрольная работа №3
# Тема 1: “Общие сведения о функциях”
# 2.	Вывести на экран последовательность из первых 100 простых чисел.
# Найти сумму элементов полученной последовательности.

list = [i for i in range(101)]

print(list)

def numsSum(iterable):
    '''
    Функция считает сумму чисел последовательности


    :param iterable: положительное число, итерируемого объекта
    :return: положительное число, возвращает сумму чисел
    '''
    if not iterable:
        return 0    # End of recursion
    else:
        return iterable[0] + numsSum(iterable[1:])

print(numsSum(list))