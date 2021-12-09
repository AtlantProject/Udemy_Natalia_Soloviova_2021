# Задача 4.2.1
# Написать рекурсивную функцию подсчета суммы элементов списка чисел
# Метод - Рекурсия

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Способ № 1 (from Internet)

nums_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def recursion_sum(arr):
    '''

    :param arr: итерируемы аргумент
    :return: возвращает сумму
    '''
    if not arr:
        return 0
    return arr[0] + recursion_sum(arr[1:])  # отрезаем от начала списка по одной цифре

# print(recursion_sum([i for i in range(10)]))
print(recursion_sum(nums_2))

# Способ № 2 (from Internet)

nums_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def getSum(iterable):
    if not iterable:
        return 0  # End of recursion
    else:
        return iterable[0] + getSum(iterable[1:])  # Recursion step

print(getSum(nums_3))


#TODO: Мой нерабочий способ рекурсивной функции ((( 08.12.2021
"""
def sum_recursion(arr, lensize=len(arr)):
    '''
    Реурсивная функция подсчета суммы элементов списка чисел

    :param arr:
    :param size:
    :return:
    '''
    if size == 0:
        return 0
    else:
        return arr[size - 1] + sum_recursion(arr, size=len(arr) - 1)

print(sum_recursion(nums))
"""
