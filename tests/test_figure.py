import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.base
class TestFigure:

    def test_add_area_with_valid_figure(self):
        triangle = Triangle(3, 4, 5)
        square = Square(2)

        result = triangle.add_area(square)
        expected = triangle.area + square.area

        assert result == expected

    def test_add_area_with_invalid_object(self):
        triangle = Triangle(3, 4, 5)

        with pytest.raises(ValueError, match="Not a figure"):
            triangle.add_area("Not a figure")

    @pytest.mark.parametrize("figure_class",
                             [lambda: Circle(2),
                              lambda: Rectangle(3, 4),
                              lambda: Square(5),
                              lambda: Triangle(3, 4, 5)],
                             ids=('Circle', 'Rectangle', 'Square', 'Triangle'))
    def test_all_figures_implement_required_methods(self, figure_class):
        figure = figure_class()

        assert hasattr(figure, 'area')
        assert hasattr(figure, 'perimeter')
        assert isinstance(figure.area, (int, float))
        assert isinstance(figure.perimeter, (int, float))
        assert figure.area > 0
        assert figure.perimeter > 0
