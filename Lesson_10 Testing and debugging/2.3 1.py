"""
Определить функцию add_underscores(), которая принимает в качестве аргумента одно слово
и возвращает новую строку, содержащую копию слова, в которой каждый символ окружен подчеркиванием.
Например, add_underscores("python") должен вернуть _p_y_t_h_o_n_.
"""


def add_underscores(word):
    # print(f'DEBUG - {word}')
    new_word = "_"
    for char in word:
        # print(f'DEBUG - {char}')
        new_word += char + "_"
        # print(f'DEBUG - {new_word}')
    # print(f'DEBUG - {new_word}')
    return new_word


phrase = "hello"
print(add_underscores(phrase))

phrase = "python"
print(add_underscores(phrase))
