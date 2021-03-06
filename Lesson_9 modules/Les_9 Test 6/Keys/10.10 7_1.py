"""
Создайте многомодульные программы на основе иерархий классов, разработанных в предыдущей контрольной работе:
“Liquid’ - “Alcohol”, - с соблюдением следующих условий:
- каждый класс должен быть оформлен в виде отдельного модуля;
- каждый модуль должен содержать строки документации;
- каждый модуль в случае, если он был импортирован, должен выводить на экран соответствующую информацию,
включающую название модуля и имя автора;
- демонстрация работы с классами должна осуществляться в главном модуле;
- демонстрация работы с классами должна осуществляться только в случае автономного запуска главного модуля.
"""
from Alcohol import Alcohol


if __name__ == "__main__":
    print('-'*50)
    a = Alcohol('Vine', 1064.2, 0.14)
    a.print_info()

    a.edit_density(1000)
    a.print_info()

    print()

    a.calc_m(0.5)
    a.calc_v(300)

    print()

    a.print_info()
    a.edit_strength(0.2)
    a.print_info()

