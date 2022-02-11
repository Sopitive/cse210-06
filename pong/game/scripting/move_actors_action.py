"""
A module that contains the Move Actors Action class
"""
from typing import List
from game.scripting.action import Action
from game.casting.actor import Actor
from game.casting.cast import Cast


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast: Cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        paddles = cast.get_actors("paddles")
        for paddle in paddles:
            paddle.move_next()
            # paddle.grow_tail(1)

        ball = cast.get_first_actor("ball")
        ball.move_next()