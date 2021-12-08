# 6.3.3 ДЗ считаем количество четных и нечетных чисел

# Генератор списка
# nums = [i for i in range(0, 30)]
# print(nums)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 28, 30]

count_even = 0      # четные числа
count_odd = 0      # НЕ четные числа

count_even = list(map(lambda i: i%2 == 0, nums)).count(True)
count_odd = list(map(lambda i: i%2 != 0, nums)).count(True)

print(f'Количество четных чисел - {count_even}')
print(f'Количество НЕ четных чисел - {count_odd}')

# odd_numbers
