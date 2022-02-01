"""
Выведите на экран имена и размер всех непустых файлов созданного в первой задаче дерева.
Создайте директорию work/empty_files и переместите в нее все пустые файлы,
при этом для каждого перемещенного файла должно быть выведено соответствующее сообщение,
содержащее имя файла, старый путь к файлу относительно корневой директории и новый путь к файлу после перемещения.
"""
import os, os.path

EMPTY_DIR = 'Work/empty_files'


def print_nonempty_files(root, topdown):
    '''
    Выводит все непустые файлы
    :param root: корневая директория, где ищем файлы
    :param topdown: проход: сверху вниз/снизу вверх
    :return:
    '''
    for root, dirs, files in os.walk(root, topdown=topdown):
        # проходимся по всем файлам (нас интересуют только файлы)
        for file in files:
            # сначала генерируем полный путь этого файла
            file_path = os.path.join(root, file)

            # ищем размер этого файла
            file_size = os.path.getsize(file_path)

            # проверяем
            if file_size > 0:
                print(f"{file_path!r} - {file_size} bytes")


def move_emty_files(root, dir):
    '''

    :param root: директория где ищем пустые файлы
    :param dir: директория куда перемещаем
    :return:
    '''
    # обход
    for root, dirs, files in os.walk(root):
        # прописываем невключении папки empty_files в проверку (иначе код будет таскать файлы из нее в нее)
        if root == dir:
            continue
        for file in files:
            # сначала генерируем полный путь этого файла
            file_path = os.path.join(root, file)

            # ищем размер этого файла
            file_size = os.path.getsize(file_path)

            if file_size == 0:
                os.rename(file_path, os.path.join(dir, file))
                print(f"{file!r} moved from {root!r} to {dir!r}")


# print_nonempty_files('C:/Users/Администратор/YandexDisk-forfirefox.s/Programming/PyCharm_Projects_2/Udemy_Natalia_Soloviova_2021-2022', topdown=True)
print_nonempty_files('Work', topdown=True)

os.makedirs(EMPTY_DIR)      # создали директорию
move_emty_files('Work', EMPTY_DIR)






