"""
A module that contains the Handle Collisions Action Class
"""
from operator import truediv
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import pyray
import random

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
        self._is_round_over = False
        self._is_delaying = False
        self._paddle_scorer = "left"
        self._winner = 0
        self._edges_collision = False
        self._paddles_collision = False
        self._lost_round = False
        self._round_timer_start = 3
        self._new_ball_y = constants.MAX_Y // 2
        self._round_timer = self._round_timer_start

    def set_is_game_over(self, value):
        """ tells the collision handler whether the game is over

        Args:
            value (bool) whether or not the game is over
        """
        self._is_game_over = value

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._handle_ball_collision(cast)
        self._handle_round_over(cast)
        self._handle_delay(cast)

    def _handle_ball_collision(self, cast):
        """ Handles whether the ball has collided with the wall or paddle.

        Args:
            first (Cast): The first paddle.
            second (Cast): The second paddle.

        """

        # Reference ball and paddles from cast
        ball = cast.get_first_actor("ball")

        hit = False

        ########
        # Paddle collison
        ########
        if not self._is_game_over:
            left, right = cast.get_actors("paddles")
            #Check collision between ball and left paddle
            if pyray.check_collision_circle_rec(ball.get_position().to_tuple(), ball.get_radius(), left.get_rectangle()):
                normal = Point(1, 0)
                hit = True
                self._paddles_collision = True
            #Check collision between ball and right paddle
            if pyray.check_collision_circle_rec(ball.get_position().to_tuple(), ball.get_radius(), right.get_rectangle()):
                normal = Point(-1,0)
                hit = True
                self._paddles_collision = True

        ########
        # Top and bottom collisons
        ########
        #Check collision between ball and top of the screen
        if ball.get_position().get_y() - ball.get_radius() <= 0:
            normal = Point(0, 1)
            hit = True
            self._edges_collision = True
        #Check collision between ball and bottom of the screen
        if ball.get_position().get_y() + ball.get_radius() >= constants.MAX_Y:
            normal = Point(0, -1)
            hit = True
            self._edges_collision = True

        ########
        # Left and right collisons
        ########
        if self._is_game_over:
            #Check collision between ball and left side of the screen
            if ball.get_position().get_x() - ball.get_radius() <= 0:
                normal = Point(1, 0)
                hit = True
                self._edges_collision = True
            #Check collision between ball and right side of the screen
            if ball.get_position().get_x() + ball.get_radius() >= constants.MAX_X:
                normal = Point(-1, 0)
                hit = True
                self._edges_collision = True

        #Changes direction if it hits paddle or top/bottom
        if hit:
            velocity = ball.get_velocity()
            velocity = velocity.reflect(normal)
            ball.set_velocity(velocity)
            ball.move_next()

        #Right player scores
        if ball.get_position().get_x() - ball.get_radius() <= 0:
            self._is_round_over = True
            self._paddle_scorer = "right"
            self._lost_round = True
        #Left player scores
        if ball.get_position().get_x() + ball.get_radius() >= constants.MAX_X:
            self._is_round_over = True
            self._paddle_scorer = "left"
            self._lost_round = True

    def _handle_delay(self, cast):
        """
        Delays the start of the round so the ball stays in the middle for 3 seconds in its new position.
        """
        if self._is_delaying and not self._is_game_over:
            self._round_timer -= pyray.get_frame_time()
            if self._round_timer <= 0:
                self._round_timer = self._round_timer_start
                self._is_delaying = False
            else:
                ball = cast.get_first_actor("ball")
                ball.set_position(Point(constants.MAX_X // 2, self._new_ball_y))

    def _handle_round_over(self, cast):
        """
        Adds to score and resets the Ball if it hits either side of the screen, starting a new round.
        """
        if self._is_round_over and not self._is_game_over:
            score_left, score_right = cast.get_actors("scores")
            if self._paddle_scorer == "left":
                score_left.add_points(1)
            if self._paddle_scorer == "right":
                score_right.add_points(1)
            self._is_round_over = False
            self._is_delaying = True
            self._new_ball_y = random.randrange(10, constants.MAX_Y - 10)


    def get_paddle_collided(self):
        """
        Lets the caller know the ball has collided with the paddle and resets the collision.
        """
        result = self._paddles_collision
        self._paddles_collision = False
        return result

    def get_edges_collision(self):
        """
        Lets the caller know the ball has collided with the edges and resets the collision.
        """
        result = self._edges_collision
        self._edges_collision = False
        return result

    def get_lost_round(self):
        """
        Lets the caller know that one of the players has lost the round and resets the indicator.
        """
        result = self._lost_round
        self._lost_round = False
        return result


