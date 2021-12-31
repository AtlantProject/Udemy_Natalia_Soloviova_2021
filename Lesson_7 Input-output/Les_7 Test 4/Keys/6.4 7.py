"""
Решите предыдущую задачу, используя поочередно другие два метода форматирования строк.
"""

l = (2, 123.4567, 10000, 12345.67)

# method format()
print('Method format():')
tmpl = 'File_{0:03} :\t{1:.2f},\t{2:.2e},\t{3:.2e}'
print(tmpl.format(*l))

# f-strings
print('\nf-strings:')
print(f'File_{l[0]:03} :\t{l[1]:.2f},\t{l[2]:.2e},\t{l[3]:.2e}')

# old style
print('\nOld style: ')
print('File_%03d :\t%.2f,\t%.2e,\t%.2e' % l)
