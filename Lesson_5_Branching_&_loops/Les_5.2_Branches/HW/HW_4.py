# from math import ceil

goods = {'smart watch': 600, 'phone': 1000, 'playstation': 450,
         'laptop': 1550, 'music player': 400, 'tablet': 400}

# money = 1300
money = int(input("Введите сумму денег: "))

buys = goods['smart watch'] + goods['playstation'] + goods['music player']
print(f"Сумма цены покупки: {buys}$.")
basket = buys
sale = 0

if basket >= 1000:
    sale  = 0.3       # Скидка 30% для следующей покупки
    basket = int(buys - buys*sale)
    print(f"Цена со скидкой - {basket}$.")
    if basket <= money:
        print(f"днег на покупку хватает!")
    else:
        print(f"Денег не хватает!!!(((")
