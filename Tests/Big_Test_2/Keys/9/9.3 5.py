"""
Вычислить значение выражения для заданного N:

y = 1 + ln2/1! + ln3/2! + ln4/3! + ... + ln(N+1)/N!

---------------
Тестовые значения:
N=3     1 + ln(2) + ln(3)/2 +  ln(4)/6 = 2.47
N=5     1 + ln(2) + ln(3)/2 +  ln(4)/6 + ln(5)/24 + ln(6)/120 = 2.56
"""
from math import log

N = 5

i = 2
y = 1

while i <= N+1:
    fact = 1
    j = 1
    while j < i:      # (i-1)!
        fact *= j
        j += 1

    y += log(i)/fact
    i += 1

print(round(y, 2))
