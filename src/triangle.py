from .figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if not self._is_valid_triangle(side_a, side_b, side_c):
            raise ValueError("A triangle with such sides cannot exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @staticmethod
    def _is_valid_triangle(a, b, c):
        return (a + b > c) and (a + c > b) and (b + c > a) and all(x > 0 for x in [a, b, c])

    @property
    def area(self):
        s = self.perimeter / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
