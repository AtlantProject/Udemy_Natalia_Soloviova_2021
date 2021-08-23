"""
Преобразовать заданную строку в читаемый текст:
'4865 6c6c 6f2c 2062 7974 6573 21'
"""

hex_s = '4865 6c6c 6f2c 2062 7974 6573 21'
bytes_s = bytes.fromhex(hex_s)

print(bytes_s)
print(bytes_s.decode())
