# разряды

n = int(input("Введите целое чивло - "))


digit = "2"
sequence = []
print(sequence)

for i in range(1, n+1):
    sequence.append(int(digit * n))
    n -= 1
    print(n)
print(sequence)

# отсортировал последовательность
sequence.sort()
print(sequence)

# нашел сумму входящих в последовательность чисел
s = sum(sequence)
print(s)




