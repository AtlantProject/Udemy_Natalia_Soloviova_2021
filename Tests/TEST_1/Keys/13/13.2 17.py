"""
Подсчитайте количество уникальных символов в высказывании Уильяма Шекспира:
"All the world's a stage, and all the men and women merely players.
They have their exits and their entrances; and one man in his time plays many parts."
(одна и та же буква в разных регистрах считается как один символ).
Согласно таблице ASCII какой из символов данного высказывания является минимальным, а какой максимальным?
"""

s = "All the world's a stage, and all the men and women merely players. " \
    "They have their exits and their entrances; and one man in his time plays many parts."

s = s.lower()
str_set = set(s)
print(len(str_set))

print(min(str_set))
print(max(str_set))
