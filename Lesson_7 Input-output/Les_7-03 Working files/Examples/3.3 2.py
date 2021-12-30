"""
В текстовом файле nums.txt хранятся вещественные числа.
Вывести их на экран и вычислить их количество.
"""
file_name = '3.8 nums.txt'

with open(file_name, 'r') as f:
    nums = f.read()

print(nums)
print(type(nums))

nums_list = list(map(float, nums.split()))
print(nums_list)
print(len(nums_list))
