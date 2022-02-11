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

        Args:
        
        """
        super().__init__()
        self.set_color(color)
        self.set_position(starting_point)
        self.set_text("8")
        self.width = 5
        self.height = 100

    def get_rectangle(self):
        return (self._position.get_x(), self._position.get_y(), self.width, self.height)

    def draw_paddle(self, paddle_size):
        """ 
        Draws the paddle 


        """
    