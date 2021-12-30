"""
Удалите из дерева директорий, созданного в первой задаче, ветвь, расположенную под директорией F2,
а также все пустые директории, выводя соответствующие сообщения на экран.
"""
import os, os.path

def remove_empty_dirs(root_tree):
    print(f"Удаление пустых директорий в ветви {root_tree!r}")
    print('-'*50)

    for root, dirs, files in os.walk(root_tree):
        if not os.listdir(root):
            os.rmdir(root)
            print(f"Директория {root!r} удалена.")

    print('-'*50)


def remove_tree(root_tree):
    print(f"Удаление ветви {root_tree!r}")
    print('-' * 50)

    for root, dirs, files in os.walk(root_tree, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Файл {file_path!r} удален.")

        if root != root_tree:
            os.rmdir(root)
            print(f"Директория {root!r} удалена.")

    print('-' * 50)


remove_empty_dirs('Work')
remove_tree('Work/F2')