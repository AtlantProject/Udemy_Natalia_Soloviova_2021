
'''
def func(a, L=[]):
    L.append(a)
    print(L)
    return L

func(1)
func(2)
func(3)
func(4)
func(5)
'''


def func(a, L=None):
    if L in None:
        L = []
    L.append(a)
    print(L)
    return L


func(1)
