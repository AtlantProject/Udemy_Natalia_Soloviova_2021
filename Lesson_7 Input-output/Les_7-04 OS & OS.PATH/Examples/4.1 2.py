"""
Напишите программу, осуществляющую проверку, существует ли указанный файл.
Если файл существует, выведите на экран имя этого файла и имя его директории,
а также время последнего доступа к файлу. Если файл не существует, выведите
соответствующее сообщение.
"""
import os.path


file_path = 'test_dir/f1/4.txt'

if os.path.exists(file_path):
    dir, name = os.path.split(file_path)
    atime = os.path.getatime(file_path)
    print(f'{name} ({dir}) - last access time {atime} sec')
else:
    print(f'File {file_path!r} does not exist!')
