"""Tests for the Point class"""
from game.shared.point import Point

class Other():
    """class to create "other" argument to test equals() and add() methods"""
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def get_x(self):
        """
        Gets the value of x
        """
        return self._x
    def get_y(self):
        """
        Gets the value of y
        """
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

def test_tuple_reflect():
    """Test the to_tuple method in the Point class"""
    assert Point(1,1).to_tuple() == (1, 1)

def test_reflect_method():
    """Test the reflect() method in the Point class"""
    point = Point(-1,-1)
    normal = Point(0,1)
    assert point.reflect(normal).equals(Point(-1,1))