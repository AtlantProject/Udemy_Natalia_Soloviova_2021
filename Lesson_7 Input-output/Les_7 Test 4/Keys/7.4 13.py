"""
Напишите программу, генерирующую в заданной директории 26 текстовых файлов:
A.txt, B.txt, C.txt, ….., Z.txt, каждый из которых содержит соответствующую
букву английского алфавита.
* Вы можете внести в программу буквы алфавита вручную или воспользоваться
атрибутом ascii_uppercase модуля string (string.ascii_uppercase).
"""
import os.path
from string import ascii_uppercase

dir_path = './res_13'

# print(ascii_uppercase)
for char in ascii_uppercase:
    file_path = os.path.join(dir_path, f"{char}.txt")
    # print(file_path)
    with open(file_path, 'w') as f:
        f.write(char + char)

