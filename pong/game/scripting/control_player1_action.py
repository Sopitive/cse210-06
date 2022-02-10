"""
A module that contains the Control Player 1 Action class
"""
from game.scripting.control_actors_action import ControlActorsAction

class ControlPlayer1Action(ControlActorsAction):
    def is_control_down(self, control):
        controls = {
            "left": "a",
            "right": "d",
            "up": "w",
            "down":"s"
        }
        return self._keyboard_service.is_key_down(controls[control])

    def get_paddle(self, cast):
        return cast.get_actors("paddles")[0]