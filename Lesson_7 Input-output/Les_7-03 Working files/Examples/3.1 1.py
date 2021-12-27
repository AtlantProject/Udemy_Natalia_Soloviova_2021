"""
Создать текстовый файл и записать в него n вещественных чисел.
"""
file_name = 'res_1.txt'

l = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]

def get_line(l):
    l = list(map(str, l))
    return ' '.join(l)

with open(file_name, 'w') as f:
    f.write(get_line(l))

print('Done!')