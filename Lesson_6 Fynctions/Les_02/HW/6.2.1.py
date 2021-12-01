# 6.2.1 Аргументы функции
#TODO: Решить задачу


def security(name=input('Ведите логин - '),
             password=int(input('Ведите пароль - ')),
             retries=3,
             reminder='Система заблокирована. Повторите попытку через 5 мин.'):
    # input('Ведите логин - ')
    if name == 'login':
        # int(input('Ведите логин - ')):
        if password == 12345:
            print("Доступ разрешен!")
        else:
            retries -= 1
            print(f'{reminder} Количество попыток - {retries}')
    else:
        retries -= 1
        print(f'{reminder} Количество попыток - {retries}')



