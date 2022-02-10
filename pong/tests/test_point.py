"""Tests for the Point class"""
from game.shared.point import Point

class Other():
    """class to create "other" argument to test equals() and add() methods"""
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

def test_point_equals_method():
    """Test equals() method in Point class"""
    point = Point(5,5)
    other = Other(5,5)

    assert point.equals(other)

def test_point_add_method():
    """Test add() method in Point class"""
    other = Other(5,5)
    point = Point(5,5).add(other)
    assert point._x == 10 and point._y == 10

def test_point_reverse_method():
    """Tests reverse() method in the point class"""
    point = Point(5,5).reverse()
    assert point._x == -5 and point._y == -5

def test_point_scale_method():
    """Test scale() method in the point class"""
    point = Point(5,5).scale(5)
    assert point._x == 25 and point._y == 25