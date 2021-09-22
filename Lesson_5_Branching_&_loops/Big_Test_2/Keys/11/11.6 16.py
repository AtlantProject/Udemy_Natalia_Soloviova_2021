"""
Дан список продуктов с ценами на них:
'milk' - $12, 'bread' - $10, 'meat' - $60, 'vegetable mix' - $20, 'fruit mix' - $35, 'fish' - $45,
'eggs' - $15, 'cake' - $15.
У Марты есть $100. Какое максимальное количество продуктов она может купить?
Выведите на экран список этих продуктов.
В случае если Марта сможет купить все продукты из списка, выведите соответствующее сообщение.
Решите эту же задачу для Алекса, у которого есть $250.
"""
goods = {'milk': 12, 'bread': 10, 'meat': 60, 'vegetable_mix': 20, 'fruit_mix': 35, 'fish': 45, 'eggs': 15, 'cake': 15}

goods_sort = {'bread': 10, 'milk': 12, 'eggs': 15, 'cake': 15, 'vegetable_mix': 20, 'fruit_mix': 35, 'fish': 45, 'meat': 60}

sum = 250
max_count = 0

for name, price in goods_sort.items():
    sum -= price
    if sum < 0:
        print(max_count)
        break

    print(name, end=' ')
    max_count += 1
else:
    print('\nВсе товары куплены')







