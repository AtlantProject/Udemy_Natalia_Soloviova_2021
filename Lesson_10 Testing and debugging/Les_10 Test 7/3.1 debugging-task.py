"""
Дан список чисел [2,3,4,5,6,7,8,9]. Найти среди них и вывести на экран все числа,
являющиеся делителями заданного пользователем числа.

---------------
Тестовые значения:
18 -> [2,3,6,9]
12 -> [2,3,4,6]
11 -> []
25 -> [5]
.....
"""

numbers = range(2, 9)
dividend = int(input('Введите число: '))     # не преобразовано к int
isDivisor = False

for i in range(0, len(numbers)):
    divisor = numbers[0]

    if dividend % divisor != 0:
        isDivisor = True

    if isDivisor:
        print(f'{divisor} - делитель числа {dividend}!')        # ' кавычка не в конце
