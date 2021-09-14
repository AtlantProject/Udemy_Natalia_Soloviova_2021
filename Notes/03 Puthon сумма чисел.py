a = sum(i for i in range(1, 5) if i % 2)
print(a)

def fn(N, x):
    sum = 0
    for i in range(N):
        if i%x:
            sum += i
    return sum

