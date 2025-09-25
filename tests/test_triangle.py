import pytest
import math
from src.triangle import Triangle


@pytest.mark.triangle
class TestTriangle:

    @pytest.mark.parametrize('side_a, side_b, side_c, perimeter',
                             [(1, 2, 2, 5),
                              (5.5, 6.5, 7.5, 19.5)],
                             ids=('Integer', 'Float'))
    def test_valid_triangle(self, side_a, side_b, side_c, perimeter):
        triangle = Triangle(side_a, side_b, side_c)
        assert triangle.perimeter == perimeter
        assert triangle.area > 0

    @pytest.mark.parametrize('side_a, side_b, side_c',
                             [(-1, 2, 3),
                              (0, 2, 2)],
                             ids=('Negative side', 'Zero side'))
    def test_invalid_triangle(self, side_a, side_b, side_c):
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0
        assert triangle.area == expected_area

    def test_equilateral_triangle(self):
        triangle = Triangle(5, 5, 5)
        expected_area = (math.sqrt(3) / 4) * 25
        assert abs(triangle.area - expected_area) < 1e-10
