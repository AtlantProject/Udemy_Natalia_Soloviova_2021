a = set("abracadabra")
print(a)    # {'r', 'a', 'c', 'b', 'd'}
b = set("alakazam")
print(b)    # {'z', 'm', 'k', 'a', 'l'}

c = a - b
print(c)    # {'r', 'c', 'b', 'd'}

d = a | b
print(d)    # {'r', 'l', 'a', 'z', 'm', 'c', 'k', 'b', 'd'}

e = a & b
print(e)    # {'a'}

f = a ^ b
print(f)    # {'d', 'c', 'z', 'm', 'r', 'k', 'b', 'l'}