'''
Тема 7: “Множества”
1.	Подсчитайте количество уникальных символов в высказывании
Уильяма Шекспира: “All the world’s a stage, and all the men and
women merely players. They have their exits and their entrances;
and one man in his time plays many parts.” (одна и та же буква в
разных регистрах считается как один символ). Согласно таблице ASCII
какой из символов данного высказывания является минимальным, а какой
максимальным?

'''

s = 'All the world"s a stage, and all the men and women merely players. ' \
    'They have their exits and their entrances; and one man in his ' \
    'time plays many parts.'
s = s.lower()
print("длина первоначальной строки", len(s))

s_set = set(s)
print("rjkbxtcdnj", len(s_set))
print("s_set", s_set)

sorted(s_set)
print(s_set)
print("min", min(s_set), "_", max(s_set), "__")