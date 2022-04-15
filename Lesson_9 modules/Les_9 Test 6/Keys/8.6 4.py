"""
В списках студентов из предыдущей задачи найдите всех студентов, обучающихся на 5 курсе,
и с помощью модуля random случайным образом распределите их на несколько групп (по датам)
для защиты выпускной квалификационной работы (ВКР) таким образом, чтобы в каждой группе оказалось
не более 5-ти человек. Используя модуль texttable выведите на экран в виде отдельных таблиц информацию
о студентах, отсортированных по фамилии в алфавитном порядке, из каждой полученной группы в следующем формате:

Дата защиты ВКР
Фамилия И.О.  | дата рождения  | специальность  | группа  | средний балл
"""
import random
import texttable
from Students import Students



students_AI_file = 'AI_students_upd.txt'
students_IS_file = 'IS_students_upd.txt'

students_AI = Students(students_AI_file, 'Applied Informatics')
students_IS = Students(students_IS_file, 'Information Security')

all_students = students_AI.get_students_list(year=5, short_info=True)
all_students.extend(students_IS.get_students_list(year=5, short_info=True))

# print(all_students)
random.shuffle(all_students)
# print(all_students)

max_st_per_day = 5
cur_day = 1
st_by_days = {}
for i in range(0, len(all_students), max_st_per_day):
    st_by_days[cur_day] = all_students[i:i+max_st_per_day]
    cur_day += 1

print(st_by_days)

# Дата защиты ВКР
# Фамилия И.О.  | дата рождения  | специальность  | группа  | средний балл
table = texttable.Texttable()
table.set_cols_align(['l', 'l', 'l', 'c', 'c'])
table.set_cols_width([20, 15, 25, 6, 10])
table.set_precision(1)

headers = ['Name', 'Birthday', 'Speciality', 'Group', 'Avg points']

for day, st_list in st_by_days.items():
    print(f'\nThe {day} day:\n')
    data = [headers]
    st_list = sorted(st_list, key=lambda s: s[0])
    data.extend(st_list)
    table.add_rows(data)
    print(table.draw())
    table.reset()

