"""
A module that contains the Handle Collisions Action Class
"""
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the paddle collides
    with the other paddle segments, or the paddle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.winner = 0
    
    def get_game_over(self):
        """ Gets whether or not the game is over"""
        return self._is_game_over

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_paddle_collision(self, first, second):
        """ Handles whether the paddle has collided with another paddle. 
        
        Args:
            first (Cast): The first paddle.
            second (Cast): The second paddle.
        
        """

        first_head = first.get_segments()[0]
        first_segments = first.get_segments()[1:]
        second_segments = second.get_segments()

        for segment in first_segments + second_segments:
            if first_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                return True
        return False
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the paddle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        paddle1, paddle2 = cast.get_actors("paddles")
        if self._handle_paddle_collision(paddle1, paddle2):
            #paddle 1 lost
            self.winner = 2
        elif self._handle_paddle_collision(paddle2, paddle1):
            # paddle 2 lost
            self.winner = 1

        # paddle = cast.get_first_actor("paddles")
        # head = paddle.get_segments()[0]
        # segments = paddle.get_segments()[1:]
        
        # for segment in segments:
        #     if head.get_position().equals(segment.get_position()):
        #         self._is_game_over = True
        
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
            message.set_text(f"Game Over! paddle {self.winner} won!")
            message.set_position(position)
            message.set_color(constants.RED)
            message.set_font_size(40)
            cast.add_actor("message", message)

            

            paddles = cast.get_actors("paddles")
            for paddle in paddles:
                paddle.set_color(constants.WHITE)
                segments = paddle.get_segments()
                for segment in segments:
                    segment.set_color(constants.WHITE)

            # for segment in segments:
            #     segment.set_color(constants.WHITE)
    
    