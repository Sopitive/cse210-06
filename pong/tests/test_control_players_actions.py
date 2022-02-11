"""
A module for running tests on the players' actions for our paddle game.
"""
import pytest
import constants
from game.shared.point import Point
from game.scripting.control_player1_action import ControlPlayer1Action
from game.scripting.control_actors_action import ControlActorsAction
from game.casting.cast import Cast
from game.casting.paddle import Paddle


class CustomKeyboardService:
    "A class used for forced key entry (rather than monkeypatch)"
    def __init__(self, key):
        self.key = key

    def is_key_down(self, key):
        return self.key == key




def test_control_player1_actions():
    "This test asserts that the paddle moved up one space when 'w' was pushed"
    cast = Cast()
    paddle = Paddle(Point(0, 0), constants.RED)
    cast.add_actor("paddles", paddle)
    action = ControlPlayer1Action(CustomKeyboardService("w"))
    action.execute(cast, None)
    paddle = action.get_paddle(cast)
    assert paddle.get_velocity().equals(Point(0, -constants.CELL_SIZE))

