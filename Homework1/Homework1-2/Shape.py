# Abstract Class
class Shape(object):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.__class__.__name__} ({self.x}, {self.y}, {self.z})'
