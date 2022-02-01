"""
Напишите программу, генерирующую в заданной директории 26 текстовых файлов:
A.txt, B.txt, C.txt, ….., Z.txt, каждый из которых содержит соответствующую
букву английского алфавита.
* Вы можете внести в программу буквы алфавита вручную или воспользоваться
атрибутом ascii_uppercase модуля string (string.ascii_uppercase).
"""
import os.path
from string import ascii_uppercase

# в текущей директории создаем папку
dir_path = './res_13'

# print(ascii_uppercase)      # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# в цикле создаем эти файлы
for char in ascii_uppercase:
    # генерируем имя и путь к файлу
    file_path = os.path.join(dir_path, f"{char}.txt")
    # print(file_path)

    # Создаем эти файлы
    with open(file_path, 'w') as f:
        # записываем в файл символ char
        f.write(char + " 123 23324")
