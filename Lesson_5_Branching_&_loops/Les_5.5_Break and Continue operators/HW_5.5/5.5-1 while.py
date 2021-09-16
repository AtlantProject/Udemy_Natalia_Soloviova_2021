# nums = [i for i in range(1, 10)]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums)
k = 0
sum = 0

while True:
    for i in nums:
        if sum < 15:
            sum += i
            print(f"sum = {sum}")
            k += 1
            print(f"k = {k}")
    break

print(f"sum = {sum}")
print(f"k = {k}")
