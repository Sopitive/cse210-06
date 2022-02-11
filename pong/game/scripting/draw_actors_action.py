"""
A module that contains the Draw Actors Action class
"""
from game.scripting.action import Action
import constants


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
            video_service (VideoService): An instance of VideoService.
            sound_service (SoundService): An instance of SoundService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            messages (string): message dispayed at end of game.
            script (Script): The script of Actions in the game.
        """
        self._video_service.draw_rectangle(constants.MAX_X //2-1,0,2, constants.MAX_Y, constants.WHITE)
        for paddle in cast.get_actors("paddles"):
            pos = paddle.get_position()
            self._video_service.draw_rectangle(pos.get_x(), pos.get_y(), paddle.width, paddle.height, paddle.get_color())
        ball = cast.get_first_actor("ball")
        self._video_service.draw_circle(ball.get_position(), ball.get_radius(), ball.get_color())
        
        messages = cast.get_actors("message")
        self._video_service.clear_buffer()

        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
