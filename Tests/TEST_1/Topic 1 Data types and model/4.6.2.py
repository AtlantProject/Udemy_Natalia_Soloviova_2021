'''
2.	Дана строка: “Th$e *ly-ri cs; i!s >no>t *th&at$ p=oo+r!$”.
Представить данную строку в виде массива байт и удалить из нее
каждый третий символ, начиная с третьего.
Вывести полученную строку на экран.
'''

s = "Th$e *ly-ri cs; i!s >no>t *th&at$ p=oo+r!$"
byte_arr = bytearray(s.encode())
print(byte_arr)

del byte_arr[2::3]
print(byte_arr.decode())
