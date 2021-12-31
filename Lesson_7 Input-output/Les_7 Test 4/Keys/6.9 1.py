"""
Напишите программу, которая спрашивала бы у пользователя его имя, пол, возраст и место жительства,
а затем выводила бы полученную информацию на экран в следующем формате:
This is [name].
He (she) is [age] years old.
He (she) lives in [city].
"""

name = input('Enter your name: ')
sex = input('Enter your sex (m/f): ')
age = input('Enter your age: ')
address = input('Enter your address: ')

print()
print(f'This is {name}')
print(f'{"He" if sex=="m" else "She"} is {age} years old.')
print(f'{"He" if sex=="m" else "She"} lives in {address}.')
