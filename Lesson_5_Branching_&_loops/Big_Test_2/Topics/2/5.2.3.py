l = [2,3,4,5,56,7,8,6,4,3,21,12,70,45,5,46]

s = len(l)
k = 0
su = 0
while s > 0:
    for i in l:
        if i % 7 == 0:
            su += i
            k += 1
            print(i)
        s -= 1

print(su, k, su/k)

