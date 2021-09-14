"""
Написать программу, которая будет запрашивать у пользователя пароль до тех пор,
пока он не удовлетворит следующим критериям:
- длина пароля не менее 8 символов
- пароль не содержит в себе имя пользователя
"""
# программf с паролем используя continue


name = input('name: ')

while True:
    psw = input('psw: ')

    if len(psw) < 8:
        print('Too short psw')
        continue
    elif name in psw:
        print('Psw contains name')
        continue
    else:
        print('Psw was set!')
        break
