"""
A module that contains the Paddle class
"""
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Paddle(Actor):
    """
    A paddle that only moves up and down to hit a ball.

    The responsibility the paddle is to move itself up and down.

    Attributes:
        _points (int): The number of points.
    """
    def __init__(self, starting_point, color):
        """
        Constructs a new paddle.

        """
        super().__init__()
        self.set_color(color)
        self.set_position(starting_point)
        self.set_text("8")
        self.width = constants.PADDLE_WIDTH
        self.height = constants.PADDLE_HEIGHT

    def get_rectangle(self):
        """
        Gets the rectangle as a tuple, needed for using raylib functions.
        """
        return (self._position.get_x(), self._position.get_y(), self.width, self.height)
