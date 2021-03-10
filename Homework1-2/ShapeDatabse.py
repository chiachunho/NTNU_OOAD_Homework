from typing import List
from operator import attrgetter
from Shape import Shape


class ShapeDatabase(object):
    def __init__(self):
        self.__shape_list: List[Shape] = []

    def __iter__(self):
        index = 0
        while index < len(self.__shape_list):
            yield self.__shape_list[index]
            index += 1

    def __getitem__(self, item):
        return self.__shape_list[item]

    def __len__(self):
        return len(self.__shape_list)

    def sort(self):
        self.__shape_list.sort(key=attrgetter('z', 'x', 'y'))

    def append(self, shape: Shape):
        self.__shape_list.append(shape)

    def clear(self):
        self.__shape_list.clear()
