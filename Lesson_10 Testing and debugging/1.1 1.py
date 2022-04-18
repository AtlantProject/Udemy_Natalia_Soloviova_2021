def foo1():
    a = 5
    b = 6
    c = a + b
    print("foo1 result is: %i" % c)
    return c


def foo2():
    d = foo1()**2
    print("foo2 result is: %i" % d)


print("Test program was started!")
res = foo1()
print("Result is: %i" % res)
foo2()
