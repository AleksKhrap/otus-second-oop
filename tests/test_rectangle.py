import pytest
from src.rectangle import Rectangle


@pytest.mark.rectangle
class TestRectangle:
    @pytest.mark.parametrize('length, width, expected_area, expected_perimeter',
                             [(2, 3, 6, 10),
                              (3.5, 4.5, 15.75, 16.0)],
                             ids=('Integer', 'Float'))
    def test_valid_rectangle(self, length, width, expected_area, expected_perimeter):
        rectangle = Rectangle(length, width)
        assert rectangle.area == expected_area
        assert rectangle.perimeter == expected_perimeter

    @pytest.mark.parametrize('side_a, side_b',
                             [(-1, 2),
                              (0, 2)],
                             ids=('Negative side', 'Zero side'))
    def test_invalid_rectangle(self, side_a, side_b):
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)
