"""
A module that contains the Handle Collisions Action Class
"""
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import pyray
import pyray


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
            self._handle_ball_collision(cast)
            self._handle_game_over(cast)

    def _handle_ball_collision(self, cast):
        """ Handles whether the ball has collided with the wall or paddle. 

        Args:
            first (Cast): The first paddle.
            second (Cast): The second paddle.

        """
        ball = cast.get_first_actor("ball")
        left, right = cast.get_actors("paddles")

        hit = False 
        if pyray.check_collision_circle_rec(ball.get_position().to_tuple(), ball.get_radius(), left.get_rectangle()):
            normal = Point(1, 0)
            hit = True
        if pyray.check_collision_circle_rec(ball.get_position().to_tuple(), ball.get_radius(), right.get_rectangle()):
            normal = Point(-1,0)
            hit = True
        if hit:
            velocity = ball.get_velocity()
            velocity = velocity.reflect(normal)
            ball.set_velocity(velocity)
        

    def _handle_screen_collision(self, cast):
        """Sets the game over flag if the paddles collides with the top and bottom of the screen.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        paddle1, paddle2 = cast.get_actors("paddles")
        if self._handle_screen_collision(paddle1, paddle2):
            # paddle 1 lost
            self.winner = 2
        elif self._handle_paddle_collision(paddle2, paddle1):
            # paddle 2 lost
            self.winner = 1

        # paddle = cast.get_first_actor("paddles")
        # head = paddle.get_segments()[0]
        # segments = paddle.get_segments()[1:]

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
                # segments = paddle.get_segments()
                for paddle in paddles:
                    paddle.set_color(constants.WHITE)

            # for segment in segments:
            #     segment.set_color(constants.WHITE)


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
                # segments = paddle.get_segments()
                for paddle in paddles:
                    paddle.set_color(constants.WHITE)


