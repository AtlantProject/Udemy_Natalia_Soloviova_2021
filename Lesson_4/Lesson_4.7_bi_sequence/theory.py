# Общие методы бинарных последовательностей

a = "abc"
b = a.replace("a", "f")
print(b)
# fbc

a = b"abc"
b = a.replace(b"a", b"f")
print(b)
# b'fbc'

a = b'1,2,3'.split(b',')
print(a)
# [b'1', b'2', b'3']

a = b'1,2,3'.split(b',', maxsplit=1)
print(a)
# [b'1', b'2,3']

a = b'            spacios              '.lstrip()
print(a)
# b'spacios

a = b'www.example.com'.lstrip(b'cmowz.')
print(a)
# b'example.com'

a= b'01\t012\t0123\t01234'.expandtabs()
print(a)
# b'01      012     0123    01234'

a= b'01\t012\t0123\t01234'.expandtabs(4)
print(a)
# b'01  012 0123    01234'