nums = [i for i in range(5, 26)]
# print(nums)

for i in nums:
    if i % 3 == 0 or i % 6 == 0:
        continue
    elif i % 5 == 0:
        print(f"{i} кратно 5")
    else:
        print(i)