"""
Написать функцию, принимающую некоторую информацию о сотруднике и выводящую ее на экран согласно следующему шаблону:
    имя
    фамилия
    пустая строка (в случае наличия других полей)
	другие поля в алфавитном порядке их заголовков
	разделитель, состоящий из записанных подряд 30-ти дефисов “-”.

Например:
	Name: Anna
	Last Name: Minker

	Age: 27
	Phone: 123456789
	------------------------------
	Name: John
	Last Name: Bold

	Age: 32
	Country: USA
	Email: john.bold.@mail.com
	Phone: 987654321

Если переданная информация не содержит имени или фамилии сотрудника, вывести сообщение об ошибке.


-------------
Тестовые значения:
(name='Anna', surname='Minker', age=27, phone=123456789)
(name='John', surname='Bold', country='USA', email='aaa@com', phone='987654321', age=32)
(name='Sonia', surname='Moon')
(name='Alex')
"""
def print_info(**kwargs):
       if 'name' not in kwargs or 'surname' not in kwargs:
              print('invalid data')
              # return None        # отсановка цикла. можно и так оставить, а можно и через else
       else:
              print('Name: ', kwargs['name'])
              print('Last name: ', kwargs['surname'])

       if len(kwargs) > 2:
              print()
              keys = list(kwargs.keys())[2:]
              keys.sort()
              for k in keys:
                     print(k, ': ', kwargs[k])

       print('-' * 30)

print_info(name='Anna', surname='Minker', age=27, phone=123456789)
print_info(name='John', surname='Bold', country='USA', email='aaa@com', phone='987654321', age=32)
print_info(name='Sonia', surname='Moon')
print_info(name='Alex')

