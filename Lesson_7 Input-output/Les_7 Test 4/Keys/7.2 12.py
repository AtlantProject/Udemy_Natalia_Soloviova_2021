"""
Дан некоторый файл students.txt, который содержит список студентов (имя и фамилия студента в каждой строке),
отсортированный в алфавитном порядке. Реализуйте следующие функции:

- добавить нового студента в список. Функция должна принимать два параметра: имя и фамилия, -
и добавлять нового студента в файл, не нарушая сортировку списка.

- найти студента. Функция должна принимать один обязательный параметр - фамилия -
и один опциональный параметр - имя. Если передается только фамилия,
то функция должна вывести на экран список всех студентов с данной фамилией или сообщение о том,
что студенты с данной фамилией не найдены. Если в функцию передаются оба параметра,
то она должна вывести на экран сообщение о том, находится ли данный студент в группе.

- редактировать информацию о студенте. Функция должна принимать 2 обязательных параметра:
текущие имя и фамилия студента, - и 2 опциональных параметра: новые имя или фамилия студента.
Функция должна найти студента с заданными параметрами в списке и изменить его имя или фамилию
(или и то, и другое в зависимости от переданных опциональных параметров), сохраняя сортировку списка.
Если заданный студент в списке не найден, необходимо вывести на экран соответствующее сообщение.

- удалить студента. Функция принимает один обязательный параметр - фамилия студента, и 1 опциональный - имя студента.
Если в функцию передана только фамилия студента, и список содержит несколько студентов с указанной фамилией,
то функция должна вывести на экран их список и попросить пользователя ввести также имя студента, и после этого удалить
заданного студента из списка. Если в функцию переданы оба параметра, то она проверяет, находится ли студент в
списке и удаляет его.
Если студент(ы) с заданными параметрами не найдены, должно быть выведено соответствующее сообщение.
"""
from typing import final


FILE_PATH: final = 'files/students.txt'


def read_file(file_path=FILE_PATH):
    students = []
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        name, surname = line.split()
        students.append({'name': name, 'surname': surname})

    return students


def write_file(students, file_path=FILE_PATH):
    students_sorted = sorted(students, key=lambda st: st['name'])
    with open(file_path, 'w') as f:
        for elem in students_sorted:
            f.write(f"{elem['name']} {elem['surname']}\n")


def add_student(name, surname):
    students = read_file()
    print(students)
    students.append({'name': name, 'surname': surname})
    write_file(students)


def find_student(surname, name=None):
    students = read_file()

    if name is None:
        res = list(filter(lambda i: i['surname']==surname, students))
        if not res:
            print(f"Студенты с фамилией {surname!r} не найдены.")
            return []
        print('Найдены студенты:')
        for st in res:
            print(f"{st['name']} {st['surname']}")
        return res

    res = list(filter(lambda i: i['surname']==surname and i['name']==name, students))
    print(f"Студент '{name} {surname}' {'не ' if not res else ''}находится в группе.")
    return res


def edit_student(name, surname, new_name=None, new_surname=None):
    students = read_file()
    st = find_student(surname=surname, name=name)

    if st:
        new_st = {'name': new_name if new_name is not None else name,
                  'surname': new_surname if new_surname is not None else surname}

        students = list(filter(lambda i: i['name']!=name or i['surname']!=surname, students))
        students.append(new_st)
        write_file(students)
        print(f"Изменения произведены успешно!")


def del_student(surname, name=None):
    students = find_student(surname=surname, name=name)

    if len(students) == 0:
        return

    if len(students) > 1:
        name = input('Введите имя студента: ')
        st = list(filter(lambda i: i['name']==name, students))
        if not st:
            print('Неверное имя!')
            return

    all_students = read_file()
    all_students = list(filter(lambda i: (i['name'] != name and name is not None) or i['surname'] != surname, all_students))
    write_file(all_students)
    print(f"Студент '{name+' ' if name is not None else ''}{surname}' успешно удален!")


# add_student(name='Владислав', surname='Колесников')
# add_student(name='Леонид', surname='Мирошниченко')

# find_student('Быкова')
# find_student('Чернышев')
# find_student('Афанасьев')
# find_student(name='Лев', surname='Никитин')
# find_student(name='Андрей', surname='Никитин')

# edit_student(name='Лев', surname='Никитин', new_name='Михаил')
# edit_student(name='Лев', surname='Никитин', new_name='Михаил')  # такого студента больше нет
# edit_student(name='Михаил', surname='Никитин', new_name='Анна', new_surname='Никитина')

# del_student(surname='Макаров')
# del_student(surname='Быкова')
# del_student(surname='Быкова')
# del_student(surname='Ильин')
# del_student(surname='Иванова', name='Злата')
