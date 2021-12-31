"""
Дан список, состоящий из 4х элементов: ['apples', 1.3, 'oranges',  1.8].
Используя f-строки, выведите на экран следующую строку:
“The weight of an apple is 1.3, the weight of an orange is 1.8”
Измените f-строку таким образом, чтобы названия фруктов были напечатаны в верхнем регистре,
а их вес увеличился на 20%.
"""
l = ['apples', 1.3, 'oranges',  1.8]

s = f"The weight of an {l[0][:-1]} is {l[1]}, the weight of an {l[2][:-1]} is {l[3]}"
print(s)

s = f"The weight of an {l[0][:-1].upper()} is {l[1]*1.2}, the weight of an {l[2][:-1].upper()} is {l[3]*1.2}"
print(s)