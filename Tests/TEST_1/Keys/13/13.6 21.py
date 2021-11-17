"""
Дан список товаров и их цены: {'smart watch': 550, 'phone': 1000, 'playstation': 500, 'laptop': 1550,
'music player': 600, 'tablet': 400}.

- выведите на экран общую стоимость всех товаров
- выведите на экран названия товаров в алфавитном порядке, а затем наоборот
- все музыкальные плееры кроме одного были распроданы, поэтому на последний экземпляр магазин решил сделать 50% скидку.
Внесите соответствующие изменения в список товаров.
- сколько планшетов необходимо продать магазину, чтобы превысить выручку, полученную от продажи пяти телефонов и трех ноутбуков?
- магазин решил провести лотерею среди своих постоянных покупателей. Выберите произвольным образом приз для победителя лотереи,
а затем удалите его из списка.
- в магазин поступило несколько новых устройств: 'iphone' - 1300, 'music player' - 850, 'headphones' - 200.
Обновите список товаров и их цены.
"""
from math import ceil

goods = {'smart watch': 550, 'phone': 1000, 'playstation': 500,
         'laptop': 1550, 'music player': 600, 'tablet': 400}

print('Общая стоимость: ', sum(goods.values()))

goods_names = goods.keys()
print(sorted(goods_names))
print(sorted(goods_names, reverse=True))

goods['music player'] = int(goods['music player'] * 0.5)
print(goods)

sum = 5 * goods['phone'] + 3 * goods['laptop']
tablet_count = ceil(sum / goods['tablet'])
print(sum, tablet_count, tablet_count*goods['tablet'])

prize = goods.popitem()
print("Приз: ", prize[0])
print(goods)

goods.update({'iphone': 1300, 'music player': 850, 'headphones': 200})
print(goods)


