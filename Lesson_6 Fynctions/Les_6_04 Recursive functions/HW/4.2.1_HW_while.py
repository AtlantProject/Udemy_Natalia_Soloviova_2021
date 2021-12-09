# Задача 4.2.1
# Написать рекурсивную функцию подсчета суммы элементов списка чисел
# Метод - Рекурсия

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
# Метод цикла while
#TODO: не работает (((
def sum_nums_while(n):
    total = 0  # общая сумма
    while True:  # бесконечный цикл

        if n == 0:  # нашли нуль
            break  # выходим из цикла
        total += n  # суммируем


print(sum_nums_while(nums))
'''

# Итеративное суммирование (lst_itsum)

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9]))

# Рекурсивное суммирование (lst_recsum)

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

