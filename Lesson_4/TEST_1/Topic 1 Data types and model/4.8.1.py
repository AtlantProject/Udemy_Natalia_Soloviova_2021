'''
1.	Перечень сетевых интерфейсов и основная информация о них представлены
в виде следующей структуры данных:
[{‘interface’: ‘Ethernet0’, ‘ip’: ‘1.1.1.1’, ‘status’: ‘up’},
{‘interface’: ‘Ethernet1’, ‘ip’: ‘2.2.2.2’, ‘status’: ‘down’},
{‘interface’: ‘Serial0’, ‘ip’: ‘3.3.3.3’, ‘status’: ‘up’},
{‘interface’: ‘Serial1’, ‘ip’: ‘4.4.4.4’, ‘status’: ‘up’}].
a.	выведите на экран общее количество интерфейсов
b.	выведите на экран информацию (название, ip-адрес и статус), соответствующую второму интерфейсу в списке
c.	выведите на экран статус последнего интерфейса в списке
d.	проверьте, добавлена ли графа ‘notes’ для первого интерфейса и выведите
ее содержимое на экран. Если такой графы нет, то сперва добавьте ее с
текстом “need to reset”
e.	добавьте в список еще один ethernet интерфейс с ip-адресом, как у
третьего интерфейса, и статусом ‘down’. После этого измените ip-адрес
третьего интерфейса на ‘3.3.3.4’
f.	выведите на экран содержимое графы ‘notes’ первого интерфейса,
а затем удалите ее
g.	переведите четвертый интерфейс в состояние ‘down’, а затем удалите
его из списка

'''

interf = [{'interface': 'Ethernet0', 'ip': '1.1.1.1', 'status': 'up'},
          {'interface': 'Ethernet1', 'ip': '2.2.2.2', 'status': 'down'},
          {'interface': 'Serial0', 'ip': '3.3.3.3', 'status': 'up'},
          {'interface': 'Serial1', 'ip': '4.4.4.4', 'status': 'up'}]
print(interf)
# common_interf = len(interf('interface'))
# print(common_interf)
# a
print(f"Interfaces count: {len(interf)}")

# b
print("the second interface - ", interf[1])

# c
print("status последнего интерфейса в списке: ", interf[-1]['status'])

# d
interf[0]['notes'] = 'need to reset'
print("nones in interf - ", 'notes' in interf[0])

# e
# interf = {'interface': 'Serial0', 'ip': '3.3.3.3', 'status': 'down'}
# print(interf)

interf.append({'interface': 'Ethernet2', 'ip': interf[2]['ip'], 'status': 'down'})
print(interf)

interf[2]['ip'] = '3.3.3.4'
print(interf)

# f
# print(f"одержимое графы ‘notes’ первого интерфейса - '{interf[0]['notes']}'")
print(interf[0].pop('notes'))
print(interf)
# g
interf[3]['status'] = 'down'
print(f"Четвертый интерфейс в состянии - {interf[3]}")


del interf[-3]
print(interf)
