"""
Написать функцию, которая выводит на экран первые N строк треугольника Паскаля.
*Треугольник Паскаля - это бесконечная таблица чисел, имеющая форму треугольника,
в котором на вершине и по бокам стоят единицы, а каждый центральный элемент равен сумме двух элементов,
расположенных над ним.

     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
"""
def get_row(prev_row):
       row = [1]
       for i in range(0, len(prev_row) - 1):
              row.append(prev_row[i] + prev_row[i + 1])
       row.append(1)
       return row


def print_tr_Pascal(n):
       cur_row = [1]
       for i in range(1, n+1):
              print(cur_row)
              next_row = get_row(cur_row)
              cur_row = next_row

print_tr_Pascal(5)
