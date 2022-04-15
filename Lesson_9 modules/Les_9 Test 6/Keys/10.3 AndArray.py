"""
Class 'AndArray'
"""
from math import sqrt
from Array import Array


class AndArray(Array):
    def plus(self, arr):
        res = set(self.data).intersection(set(arr.data))
        print(f'Plus (intersection):\n{self.data} + {arr.data} = {tuple(res)}')
        return tuple(res)

    def edit_elem(self):
        res = list(map(sqrt, self.data))
        res = list(map(round, res, [2]*len(res)))
        print(f'Edit elements (sqrt):\n{self.data}  ->  {res}')
        return res


__author__ = 'Natalia S.'
if __name__ == "AndArray":
    print(f'Module {__name__!r} (author: {__author__}) was imported.')