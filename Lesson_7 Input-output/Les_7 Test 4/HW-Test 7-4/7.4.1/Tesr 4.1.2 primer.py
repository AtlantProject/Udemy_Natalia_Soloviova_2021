'''
Контрольная работа №4
Тема 1: “Стандартные функции ввода-вывода”
2.	Напишите программу, которая предлагает пользователю решить пример: 4*100-54. В случае, если пользователь
ошибается, программа должна вывести соответствующее сообщение и правильный ответ.
А в случае, если пользователь прав, - поздравить его с правильным ответом.
'''
# 4*100-54

num1 = 4
num2 = 100
num3 = 54

task = num1*num2-num3
question = str(task)

print(f"Решите следующую задачу: 4*100-54")
answer = int(input("Введите ответ - "))

if answer == task:
    print("Поздравляем! задача решена правильно!!!")
else:
    print(f"Задача решена неверно!!!((( Верный ответ {task}")

