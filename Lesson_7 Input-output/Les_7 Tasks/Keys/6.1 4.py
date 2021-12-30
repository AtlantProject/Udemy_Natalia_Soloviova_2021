"""
Напишите программу, запрашивающую у пользователя 4 числа.
Отдельно сложите первые два числа, а затем вторые два числа.
Разделите первую сумму на вторую и выведите результат на экран так,
чтобы ответ содержал знак и две цифры после запятой.

--------
Тестовые значения:
12 23 34 56   -> +0.39
34 65 13 10   -> +4.30
34 65 -13 10   -> -33.00
"""

num1 = int(input('Please, enter the first number: '))
num2 = int(input('Please, enter the second number: '))
num3 = int(input('Please, enter the third number: '))
num4 = int(input('Please, enter the fourth number: '))

sum1 = num1 + num2
sum2 = num3 + num4

res = sum1/sum2
print('The result is {:+.2f}'.format(res))
