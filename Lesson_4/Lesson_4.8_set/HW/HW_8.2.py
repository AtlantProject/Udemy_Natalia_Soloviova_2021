a = {0, 1, 2, 3, 4}
b = {3, 4, 5, 6, 7}
c = {0, 1, 6, 7, 8}

result = (a - b) - c == (a - c) - (b - c)
print(result)