"""
Выведите на экран имена и размер всех непустых файлов созданного в первой задаче дерева.
Создайте директорию work/empty_files и переместите в нее все пустые файлы,
при этом для каждого перемещенного файла должно быть выведено соответствующее сообщение,
содержащее имя файла, старый путь к файлу относительно корневой директории и новый путь к файлу после перемещения.
"""
import os, os.path

EMPTY_DIR = 'Work/empty_files'


def print_nonempty_files(root, topdown):
    for root, dirs, files in os.walk(root, topdown=topdown):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > 0:
                print(f"{file_path!r} - {file_size} bytes")


def move_empty_files(root, dir):
    for root, dirs, files in os.walk(root):
        if root == dir:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size == 0:
                os.rename(file_path, os.path.join(dir, file))
                print(f"{file!r} moved from {root!r} to {dir!r}")


print_nonempty_files('Work', topdown=True)
os.makedirs(EMPTY_DIR)
move_empty_files('Work', EMPTY_DIR)

