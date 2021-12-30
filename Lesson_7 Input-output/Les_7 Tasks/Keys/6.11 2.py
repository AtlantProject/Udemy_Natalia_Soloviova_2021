"""
Напишите программу, которая предлагает пользователю решить пример:
4*100-54. В случае, если пользователь ошибается, программа должна вывести соответствующее сообщение
и правильный ответ. А в случае, если пользователь прав, - поздравить его с правильным ответом.
"""
print('4*100 - 54')
user_answ = int(input('Your answer: '))
correct_answ = 4*100 - 54

if user_answ == correct_answ:
    print("Congratulations! That's a correct answer! ")
else:
    print("Unfortunately, that's a wrong answer :-(")
    print(f"The correct answer is {correct_answ}")

