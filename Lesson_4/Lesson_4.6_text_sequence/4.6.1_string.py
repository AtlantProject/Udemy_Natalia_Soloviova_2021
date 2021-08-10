s = "1 2 3 4 5 6 7 8"
print(s)

sp = s.split()
print(sp)

sp = s.split(maxsplit=1)
print(sp)

sp = s.split(maxsplit=2)
print(sp)

print("1,2,3".split(","))               # ['1', '2', '3']
print("1,2,3".split(",", maxsplit=1))   # ['1', '2,3']
print("1,2,,3,".split(","))             # ['1', '2', '', '3', '']
