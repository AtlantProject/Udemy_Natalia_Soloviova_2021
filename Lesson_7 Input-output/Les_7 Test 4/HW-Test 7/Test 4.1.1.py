"""
Контрольная работа №4
Тема 1: “Стандартные функции ввода-вывода”
1.	Напишите программу, которая спрашивала бы у пользователя его имя, пол,
возраст и место жительства, а затем
выводила бы полученную информацию на экран в следующем формате:
"""

name = input("Введите свое имя ")
age = input("Введите возраст ")
city = input("Введите город ")

print(f"This is {name}.")
print(f"He (she) is {age} years old.")
print(f"He (she) lives in {city}.")