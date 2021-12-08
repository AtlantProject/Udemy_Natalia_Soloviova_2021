nums = [i for i in range(1, 10)]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums)
k = 0
sum = 0

for i in nums:
    if sum >= 15:
        break
    sum += i
    k += 1

print(f"sum = {sum}")
print(f"k = {k}")