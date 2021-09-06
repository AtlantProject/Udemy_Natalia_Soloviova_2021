"""
Напишите программу, которая позволит выполнять проверку пароля на сложность в соответствии со следующими критериями:
- длина пароля не менее 5 символов
- содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре: A-Z, a-z
- содержит цифры от 0 до 9
- содержит хотя бы один из символов: @, #, %, &
"""

psw = input(f"Введите пароль: ")

if len(psw) >= 5:
    if not psw.islower() and not psw.isupper():
        if len({'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} & set(psw)) > 0:
            if len({'@', '#', '%', '&'} & set(psw)) > 0:
                print(f'Пароль {psw} является достаточно сложным: ')
            else:
                print("Input a new password!")
        else:
            print("Input a new password!")
    else:
        print("Input a new password!")
else:
    print("Input a new password!")
