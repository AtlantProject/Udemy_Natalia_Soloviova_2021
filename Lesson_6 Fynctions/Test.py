l = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]

# def is_prime(n):
#     for i in range(2, n//2+1):
#         if n%i == 0:
#             return False    # если не простое
#     return True             # если простое
#
# def is_neutral(n):
#     return n in [0, 1]      # 0 и 1 - нейтральные числа, не прост

for n in l:

    for i in range(2, n//2+1):
        if n % i == 0:
            print(f"Не простое - {i}")
            # return False    # если не простое
    # return True             # если простое
    print(f"Простое - {i}")
    if n in [0, 1]:
        continue

# def is_neutral(n):
#     return n in [0, 1]      # 0 и 1 - нейтральные числа, не прост