"""
Написать программу, которая создаст приведенное на рисунке дерево директорий и файлов.

Work:
- w.txt
- F1:
    - f11.txt
    - f12.txt
    - f13.txt
- F2:
    - F21:
        - f211.txt
        - f212.txt
- F3:
    - F31
    - F32:
        - f321.txt

Заполните файлы w.txt, f12.txt, f211.txt, f212.txt некоторым текстом.
Выполните обход созданного дерева снизу вверх, а затем сверху вниз и выведите результаты на экран.
Выполните аналогичные действия для ветви с корнем в директории F3.
"""
import os, os.path

dirs = ['Work/F1', 'Work/F2/F21', 'Work/F3/F31', 'Work/F3/F32']
for dir in dirs:
    os.makedirs(dir)

files = {'Work': ['w.txt'],
         'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
         'Work/F2/F21': ['f211.txt', 'f212.txt'],
         'Work/F3/F32': ['f321.txt']}

for dir, files in files.items():
    for file in files:
        file_path = os.path.join(dir, file)
        open(file_path, 'w').close()  # создает пустой файл и сразу же его закрывает

files_with_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
for file in files_with_text:
    with open(file, 'w') as f:
        f.write(f"some sample text for {file!r} file")

# ------------------------

def print_tree(root, topdown):
    print(f"Обход {root!r} {'сверху вниз' if topdown else 'снизу вверх'}")
    for root, dirs, files in os.walk(root, topdown=topdown):
        print(root)
        print(dirs)
        print(files)
    print('-'*50)

print_tree('Work', topdown=False)
print_tree('Work', topdown=True)

print_tree('Work/F3', topdown=False)
print_tree('Work/F3', topdown=True)