from Shape import Shape


class Circle(Shape):
    def __init__(self, x: int, y: int, z: int, radius=1):
        super().__init__(x, y, z)
        self.radius = radius

    def __str__(self):
        return f'{self.__class__.__name__} ({self.x}, {self.y}, {self.z}) Radius: {self.radius}'
