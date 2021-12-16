"""
Напишите функцию, ведущую подсчет количества посещений указанного города.
Функция должна принимать в качестве аргумента название города и возвращать
некоторую внутреннюю функцию, которая каждый раз при ее вызове будет увеличивать
счетчик посещений на 1. При решении задачи используйте нелокальную область видимости.
"""
def foo(city):
    s = 0

    def incr():
        nonlocal s
        s += 1
        print(city, s)

    return incr

res1 = foo('Moscow')
res1()
res1()

res2 = foo('NY')
res2()

res1()
