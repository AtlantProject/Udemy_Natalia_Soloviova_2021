"""
Class 'OrArray'
"""
from math import log
from Array import Array

class OrArray(Array):
    def plus(self, arr):
        res = set(self.data).union(set(arr.data))
        print(f'Plus (union):\n{self.data} + {arr.data} = {tuple(res)}')
        return tuple(res)

    def edit_elem(self):
        res = list(map(log, self.data))
        res = list(map(round, res, [2] * len(res)))
        print(f'Edit elements (log):\n{self.data}  ->  {res}')
        return res


__author__ = 'Natalia S.'
if __name__ == "OrArray":
    print(f'Module {__name__!r} (author: {__author__}) was imported.')