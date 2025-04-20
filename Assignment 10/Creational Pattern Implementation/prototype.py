import copy

class Shape:
    def clone(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return f"Circle(Radius: {self.radius})"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return f"Rectangle(Width: {self.width}, Height: {self.height})"
