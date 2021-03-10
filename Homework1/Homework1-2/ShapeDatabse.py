from typing import List
from operator import attrgetter
from Shape import Shape


# Class alike list to store Shape-based Class objects
class ShapeDatabase(object):
    # constructor
    def __init__(self):
        self.__shape_list: List[Shape] = []

    # iterator
    def __iter__(self):
        index = 0
        while index < len(self.__shape_list):
            yield self.__shape_list[index]
            index += 1

    # getitem by index
    def __getitem__(self, item):
        return self.__shape_list[item]

    # get list length
    def __len__(self):
        return len(self.__shape_list)

    # sort list of shapes by z-value of shape
    def sort(self):
        self.__shape_list.sort(key=attrgetter('z', 'x', 'y'))

    # append shape to list
    def append(self, shape: Shape):
        self.__shape_list.append(shape)

    # clear list
    def clear(self):
        self.__shape_list.clear()
