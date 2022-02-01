"""
Выведите на экран сначала все файлы, а затем все директории,
расположенные в корневой директории созданного в предыдущей задаче дерева.
"""
import  os, os.path

# обозначаем корневую директорию дерева
root = 'Work'

# получаем все объекты, к-е находятся в этой папке
objs = os.listdir(root)

# преобразуем objs в список, содержащий ПУТИ к данному объекту
objs = list(map(lambda i: os.path.join(root, i), objs))

print(objs)

# сортируем от файла к директории
objs_sorted = sorted(objs, key=os.path.isfile, reverse=True)    # сортировка происходит от False к True

print(objs_sorted)


