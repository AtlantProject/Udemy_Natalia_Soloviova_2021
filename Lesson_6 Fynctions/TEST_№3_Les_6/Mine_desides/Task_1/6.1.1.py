# Контрольная работа №3
# Тема 1: “Общие сведения о функциях”
# 1. Дана последовательность из N целых чисел. Сформировать последовательность, каждый элемент которой равен
# сумме цифр соответствующего элемента исходной последовательности. Найти сумму цифр в сформированной последовательности.

# TODO: задача не решена

list = [1, 2, 3, 4, 5]

# функция вычисления сумму чисел последовательности
def getSum(iterable):
    if not iterable:
        return 0  # End of recursion
    else:
        return iterable[0] + getSum(iterable[1:])  # Recursion step


# Формируем последовательность
def numsSum(l):

    list_sum = []

    for i in l:
        if i == 0:
            continue

        if i == 1:
            list_sum = list_sum.append(i)

        # Формируем последовательность для вычисления суммы составляющих очередной элемент исходной последовательности
        list_from_i = [b for b in range(len(i) + 1)]
            for iterable in list_from_i:
                return list_sum.append(getSum(iterable))
        return list_sum

