"""
A module for running tests on the players' actions for our paddle game.
"""
from ctypes import cast
import pytest
import constants
from game.shared.point import Point
from game.scripting.control_player1_action import ControlPlayer1Action
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.script import Script
from game.casting.cast import Cast
from game.casting.paddle import Paddle
from game.scripting.action import Action
from game.services.keyboard_service import KeyboardService
from game.casting.actor import Actor


class CustomKeyboardService:
    "A class used for forced key entry (rather than monkeypatch)"
    def __init__(self, key):
        self.key = key

    def is_key_down(self, key):
        """
        tests to see if key is being pushed and gives the value of key
        """
        return self.key == key

def test_control_player1_actions():
    "This test asserts that the paddle moved up one space when 'w' was pushed"
    cast = Cast()
    paddle = Paddle(Point(0, 0), constants.RED)
    cast.add_actor("paddles", paddle)
    action = ControlPlayer1Action(CustomKeyboardService("w"))
    action.execute(cast, None)
    paddle = action.get_paddle(cast)
    assert paddle.get_velocity().equals(Point(0, -constants.PADDLE_SPEED))

    action = ControlPlayer1Action(CustomKeyboardService("s"))
    action.execute(cast, None)
    paddle = action.get_paddle(cast)
    assert paddle.get_velocity().equals(Point(0, constants.PADDLE_SPEED))

def test_action():
    """This test asserts the execute function of the Action class that raises a NotImplementedError"""
    cast = Cast()
    script = Script()
    action = Action()
    with pytest.raises(NotImplementedError):
        action.execute(cast, script)

def test_script():
    """This test asserts add_action, get_action, and remove_action methods work in the Script class"""
    script = Script()
    action = Action()
    script.add_action("action", action)
    assert len(script.get_actions("action")) == 1
    script.remove_action("action", action)
    assert len(script.get_actions("action")) == 0

def test_control_actors_action():
    "tests the functions within the ControlActorsAction class"
    keyboard_service = KeyboardService()
    cast = Cast()
    control_actors_action = ControlActorsAction(keyboard_service)
    with pytest.raises(NotImplementedError):
        control_actors_action.is_control_down('w')
    with pytest.raises(NotImplementedError):
        control_actors_action.get_paddle(cast)

def test_cast_actors():
    """ tests the methods of getting all actors, getting first actor and removing actor within the Cast class"""
    cast = Cast()
    actor = Actor()
    actor.set_text("TEST")
    cast.add_actor("group", actor)
    first_actor = cast.get_first_actor("group")
    assert first_actor.get_text() == "TEST"
    assert len(cast.get_all_actors()) == 1
    cast.remove_actor("group", actor)
    assert len(cast.get_all_actors()) == 0
