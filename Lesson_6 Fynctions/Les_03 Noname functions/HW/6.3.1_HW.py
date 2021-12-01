# 6.3.1 ДЗ сортировка списка кортежей

l = [('asdf', 'weuhw', 'qqer'), ('awfewf', 'sfjo', 'bcjhiq'), ('ijae', 'wua', 'iquheqi')]
print(l)
print(l[0])
print(l[0][-1])
print(l[0][-1][-1])

l_sort = sorted(l, key=lambda i: i[1][-1])

print(l_sort)