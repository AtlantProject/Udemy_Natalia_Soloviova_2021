"""
Написать программу, проверяющую, начинается ли заданная строка с заданного символа, с помощью lambda-функции.
"""
starts_with = lambda s: True if s.startswith('P') else False

print(starts_with('Python!'))
print(starts_with('Java'))

# проверяемая буква также передается как параметр

def starts_with(letter):
    return lambda s: True if s.startswith(letter) else False

res1 = starts_with('A')
print(res1('Antony'))
print(res1('AMax'))

res2 = starts_with('B')
print(res2('Antony'))
print(res2('BMax'))