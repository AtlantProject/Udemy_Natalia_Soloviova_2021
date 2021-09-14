"""
Написать программу, которая будет запрашивать у пользователя пароль до тех пор,
пока он не удовлетворит следующим критериям:
- длина пароля не менее 8 символов
- пароль не содержит в себе имя пользователя
"""
name = input('name: ')
psw = input('psw: ')

while True:
    if len(psw)<8:
        print('Too short psw')
    elif name in psw:
        print('Psw contains name')
    else:
        print('Psw was set!')
        break
    psw = input('psw: ')
