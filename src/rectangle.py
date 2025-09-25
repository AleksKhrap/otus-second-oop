from .figure import Figure


class Rectangle(Figure):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("The sides of the square should be positive")
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return (self.length + self.width) * 2
