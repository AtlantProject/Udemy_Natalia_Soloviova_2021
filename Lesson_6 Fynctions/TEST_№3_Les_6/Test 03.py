
n = 100

for i in range(2, n//2+1):
    if n%i == 0:
        print(f"False - {n%i}, i = {i}")
    else:
        print(f"True {i}")
