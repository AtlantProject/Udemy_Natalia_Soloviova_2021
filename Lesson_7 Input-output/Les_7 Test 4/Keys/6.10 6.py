"""
Дан кортеж, состоящий из 4х элементов: (2, 123.4567, 10000, 12345.67).
Используя форматированный вывод, преобразуйте данные значения в следующую строку:
'File_002 :      123.46,  1.00e+04,  1.23e+04'
"""

l = (2, 123.4567, 10000, 12345.67)

tmpl = 'File_{0:03} :\t{1:.2f},\t{2:.2e},\t{3:.2e}'
print(tmpl.format(*l))
