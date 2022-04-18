"""
Дан текстовый файл с некоторыми числами (каждое число в новой строке).
Создать новый файл в который будут записаны результаты вычисления квадратного корня
из соответствующих чисел исходного файла.
"""
from math import sqrt


inp_file = 'test_data.txt'
res_file = 'res.txt'

def get_data(file_name):
    res = []
    with open(file_name) as f:
        while True:
            data = f.readline()
            # print(f'DEBUG - {data}')
            if not data:
                break

            if ',' in data:
                data = data.replace(',', '.')
            # print(f'DEBUG - {data}')
            res.append(float(data))

    return res

def write_data(file_name, data):
    with open(file_name, 'w') as f:
        for elem in data:
            f.write(f'{elem:.2f}\n')


nums = get_data(inp_file)
# print(f'DEBUG - {nums}')

sqrt_nums = []
for elem in nums:
    # print(f'DEBUG - {elem}')
    if elem >= 0:
        sqrt_nums.append(sqrt(elem))

# sqrt_nums = list(map(sqrt, nums))
# print(f'DEBUG - {sqrt_nums}')
write_data(res_file, sqrt_nums)
