"""
Abstract class 'Array'
"""
from abc import ABC, abstractmethod


class Array(ABC):
    def __init__(self, *args):
        self.data = args

    @abstractmethod
    def plus(self, arr):
        pass

    @abstractmethod
    def edit_elem(self):
        pass


__author__ = 'Natalia S.'
if __name__ == "Array":
    print(f'Module {__name__!r} (author: {__author__}) was imported.')