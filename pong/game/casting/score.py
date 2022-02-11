"""
A module that contains the Score class
"""
from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost.

    The responsibility of Score is to keep track of the points the player has earned by winning each round.
    It contains methods for adding and getting points. Client should use get_text() to get a string
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"{self._points}")

    def get_points(self):
        """
        Returns the points
        """
        return self._points