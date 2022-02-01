"""
Дано два бинарных файла. Напишите программу, выполняющую слияние заданных файлов
(первая строка первого файла складывается с первой строкой второго файла и т.д.)
и записывающую результат в третий бинарный файл.
"""
import os.path

dir_path = './files'    # './files' == 'files'

bin1_path =  os.path.join(dir_path, 'bin1.bin') # =='./files/bin1.bin'
bin2_path =  os.path.join(dir_path, 'bin2.bin')

res_path =  os.path.join(dir_path, 'res14.bin')

def read_file(file_path):
    with open(file_path, 'rb') as f:
        return f.readlines()

bin1_data = read_file(bin1_path)
bin2_data = read_file(bin2_path)

res = []

# находим мин общее кол-во строк
min_len = min(len(bin1_data), len(bin2_data))

def valid_data_files(file_data):
    '''
    Функция проверяет наличие в конце строки '\n' (перехода на новую строчку)

    :param file_data: проверяемый файл
    :return: возвращает файл без '\n' (перехода на новую строчку) в конце строки
    '''
    if file_data[i].endswith(b'\n'):
        file_data[i] = file_data[i][:-1]
    return file_data


for i in range(0, min_len):
    #избавляемся от ненужного перехода на новую строчку

    # if bin1_data[i].endswith(b'\n'):
    #     bin1_data[i] = bin1_data[i][:-1]
    # if bin2_data[i].endswith(b'\n'):
    #     bin2_data[i] = bin2_data[i][:-1]

    # избавляемся от ненужного перехода на новую строчку с помощью фукции
    valid_data_files(bin1_data)
    valid_data_files(bin2_data)
    # конкатенация строк
    res.append(bin1_data[i] + b' ' + bin2_data[i] + b'\n')

# проверяем если один из файлов оказался длиннее
if len(bin1_data) > min_len:
    res.extend(bin1_data[min_len:])     # добавляем сразу несколько строк к результату

else:
    res.extend(bin2_data[min_len:])

# записываем результат в результирующий файл
with open(res_path, 'wb') as f:
    f.writelines(res)


