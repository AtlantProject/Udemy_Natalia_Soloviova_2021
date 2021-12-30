"""
Отредактируйте файл w.txt, созданный в первой задаче, следующим образом:
после 10-го символа, вставьте строку "--- truncate here ---", а затем обрежьте оставшуюся часть файла.
Выведите содержимое полученного файла на экран.
"""
import os

file_path = 'Work/w.txt'

ins_row = "--- truncate here ---"

f = open(file_path, 'r+')
f.seek(10)
f.write(ins_row)
f.close()

os.truncate(file_path, 10+len(ins_row))
