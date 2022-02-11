"""
A module that contains the Control Player 2 Action class
"""
from game.scripting.control_actors_action import ControlActorsAction

class ControlPlayer2Action(ControlActorsAction):
    """ Defines controls that allow player 2 to move. """
    def is_control_down(self, control):
        """ Checks if i or k is pressed.

        Args:
            control:

        """
        controls = {
            "up": "i",
            "down":"k"
        }
        return self._keyboard_service.is_key_down(controls[control])

    def get_paddle(self, cast):
        """
        Gets the paddle that's being controlled by these controls
        """
        return cast.get_actors("paddles")[1]