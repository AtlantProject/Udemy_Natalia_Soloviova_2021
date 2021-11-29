l = [i for i in range(1, 101)]
print(l)
# n = 24

def delit(n):
    count_of_dividers = 0
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            # print(i, end= " ")
            count_of_dividers += count_of_dividers
    return count_of_dividers

for i in l:
    if delit(i):
        print(f"Для числа {i} количество делителей - {delit(i)}\n")


