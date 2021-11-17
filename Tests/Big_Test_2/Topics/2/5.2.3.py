# l = [2,3,4,5,56,7,8,6,4,3,21,12,70,45,5,46]
l = [2.4, 6.2, 7.0, 14.0, 0.7, 12.4]
'''
# Мой пробный код

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
'''

i = 0   # Счетчик
nums = []   # Числа кратные 7

# Цикл
while i < len(l):
    if l[i] % 7 == 0:
        nums.append(l[i])
    i += 1

if nums:
    res = sum(nums)/len(nums)
    print(res)
else:
    print("Таких чисел не найдено")