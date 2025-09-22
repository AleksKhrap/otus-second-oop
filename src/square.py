from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("The side of the square should be positive")
        super().__init__(side, side)

    @property
    def side(self):
        return self.length
