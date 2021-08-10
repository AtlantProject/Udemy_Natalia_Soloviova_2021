# В кружке по борьбе занимаются 8 человек: Круглов Алексей, Ворожейкин Борик, Митин Сергей, Алешин Сергей, Кутиков
# Владимир, Круглов Денис, Бочкин Иван, Мечников Алексей. Выведите список учеников в алф. порядке.
# Подсчитайте, сколько в группе Сергеев, Алексеев и Денисов? Есть ли в группе однофамильцы?

pupils = ["Круглов Алексей",
          "Ворожейкин Борис",
          "Митин Сергей",
          "Алешин Сергей",
          "Кутиков Владимир",
          "Круглов Денис",
          "Бочкин Иван",
          "Мечников Алексей"]

print(pupils)

pupils.sort()
print(pupils)

print(len(pupils))

print(f"В группе Сергеев - {pupils.count('Сергей')} человек" )
print(f"В группе Сергеев - {pupils.count('Денис')} человек" )
print(f"В группе Сергеев - {pupils.count('Алексей')} человек" )

pupils.remove("Бочкин Иван")
print(pupils)

pupils.append("Фомин Петр")
pupils.append("Краснов Дмитрий")

print(pupils)

pupils.sort()
print(pupils)


names = [fullname.split(" ")[1] for fullname in pupils]
print(names)

print(names.count("Алексей"))

# Если список большой и/или надо посчитать много элементов, то лучше использовать словарь:
#
# Построение ручками:

name_counts = {}
for name in names:
    if name not in name_counts:
        name_counts[name] = 1
    else:
        name_counts[name] += 1

print(name_counts)

# С помощью Counter

import collections

name_counts = collections.Counter(names)
print(name_counts)

# Вариант какой-то

people = ['Круглов Алексей', 'Ворожейкин Борик', 'Митин Сергей', 'Алешин Сергей', 'Кутиков Владимир', 'Круглов Денис', 'Бочкин Иван', 'Мечников Алексей']
choices = ['Сергей', 'Алексей', 'Денис']

names = [full_name.split()[1] for full_name in people]
result = {name: names.count(name) for name in choices}

print(result)

