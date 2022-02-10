"""A module that contains the Ball class"""

import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Ball(Actor):
    """A ball that bounces. 
    
    The responsibility of Ball is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """