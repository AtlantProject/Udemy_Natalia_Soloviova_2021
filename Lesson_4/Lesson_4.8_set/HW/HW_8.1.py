# HW_8.1

history = {'Kostya', 'Masha', 'Danila', 'Ivan', 'Egor'}
biology = {'Sveta', 'Ivan', 'Sergei', 'Marina', 'Kostya', 'Masha', 'Anton'}
sport = {'Anton', 'Nikolai'}

history_and_biology = history.intersection(biology)
print(f'History and biology: {history_and_biology} pupils.')

all_discipline = history.intersection(biology, sport)
print(f'All discipline: {all_discipline} pupils.')

botanik_and_spormen = biology.intersection(sport)
print(f'Botanik and spormen: {botanik_and_spormen} pupils.')

pupils = history | biology | sport
pupils_len = len(pupils)
print(f'In dop. exersize {pupils_len} pupils. There are: {sorted(pupils)}.')