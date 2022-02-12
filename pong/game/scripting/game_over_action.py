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

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._is_round_over = False
        self._paddle_scorer = "left"
        self._winner = 0
        self._edges_collision = False
        self._paddles_collision = False
        #the points needed to win the game, end game.
        self.match_point = 2 #it will be 10 but for testing use 2.

    def _handle_round_over(self, cast):
        score_left, score_right = cast.get_actors("scores")
        if score_left or score_right == self.match_point:
            self._is_game_over = True 
        else:
            self._is_round_over = False


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the paddles white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"Game Over! Paddle {self._winner} won!")
            message.set_position(position)
            message.set_color(constants.RED)
            message.set_font_size(40)
            cast.add_actor("message", message)

            paddles = cast.get_actors("paddles")
            for paddle in paddles:
                paddle.set_color(constants.WHITE)
                for paddle in paddles:
                    paddle.set_color(constants.WHITE)



    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the paddles white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"Game Over! Paddle {self.winner} won!")
            message.set_position(position)
            message.set_color(constants.RED)
            message.set_font_size(40)
            cast.add_actor("message", message)

            paddles = cast.get_actors("paddles")
            for paddle in paddles:
                paddle.set_color(constants.WHITE)
                # segments = paddle.get_segments()
                for paddle in paddles:
                    paddle.set_color(constants.WHITE)

    
    def get_paddle_collided(self):
        return self._paddles_collision
    
    def get_edges_collision(self): 
        return self._edges_collision

    def get_lost_round(self): 
        return self._lost_round


