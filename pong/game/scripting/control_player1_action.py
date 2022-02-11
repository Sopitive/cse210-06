"""
A module that contains the Control Player 1 Action class
"""
from game.scripting.control_actors_action import ControlActorsAction

class ControlPlayer1Action(ControlActorsAction):
    """ Defines controls that allow player 1 to move. """
    def is_control_down(self, control):
        """ Checks if the keys w or s are pressed. 
        
        Args:
            control:
        
        """
        controls = {
            "up": "w",
            "down":"s"
        }
        return self._keyboard_service.is_key_down(controls[control])

    def get_paddle(self, cast):
        return cast.get_actors("paddles")[0]