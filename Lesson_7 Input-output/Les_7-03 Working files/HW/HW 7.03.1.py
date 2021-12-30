def get_line(l):
    '''
    Преобразование саписка чисел в строку

    :param l: список чисел
    :return: возвращает строку
    '''
    l = list(map(str, l))
    return ' '.join(l)

with open('3.8 nums.txt', 'r+') as f:
    nums = f.read()
    # print(f.close())
    # print(f.close())


print(nums)

nums_list = list(map(float, nums.split()))
print(nums_list)

# отсортировали по возрастанию
nums_list.sort()
print(nums_list)

with open('3.8 nums.txt', 'a') as f:
    f.write(f'\n{get_line(nums_list)}\n')

print('Done')

# with open('3.8 nums.txt', 'a') as f:
#     for i in nums_list:
#         f.write(str(i))

# with open('3.8 nums.txt', 'a') as f:
#     f.write(nums_list)
#     print(f.read())

# Преобразование саписка чисел в строку

