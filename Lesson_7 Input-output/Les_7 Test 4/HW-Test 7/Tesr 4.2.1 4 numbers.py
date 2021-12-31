'''
Контрольная работа №4
Тема 2: “Форматированный вывод”
1.	Напишите программу, запрашивающую у пользователя 4 числа. Отдельно сложите
первые два числа, а затем вторые два числа.
Разделите первую сумму на вторую и выведите результат на экран так, чтобы
ответ содержал знак и две цифры после запятой.
'''
# Этап 1
l = input("Введите 4 числа через пробел: ")
# l = "22 33 44 556"
print(l)

num1, num2, num3, num4 = list(map(int, l.split()))
# numbers = list(map(int(), l.split()))
# numbers = l.split()
# numbers = list(map(int, numbers))
# print(numbers)
# print(type(numbers))

# num1, num2, num3, num4 = numbers
print(num1, num2, num3, num4)
print(type(num1))

# Этап 2
sum_1 = num1 + num2
sum_2 = num3 + num4
res = sum_1 / sum_2
# Этап 3
print("The result is {:+.2f}".format(res))
# print('The result is {:+.2f}'.format(res))
