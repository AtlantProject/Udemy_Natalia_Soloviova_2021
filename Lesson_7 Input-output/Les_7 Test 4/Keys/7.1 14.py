"""
Дано два бинарных файла. Напишите программу, выполняющую слияние заданных файлов
(первая строка первого файла складывается с первой строкой второго файла и т.д.)
и записывающую результат в третий бинарный файл.
"""
import os.path


dir_path = './files'

bin1_path = os.path.join(dir_path, 'bin1.bin')
bin2_path = os.path.join(dir_path, 'bin2.bin')

res_path = os.path.join(dir_path, 'res14.bin')


def read_file(file_path):
    with open(file_path, 'rb') as f:
        return f.readlines()

bin1_data = read_file(bin1_path)
bin2_data = read_file(bin2_path)

res = []
min_len = min(len(bin1_data), len(bin2_data))

for i in range(0, min_len):
    if bin1_data[i].endswith(b'\n'):
        bin1_data[i] = bin1_data[i][:-2]
    if bin2_data[i].endswith(b'\n'):
        bin2_data[i] = bin2_data[i][:-2]
    res.append(bin1_data[i] + b' ' + bin2_data[i] + b'\n')

if len(bin1_data) > min_len:
    res.extend(bin1_data[min_len:])
else:
    res.extend(bin2_data[min_len:])


with open(res_path, 'wb') as f:
    f.writelines(res)
