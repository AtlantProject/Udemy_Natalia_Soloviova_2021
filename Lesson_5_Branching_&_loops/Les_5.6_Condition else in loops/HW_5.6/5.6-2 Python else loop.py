l = "Python else loop"
laoe = ["la", "lo", "le"]

# lo = "lo"
# le = "le"
# решение задачи № 1
'''
for i in l:
    if i == "l" and (l[l.index(i) + 1] == "o" or l[l.index(i) + 1] == "o" or l[l.index(i) + 1] == "e"):
        print(i, "следующая буква - ", l[l.index(i) + 1])
        break
else:
    print("Искомая комбинация не найдена")
'''
for i in l:
    if i == "l":
        for i in laoe:
            if i in l:
                print(i)
        break
else:
    print("Искомая комбинация не найдена")

# решение задачи № 2


