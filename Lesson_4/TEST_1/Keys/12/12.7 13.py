"""
Вы находитесь в квест-комнате по мультфильму WALL-E! Вы нашли записку:
"In a distant, but not so unrealistic, future where mankind has abandoned earth because it has become covered with trash from products sold by the powerful multi-national Buy N Large corporation, WALLE, a garbage collecting robot has been left to clean up the mess. Mesmerized with trinkets of Earth's history and show tunes, WALLE is alone on Earth except for a sprightly pet cockroach. One day, EVE, a sleek (and dangerous) reconnaissance robot, is sent to Earth to  find proof that life is once again sustainable."

Чтобы выбраться из комнаты, необходимо выполнить следующие шаги:
- вывести на экран длину текста в обнаруженной записке
- вывести на экран весь текст в нижнем регистре
- заменить все вхождения некорректно написанного имени WALLE на его правильную форму WALL-E.
- подсчитать, сколько раз в тексте было использовано слово Earth.
"""

text = "In a distant, but not so unrealistic, future where mankind has abandoned " \
       "earth because it has become covered with trash from products sold by the " \
       "powerful multi-national Buy N Large corporation, WALLE, a garbage collecting " \
       "robot has been left to clean up the mess. Mesmerized with trinkets of Earth's " \
       "history and show tunes, WALLE is alone on Earth except for a sprightly pet cockroach. " \
       "One day, EVE, a sleek (and dangerous) reconnaissance robot, is sent to Earth to  " \
       "find proof that life is once again sustainable."

print('Длина текста: ', len(text))
#text = text.lower()
print('Текст в нижнем регистре: ', text.lower())
text = text.replace('WALLE', 'WALL-E')
print('Текст после замены имени: ', text)
print('Количество слова Earth: ', text.count('Earth'))


