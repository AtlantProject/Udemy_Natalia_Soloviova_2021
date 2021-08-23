"""
Марина, Женя и Света занимаются рисованием, а Костя, Женя и Илья - дополнительно посещают уроки музыки.
Определите, сколько человек занимается только одним видом искусства и выведите список их имен.
Ученик, занимающийся в обоих кружках, решил бросить занятия рисованием.
Произведите соответствующие изменения.
"""

drawing = {'Marina', 'Zhenya', 'Sveta'}
music = {'Kostya', 'Zhenya', 'Ilya'}

only_one_hobby = drawing.symmetric_difference(music)
print('Only one hobby: ', only_one_hobby)

both_hobbies = drawing.intersection(music)
print('Both hobbies: ', both_hobbies)

drawing = drawing - both_hobbies
print('Drawing: ', drawing)
