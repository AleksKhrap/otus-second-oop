import pytest
import math
from src.circle import Circle


@pytest.mark.circle
class TestCircle:

    def test_valid_circle(self):
        circle = Circle(5)
        assert circle.radius == 5

    @pytest.mark.parametrize('radius',
                             [-1, 0],
                             ids=('Negative', 'Zero'))
    def test_invalid_circle(self, radius):
        with pytest.raises(ValueError):
            Circle(radius)

    @pytest.mark.parametrize('radius, expected_area, expected_perimeter',
                             [(1, math.pi, 2 * math.pi),
                              (10, 100 * math.pi, 20 * math.pi),
                              (0.5, 0.25 * math.pi, math.pi)],
                             ids=('Positive 1', 'Positive 2', 'Float'))
    def test_circle_parameters(self, radius, expected_area, expected_perimeter):
        circle = Circle(radius)
        assert abs(circle.area - expected_area) < 1e-10
        assert abs(circle.perimeter - expected_perimeter) < 1e-10
