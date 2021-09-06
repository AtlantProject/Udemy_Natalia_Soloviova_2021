"""
Напишите программу, которая позволит выполнять проверку пароля на сложность в соответствии со следующими критериями:
- длина пароля не менее 5 символов
- содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре: A-Z, a-z
- содержит цифры от 0 до 9
- содержит хотя бы один из символов: @, #, %, &
!!! Пароль удовлетворяет хотя бы 3-м критериям из списка!!!
"""

# psw = input(f"Введите пароль: ")
psw = '12345A'

cond1 = len(psw) >= 5
print(cond1)
cond2 = not psw.islower() and not psw.isupper()
print(cond2)
cond3 = len({'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} & set(psw)) > 0
print(cond3, set(psw))
cond4 = len({'@', '#', '%', '&'} & set(psw)) > 0
print(cond4)

# print('Пароль является достаточно сложным: ', cond1 and cond2 and cond3 and cond4)

if cond1 + cond2 + cond3 + cond4 >= 3:
    print(f'Пароль {psw} удовлетворяет 3-м критериям из списка! ')
    print(f"Выполнено условий: {cond1 + cond2 + cond3 + cond4}")
else:
    print(f"Выполнено условий: {cond1 + cond2 + cond3 + cond4}")
    print("Input a new password!")


# if cond1:
#     if cond2:
#         if cond3:
#             if cond4:
#                 print(f'Пароль {psw} является достаточно сложным: ')
#             else:
#                 print("Input a new password!")
#         else:
#             print("Input a new password!")
#     else:
#         print("Input a new password!")
# else:
#     print("Input a new password!")
