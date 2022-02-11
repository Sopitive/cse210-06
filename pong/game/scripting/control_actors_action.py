"""
A module that contains the Control Actors Action class
"""
import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """paddle
    An input action that controls the paddle.

    The responsibility of ControlActorsAction is to get the direction and move the paddle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        # self._direction = Point(0, constants.CELL_SIZE)

    def is_control_down(self, control):
        """
        Checks to see if a control is being pushed. It will be overriden by other classes.
        """
        raise NotImplementedError

    def get_paddle(self, cast):
        """
        Gets the paddle from the cast. It will be overriden by other classes.
        """
        raise NotImplementedError

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        direction = Point(0, 0)

        # up
        if self.is_control_down("up"):
            # self._direction = Point(0, -constants.CELL_SIZE)
            direction = Point(0, -constants.CELL_SIZE)

        # down
        if self.is_control_down("down"):
            # self._direction = Point(0, constants.CELL_SIZE)
            direction = Point(0, constants.CELL_SIZE)

        paddle = self.get_paddle(cast)
        paddle.set_velocity(direction)
        # paddle.turn_head(self._direction)
