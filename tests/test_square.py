import pytest
from src.square import Square
from src.rectangle import Rectangle


@pytest.mark.square
class TestSquare:

    @pytest.mark.parametrize('side, expected_area, expected_perimeter',
                             [(1, 1, 4),
                              (10, 100, 40),
                              (2.5, 6.25, 10.0)],
                             ids=('Integer 1', 'Integer 2', 'Float'))
    def test_valid_square(self, side, expected_area, expected_perimeter):
        square = Square(side)
        assert square.area == expected_area
        assert square.perimeter == expected_perimeter

    @pytest.mark.parametrize('side_a',
                             [-1, 0],
                             ids=('Negative side', 'Zero side'))
    def test_invalid_square(self, side_a):
        with pytest.raises(ValueError):
            Square(side_a)

    def test_square_inheritance(self):
        square = Square(5)
        assert isinstance(square, Rectangle)
        assert square.length == 5
        assert square.width == 5
