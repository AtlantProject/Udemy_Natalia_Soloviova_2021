"""
Дана строка, содержащая русскоязычный текст.
Найти количество слов, начинающихся с буквы “е”.

-------------------
Тестовый пример:

Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели. (7 слов)
"""

s = b"Ezheviku dlya ezhat " \
    b"Prinesli dva ezha." \
    b"Ezheviku ele-ele" \
    b"Ezhata vozle eli s'eli."

count_E = s.count(b'E')
count_e = s.count(b' e')
count_res = count_E + count_e
print('Count: ', count_res)

