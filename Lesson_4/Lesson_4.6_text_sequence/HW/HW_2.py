# Сколько слов заканчивается на букву "я", "й"

s = 'Lorem Ipsum - это текст - "рыба", часто используемый в печати и вэб - дизайне. ' \
    'Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. ' \
    'В то время некий безымянный печатник создал большую коллекцию ' \
    'размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. ' \
    'Lorem Ipsum не только успешно пережил без ' \
    'заметных изменений пять веков, но и перешагнул в электронный дизайн. '

s = s.replace(',', '')
s = s.replace(';', '')
s = s.replace(':', '')
s = s.replace('.', '')
s = s.replace('"', '')
s = s.replace("'", '')
s = s.replace("-", '')
# s = s.replace(" ", '')

l = s.split()
print(l)

print(s)

letter = "й"

count = 0
for i in l:
    w_1 = i.count(letter, -1)
    count += w_1
    if w_1 == 1:
        print(i)
print(f"Количество слов, заканчивающихся на букву {letter} - {count}")

