'''
Тема 5: “Текстовые последовательности”
1.	Напишите программу, которая позволит выполнять проверку пароля на сложность в соответствии со следующими критериями:
a.	длина пароля не менее 5 символов
b.	содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре: A-Z, a-z
c.	содержит цифры от 0 до 9
d.	содержит хотя бы один из символов: @, #, %, &
'''
# Цифры от 0 до 9
# data = [i for i in range(0, 10)]
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data)

# Английский алфавит
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ABC = list(ABC)
print(ABC)
abc = 'abcdefghijklmnopqrstuvwxyz'
abc = list(abc)
print(abc)

# Символы @, #, %, &

symbols = ['@', '#', '%', '&']

# parol = input("Ведите пароль латинскими буквами - ")
parol = "0123456789abcABC@#%&"
analis_p = list(parol)
print(analis_p)

if len(parol) >= 5:
    print("В пароле больше 5 символов")
else:
    print("Пароль слишком короткийю введите новый пароль")

for i in ABC:
    if i in parol:
        print("В пароле есть заглавные буквы ABC")
    else:
        # print("Пароль должен включать заглавные буквы ABC")
        continue

for i in abc:
    if i in parol:
        print("В пароле есть строчные буквы abc")
    else:
        print("Пароль должен включать строчные буквы abc")


for i in symbols:
    if i in parol:
        print("Пароль содержит хотя бы один из символов: @, #, %, &")
    else:
        print("Пароль должен включать в себя хотя бы один из символов: @, #, %, &")
    break

'''
stop = True

while stop == True:
    if parol == 'exit':
        stop = False
    if len(analis_p) >= 5:
        print(f"Длина пароля {len(analis_p)} символов.")
    continue
    else    print("Введите более длинный пароль. Для выхода введите 'exit'")
        parol = input("Ведите пароль латинскими буквами - ")
# b.	содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре: A-Z, a-z

data = [i for i in range(0, 10)]
print(data)

for digit in data:
    print(digit)
    if digit in analis_p:
        print(f"Цифра {digit} имеется в пароле.")
'''

'''
2.	Вы находитесь в квест-комнате по мультфильму WALL-E! Вы нашли записку:
"In a distant, but not so unrealistic, future where mankind has abandoned earth because it has become covered 
with trash from products sold by the powerful multi-national Buy N Large corporation, WALLE, a garbage collecting 
robot has been left to clean up the mess. Mesmerized with trinkets of Earth's history and show tunes, WALLE is alone 
on Earth except for a sprightly pet cockroach. One day, EVE, a sleek (and dangerous) reconnaissance robot, is sent to 
Earth to  find proof that life is once again sustainable."
Чтобы выбраться из комнаты, необходимо выполнить следующие шаги:
a.	вывести на экран длину текста в обнаруженной записке
b.	вывести на экран весь текст в нижнем регистре
c.	заменить все вхождения некорректно написанного имени WALLE на его правильную форму WALL-E.
d.	подсчитать, сколько раз в тексте было использовано слово Earth. 
'''

text = "In a distant, but not so unrealistic, future where mankind has abandoned earth because it has become covered\n ' \
       'with trash from products sold by the powerful multi-national Buy N Large corporation, WALLE, a garbage collecting\n' \
       'robot has been left to clean up the mess. Mesmerized with trinkets of Earth's history and show tunes,\n " \
       "WALLE is alone on Earth except for a sprightly pet cockroach. One day, EVE, a sleek (and dangerous)\n " \
       "reconnaissance robot, is sent to Earth to  find proof that life is once again sustainable.\n"

# a.	вывести на экран длину текста в обнаруженной записке

print(f"Длина текста в обнаруженной записке {len(text)} символа.")

# b.	вывести на экран весь текст в нижнем регистре

text_small = text.lower()
print(text_small)

# c.	заменить все вхождения некорректно написанного имени
# WALLE на его правильную форму WALL-E.

# print(text.index("WALLE"))
# print(text[207::].index("WALLE"))

print(text.count("WALLE"))
print(text.find("WALLE"))
print(text.rfind("WALLE"))

change_start = text.find("WALLE")
change_end = text.rfind("WALLE")

# text[change_start] = "WALL-E"
# text[change_end] = "WALL-E"

text[206] = "WALL-E"
text[347] = "WALL-E"

print(text)

# d.	подсчитать, сколько раз в тексте было использовано слово Earth.

