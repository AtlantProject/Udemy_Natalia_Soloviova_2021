'''
Тема 3: “Циклы со счетчиком”

3.	Вывести на экран следующую последовательность символов:

---------------
Тестовые значения:
	* * * * * * *
	  * * * * *
	    * * *
	      *
	    * * *
	  * * * * *
	* * * * * * *

'''
n = 7
sym = "*"

for i in range(n, 0, -2):
    s = str(sym * i)
    space_count = int((n - i) / 2)
    s = s.rjust(space_count + i)
    print(s)

for i in range(3, n+1, 2):
    s = str(sym * i)
    space_count = int((n - i) / 2)
    s = s.rjust(space_count + i)
    print(s)