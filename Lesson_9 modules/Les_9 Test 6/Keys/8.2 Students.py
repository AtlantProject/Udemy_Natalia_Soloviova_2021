class Student:
    def __init__(self, surname, first_name, second_name, birthday,
                 speciality, year, group, entry_points, avg_points):
        self.surname = surname
        self.first_name = first_name
        self.second_name = second_name
        self.birthday = birthday
        self.speciality = speciality
        self.year = year
        self.group = group
        self.entry_points = entry_points
        self.avg_points = avg_points

    def get_info(self):
        name = f'{self.surname} {self.first_name[0]}.{self.second_name[0]}.'
        return [name, self.birthday, self.speciality, self.year, self.group,
                self.entry_points, self.avg_points]

    def get_short_info(self):
        name = f'{self.surname} {self.first_name[0]}.{self.second_name[0]}.'
        return [name, self.birthday, self.speciality, self.group, self.avg_points]



# Фамилия И.О.  | дата рождения  | специальность  | группа  | средний балл
class Students:
    def __init__(self, file_name, speciality):
        self.students_list = Students.load_students_list(file_name, speciality)

    @staticmethod
    def load_students_list(file_name, speciality):
        with open(file_name, 'r') as f:
            st_list = f.readlines()
        # print(st_list)

        students = []
        for st in st_list:
            if st.endswith('\n'):
                st = st[:-1]
            sur, f_name, s_name, birth, entry_p, year, group, avg_p = st.split()
            students.append(Student(sur, f_name, s_name, birth, speciality,
                                    int(year), group, int(entry_p), float(avg_p)))

        return students

    def sort_by_surname(self):
        self.students_list = sorted(self.students_list, key=lambda st: st.surname)

    def get_students_list(self, sort=False, year=None, short_info=False):
        if sort:
            self.sort_by_surname()

        st_list = []
        for st in self.students_list:
            if year is not None and st.year != year:
                continue
            st_list.append(st.get_info() if not short_info else st.get_short_info())
        return st_list