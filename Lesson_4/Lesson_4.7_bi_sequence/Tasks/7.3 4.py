"""
Дана строка. Заменить каждый третий символ на звездочку “*”.
"""

s = "Some very-very long string."

bytes_s = s.encode()
bytearr_s = bytearray(bytes_s)

print(bytearr_s)

count = int(len(s)/3)
repl_s = ('*' * count).encode()
bytearr_s[2::3] = repl_s

print(bytearr_s)
print(bytearr_s.decode())