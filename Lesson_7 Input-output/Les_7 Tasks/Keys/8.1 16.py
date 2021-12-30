"""
Выведите на экран сначала все файлы, а затем все директории,
расположенные в корневой директории созданного в предыдущей задаче дерева.
"""
import os, os.path


root = 'Work'
objs = os.listdir(root)
objs = list(map(lambda i: os.path.join(root, i), objs))
# print(objs)

objs_sorted = sorted(objs, key=os.path.isfile, reverse=True)    # сортировка происходит от False к True
print(objs_sorted)