'''
def recursion_sum(els):
    el, *tail = els
    return el + recursion_sum(tail)

print(recursion_sum([1, 2, 3]))
'''


def recursion_sum(arr):
    if not arr:
        return 0
    return arr[0] + recursion_sum(arr[1:])

print(recursion_sum([i for i in range(200)]))


def getSum(iterable):
    if not iterable:
        return 0  # End of recursion
    else:
        return iterable[0] + getSum(iterable[1:])  # Recursion step
