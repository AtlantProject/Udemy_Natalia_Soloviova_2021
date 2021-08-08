a = list("лоывonksdfn sdfmskl skldf lsdfk")
print(a)

my_list = [True, 786, 3.14, 'text', 70.2]
print(my_list[0])       # True
print(my_list[1:3])     # [786, 3.14]
print(my_list[3:4])     # ['text']
print(my_list[0:5])     # [True, 786, 3.14, 'text', 70.2]
print(my_list[:])       # [True, 786, 3.14, 'text', 70.2]
print(my_list[2:])      # [3.14, 'text', 70.2]
print(my_list[:2])      # [True, 786] аналогично my_list[0:2]
print(my_list[-1])      # 70.2
print(my_list[-2])      # text
print(my_list[-1:-2])   # [] Не стаботает
print(my_list[-2:-1])   # ['text']
print(my_list[::2])     # [True, 3.14, 70.2] Третий аргумент - шаг
print(my_list[::-1])    # [70.2, 'text', 3.14, 786, True] Список в обратном порядке
print(my_list[::-2])    # [70.2, 3.14, True] Список в обратном порядке с шагом 2
print(my_list[-2])      # text
