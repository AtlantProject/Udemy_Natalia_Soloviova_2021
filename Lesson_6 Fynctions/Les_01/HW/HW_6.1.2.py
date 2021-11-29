l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# функция поиска четного числа
def chet_num(n):
    if n % 2 == 0:
        return n    # возвращает четное число

# for i in l:
#     if chet_num(i):
#         print(f"{i} - четное число")

for i in l:
    for j in range(i + 1):
        sum_chet = 0
        if chet_num(i):
            sum_chet += i
    print(f"Для {i} сумма четных цифр = {sum_chet}")



