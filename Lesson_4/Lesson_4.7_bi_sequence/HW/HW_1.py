s = 'Lorem Ipsum - eto tekst-"riba".'

s_byte = bytearray(b'Lorem Ipsum - eto tekst-"riba".')
print(s_byte)

s_2 = 'Лорем Ипсум   это текст "рыба", часто используемый в печати и вэб-дизайне. '
s_2.encode("utf-8")
s_2_bytes = s_2.encode("utf-8")

print(s_2_bytes)
