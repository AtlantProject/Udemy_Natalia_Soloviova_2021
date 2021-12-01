"""
Дан список чисел. Используя lambda-функцию, возведите в квадрат и в куб все элементы данного списка.
"""
nums = [3,5,7,3,9,5,7,2]

square_nums = list(map(lambda i: i**2, nums))
cube_nums = list(map(lambda i: i**3, nums))

print(square_nums)
print(cube_nums)