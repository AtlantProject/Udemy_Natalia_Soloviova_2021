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

# оформили как константу
FILE_PATH: final = "files/students.txt"


def read_file(file_path=FILE_PATH):
    students = []
    # with open(file_path, 'r', encoding="UTF-8") as f:
    with open(file_path, 'r', encoding="Windows-1251") as f:
        lines = f.readlines()

    for line in lines:
        name, surname = line.split()
        students.append({'name': name, 'surname': surname})

    return students


def write_file(students, file_path=FILE_PATH):
    students_sorted = sorted(students, key=lambda st: st['name'])   # отсортировали по имени студента
    with open(file_path, 'w') as f:
        for elem in students_sorted:
            f.write(f"{elem['name']} {elem['surname']}\n")      # запись в файл


def add_student(name, surname):
    students = read_file()
    print(students)
    students.append({'name': name, 'surname': surname})     # Добавили нового студента
    write_file(students)


def find_student(surname, name=None):
    students = read_file()      # получаем список студентов
    '''
    Эта функция нам возвратит:
    1. пустой список
    или
    2. список из одного элемента
    или
    3. список из нескольких элементов
    '''


    if name is None:
        res = list(filter(lambda i: i['surname'] == surname, students))     # фильтруем список студентов по фамилии
        if not res:
            print(f"Студенты с фамилией {surname!r} не найдены.")
            return []     # просто прерываем выполнение функции
        print("Найдены студенты:")      # если студенты найдены

        # выводим студентов на экран
        for st in res:
            print(f"{st['name']} {st['surname']}")
        return res

    # пишем что случится если имя задано
    res = list(filter(lambda i: i['surname'] == surname and i['name']==name, students))
    print(f"Студент '{name} {surname}' {'не ' if not res else ''}находится в группе")
    print("*" * 50)
    return res


def edit_student(name, surname, new_name=None, new_surname=None):
    # Сначала читаем файл
    students = read_file()
    # ищем студента
    st = find_student(surname=surname, name=name)

    # if len(st) == 0:    # если студента не нашли
        # сама функция find_student() выведет сообщение, что студента такого нет
        # поэтому не используем эту конструкцию

    # если студенты найдены
    if st:
        # создаем нового студента с новой фамилией и именем
        new_st = {'name': new_name if new_name is not None else name,
                  'surname': new_surname if new_surname is not None else surname}

        # удаляем старого студента
        # после этого фльтра в тудентах останутся все студенты кроме заданного
        students = list(filter(lambda i: i['name'] != name or i['surname'] != surname, students))

        # добавляем нового студента
        students.append(new_st)

        # сортируем список и записываем в файл
        write_file(students)
        print("Изменения произведены успешно!")


def del_student(surname, name=None):
    # Ищем студентов
    students = find_student(surname=surname, name=name)

    if len(students) == 0:
        return

    if len(students) > 1:
        name = input('Введите имя студента: ')

        # проверяем существует ли студент в нашем списке
        st = list(filter(lambda i: i['name'] == name, students))

        # если студент не найден
        if not st:
            print('Неверное имя!')
            # теоретически в цикле мы могли бы запрашивать имя пока пользователь не введет правильное имя
            return

    # получаем список всех студентов
    all_students = read_file()
    all_students = list(filter(lambda i: (i['name'] != name and name is not None) or i['surname'] != surname, all_students))
    write_file(all_students)
    print(f"Студент '{name + ' ' if name is not None else ''}{surname}' успешно удален!")







# add_student(name='Alex', surname='Smit')
# add_student(name='Боба', surname='Фет')

# find_student('Филиппов')
# find_student('Рожкова')
# find_student('Ильин')
# find_student('Кривой')
# find_student(name='Лев', surname='Никитин')
# find_student(name='Андрей', surname='Никитин')

# edit_student(name='Лев', surname='Никитин', new_name='Михало007')
# edit_student(name='Лев', surname='Никитин', new_name='Михало007')   # такого студента нет
# edit_student(name='Михало007', surname='Никитин', new_name='Анна', new_surname='Никитинааааа')

# del_student(surname='Маккров')
# del_student(surname='Филиппов')


# TODO: Доанализировать задачу