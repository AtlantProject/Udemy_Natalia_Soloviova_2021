"""
Дано несколько строк: "First $99.01 Second $88.09", "Second $15.67 Third $8.19", "Fourth $20.2 Fifth $105.5".
Используя форматированный вывод, выведите данные строки в форме таблицы
(поочередно с выравниванием по левому или по правому краю).
Например:

First		$99.01		Second	    $88.09
Second	    $15.67 	    Third 		$8.19
Fourth 		$20.2 		Fifth 		$105.5
"""

rows = ["First $99.01 Second $88.09", "Second $15.67 Third $8.19", "Fourth $20.2 Fifth $105.5"]

for row in rows:
    name1, pr1, name2, pr2 = row.split()
    print(f"{name1:10}{pr1:10}{name2:10}{pr2:10}")

print("*"*50)
for row in rows:
    name1, pr1, name2, pr2 = row.split()
    print(f"{name1:>10}{pr1:>10}{name2:>10}{pr2:>10}")