"""
Создайте многомодульные программы на основе иерархий классов, разработанных в предыдущей контрольной работе:
“Array” - “AndArray” - “OrArray”, - с соблюдением следующих условий:
- каждый класс должен быть оформлен в виде отдельного модуля;
- каждый модуль должен содержать строки документации;
- каждый модуль в случае, если он был импортирован, должен выводить на экран соответствующую информацию,
включающую название модуля и имя автора;
- демонстрация работы с классами должна осуществляться в главном модуле;
- демонстрация работы с классами должна осуществляться только в случае автономного запуска главного модуля.
"""
from OrArray import OrArray
from AndArray import AndArray

if __name__ == "__main__":
    print('-'*50)
    arr1 = AndArray(1,2,3,4,5,6,7,8,9)
    arr2 = AndArray(3,6,8,0,2)
    arr1.plus(arr2)
    arr1.edit_elem()

    print()

    arr3 = OrArray(3,4,5,9,1,7,13)
    arr3.plus(arr2)
    arr3.edit_elem()