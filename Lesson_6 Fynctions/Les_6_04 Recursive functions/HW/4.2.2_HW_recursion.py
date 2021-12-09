# Задача 4.2.2
# Написать рекурсивную функцию подсчета суммы цифр положительного целого числа
# Метод - Рекурсия

num = 123456789


def digSum(n):
    n = list(str(n))
    if not n:
        return 0
    else:
        return n[0] + digSum(n[1:])

print(digSum(num))

