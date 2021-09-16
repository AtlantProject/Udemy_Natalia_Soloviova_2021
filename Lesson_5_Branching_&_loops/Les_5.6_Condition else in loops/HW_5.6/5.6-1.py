# numbers = [i for i in range(1, 33)]
numbers = [1, 3, 5]
print(numbers)

for n in numbers:
    if n % 2 == 0:
        print(f"Четное число {n}")
        break
else:
    print("Четные числа не найдены")
