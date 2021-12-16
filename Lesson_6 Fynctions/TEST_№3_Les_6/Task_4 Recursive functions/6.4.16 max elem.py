"""
Написать рекурсивную функцию поиска максимального элемента числовой последовательности.
"""
l = [3, 6, 4]

# TODO: Не понял как работает этот код(((

def foo(l):
    if len(l) > 1:
        print(f'len(l) = {len(l)}')
        print(f"l[0] = {l[0]}")
        # print(f"foo(l[1:]) = {foo(l[1:])}")
        print(f'max(l[0], foo(l[1:])) = {max(l[0], foo(l[1:]))}')
        return max(l[0], foo(l[1:]))
    else:
        print(f'Иначе l[0] = {l[0]}')
        return l[0]

print(foo(l))