"""
В файлах “AI_students.txt” и “IS_students.txt” содержится информация о студентах,
обучающихся по специальностям “Прикладная информатика” и “Защита информации” соответственно.
Каждая строка в указанных файлах содержит информацию об одном конкретном студенте в следующем формате:

[Фамилия] [Имя] [Отчество] [дата рождения] [балл при поступлении] [курс] [группа] [средний балл]

Например:
Дмитриев Иван Петрович 12.5.2003 76 1 ПИ-11 4.3
Любимова Мария Ивановка 05.08.2000 98 4 ЗИ-42 5.0

С помощью модуля texttable выведите на экран в виде таблицы информацию о студентах,
обучающихся на обеих специальностях, отсортированную по названию специальности и фамилии студента
(внутри каждой специальности) в следующем формате:

Фамилия И.О. | дата рождения | специальность | курс | группа | балл при поступлении | средний балл
"""
import texttable
from Students import Students


students_AI_file = 'AI_students.txt'
students_IS_file = 'IS_students.txt'

students_AI = Students(students_AI_file, 'Applied Informatics')
students_IS = Students(students_IS_file, 'Information Security')

all_students = students_AI.get_students_list(sort=True)
all_students.extend(students_IS.get_students_list(sort=True))
# print(data)

# Фамилия И.О. | дата рождения | специальность | курс | группа | балл при поступлении | средний балл
table = texttable.Texttable()
table.set_cols_align(['l', 'l', 'l', 'c', 'c', 'c', 'c'])
table.set_cols_width([20, 15, 25, 6, 10, 10, 10])
table.set_precision(1)

headers = ['Name', 'Birthday', 'Speciality', 'Year', 'Group', 'Entry points', 'Avg points']
data = [headers]
data.extend(all_students)
table.add_rows(data)
print(table.draw())