"""
Class 'Pair'
"""
from abc import ABC, abstractmethod


class Pair(ABC):
    def __init__(self, a, b):
        self.A = a
        self.B = b

    @abstractmethod
    def sum(self):
        pass

    @abstractmethod
    def minus(self):
        pass

    @abstractmethod
    def mult(self):
        pass

    @abstractmethod
    def div(self):
        pass


__author__ = 'Natalia S.'
if __name__ == "Pair":
    print(f'Module {__name__!r} (author: {__author__}) was imported.')