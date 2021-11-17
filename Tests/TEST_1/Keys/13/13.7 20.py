"""
Перечень сетевых интерфейсов и основная информация о них представлены в виде следующей структуры данных:
[{'interface': 'Ethernet0', 'ip': '1.1.1.1', 'status': 'up'},
{'interface': 'Ethernet1', 'ip': '2.2.2.2', 'status': 'down'},
{'interface': 'Serial0', 'ip': '3.3.3.3', 'status': 'up'},
{'interface': 'Serial1', 'ip': '4.4.4.4', 'status': 'up'}].

- выведите на экран общее количество интерфейсов
- выведите на экран информацию (название, ip-адрес и статус), соответствующую второму интерфейсу в списке
- выведите на экран статус последнего интерфейса в списке
- проверьте, добавлена ли графа 'notes' для первого интерфейса и выведите ее содержимое на экран.
Если такой графы нет, то сперва добавьте ее с текстом "need to reset"
- добавьте в список еще один ethernet интерфейс с ip-адресом, как у третьего интерфейса, и статусом 'down'.
После этого измените ip-адрес третьего интерфейса на '3.3.3.4'
- выведите на экран содержимое графы 'notes' первого интерфейса, а затем удалите ее
- переведите четвертый интерфейс в состояние 'down', а затем удалите его из списка
"""

interf = [{'interface': 'Ethernet0', 'ip': '1.1.1.1', 'status': 'up'},
          {'interface': 'Ethernet1', 'ip': '2.2.2.2', 'status': 'down'},
          {'interface': 'Serial0', 'ip': '3.3.3.3', 'status': 'up'},
          {'interface': 'Serial1', 'ip': '4.4.4.4', 'status': 'up'}]

print('Interfaces count: ', len(interf))
print('The second interface: ', interf[1])
print('The last interface: ', interf[-1])

interf[0].setdefault('notes', "need to reset")
print(interf[0])

interf.append({'interface': 'Ethernet2', 'ip': interf[2]['ip'], 'status': 'down'})
interf[2]['ip'] = '3.3.3.4'
print(interf)

print(interf[0].pop('notes'))
print(interf)

interf[3]['status'] = 'down'
print(interf[3])

del interf[3]
print(interf)
