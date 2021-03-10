from Shape import Shape


class Triangle(Shape):
    def __init__(self, x: int, y: int, z: int, side_length=1):
        super().__init__(x, y, z)
        self.side_length = side_length

    def __str__(self):
        return f'{self.__class__.__name__} ({self.x}, {self.y}, {self.z}) Side Length: {self.side_length}'
