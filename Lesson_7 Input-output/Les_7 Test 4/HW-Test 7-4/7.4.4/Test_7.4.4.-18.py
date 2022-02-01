"""
Удалите из дерева директорий, созданного в первой задаче, ветвь, расположенную под директорией F2,
а также все пустые директории, выводя соответствующие сообщения на экран.
"""
import os, os.path


def remove_empty_dirs(root_tree):
    '''
    Функция удаляет все пустые директории.
    Эта функция предназначена только для пустых директорий.

    :param root_tree:
    :return:
    '''
    print(f"Удаление пустых директорий в ветви {root_tree!r}")
    print('-' * 50)

    # обход
    for root, dirs, files in os.walk(root_tree):
        # проверяем есть ли внутри директории хотя бы что-то
        if not os.listdir(root):
            # удаляем данную директорию
            os.rmdir(root)
            print(f"Директория {root!r} удалена.")

    print('-' * 50)


# Удалите из дерева директорий, созданного в первой задаче, ветвь, расположенную под директорией F2
def remove_tree(root_tree):
    print(f"Удаление ветви {root_tree!r}")
    print('-' * 50)

    # снова начинаем обход дерева с самого конца (идем с низу)
    for root, dirs, files in os.walk(root_tree, topdown=False):
        for file in files:
            # генерируем полный путь к файлу
            file_path = os.path.join(root, file)
            # удаляем этот файл
            os.remove(file_path)
            print(f"Файл {file_path!r} удален!")

# после удаления файла можем удалить саму директорию
# саму директорию F2 мы не должны трогать
        if root != root_tree:
            # можем воспользоваться os.rmdir() так как выше удалили все файлы из этой директории
            os.rmdir(root)
            print(f"Директория {root!r} удалена!")

    print('-' * 50)



remove_empty_dirs('Work')
remove_tree('Work/F2')

