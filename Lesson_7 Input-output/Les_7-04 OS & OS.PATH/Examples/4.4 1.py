"""
Напишите программу, которая просканирует выбранную директорию и для всех ее объектов выведет
следующую информацию на экран:

имя - тип - размер (только для файлов)

* Типы объектов: файл, директория, ссылка или неизвестный
* Размер: только для файлов
"""
import os, os.path

dir_name = 'test_dir/f1'

objs = os.listdir(dir_name)

for obj in objs:
    p = os.path.join(dir_name, obj)
    if os.path.isfile(p):
        print(f'{obj} - file - {os.path.getsize(p)} bytes')
    elif os.path.isdir(p):
        print(f'{obj} - dir')
    elif os.path.islink(p):
        print(f'{obj} - link')
    else:
        print(f'{obj} - undefined')

