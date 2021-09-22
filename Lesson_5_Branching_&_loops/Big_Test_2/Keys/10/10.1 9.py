"""
Вывести на экран следующую последовательность символов:

	* * * * * * *
	  * * * * *
	    * * *
	      *
	    * * *
	  * * * * *
	* * * * * * *

"""
n = 7
sym = '*'

for i in range(n, 0, -2):
    s = str(sym*i)
    space_count = int((n-len(s))/2)
    s = s.rjust(space_count + len(s))
    print(s)

for i in range(3, n+1, 2):
    s = str(sym * i)
    space_count = int((n - len(s)) / 2)
    s = s.rjust(space_count + len(s))
    print(s)

