# Задача 4.2.1
# Написать рекурсивную функцию подсчета суммы элементов списка чисел
# Метод - Рекурсия

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_recursion(arr, size=len(arr)):
    if size == 0:
        return 0
    else:
        return arr[size - 1] + sum_recursion(arr, size=len(arr) - 1)

print(sum_recursion(nums))

'''
# Метод цикла for

def sum_nums_for(n):
    summa = 0
    for i in n:
        summa += i
    return summa

print(sum_nums(nums))
'''
