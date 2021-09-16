"""
Ограничить количество попыток ввода пароля - 3
"""
# программа с паролем используя continue


name = input('name: ')

trials = 0       # попытки

while True:
    psw = input('psw: ')
    trials += 1

    if trials == 3:
        print(f"Пароль введен неверно {trials} раза. Программа "
              f"закрывается.")
        break

    if len(psw) < 8:
        print('Too short psw')
        continue
    elif name in psw:
        print('Psw contains name')
        continue
    else:
        print('Psw was set!')
        break
