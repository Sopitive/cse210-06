"""
A module that contains the handel to end the game
"""
from operator import truediv
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.handle_collisions_action import Action
import pyray
import pyray


class GameOverAction(Action):
    """
    If the match point (11) has been reached by the left or right side then the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, handle_collisions_action):
        """Constructs a new HandleCollisionsAction."""
        #the points needed to win the game, end game.
        self._handle_collisions_action = handle_collisions_action


    def execute(self, cast, script):
        """Shows the 'game over' message and turns the paddles white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1, score2 = cast.get_actors("scores")
        winner = 0
        if score1.get_points() == constants.WINNING_SCORE:
            winner = 1
        if score2.get_points() == constants.WINNING_SCORE:
            winner = 2

        if winner:
            self._handle_collisions_action.set_is_game_over(True)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"Game Over! Paddle {winner} won!")
            message.set_position(position)
            message.set_color(constants.RED)
            message.set_font_size(40)
            cast.add_actor("message", message)

            paddles = cast.get_actors("paddles")
            for paddle in paddles:
                paddle.set_color(constants.BLACK)
