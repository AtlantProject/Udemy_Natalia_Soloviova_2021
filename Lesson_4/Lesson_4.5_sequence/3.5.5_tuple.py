my_tuple = (True, 786, 3.14, 'text', 70.2)
second_tuple = (123, 'text')

print(second_tuple * 2)

a = my_tuple + second_tuple
print(a)

# РАспаковка кортежа
a, b, c, d, e = my_tuple
print(a, b, c, d, e)
