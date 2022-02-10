"""
A module that begins the game
"""
import constants

from game.casting.cast import Cast
from game.casting.paddle import Paddle
from game.casting.actor import Actor
from game.casting.ball import Ball

from game.scripting.play_sounds_action import PlaySoundsAction
from game.scripting.control_player1_action import ControlPlayer1Action
from game.scripting.control_player2_action import ControlPlayer2Action
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.sound_service import SoundService

from game.shared.color import Color
from game.shared.point import Point


def main():
    """
    The entry point of the program
    """
    paddle1 = paddle(Point(constants.MAX_X//4, constants.MAX_Y//2), constants.RED)
    paddle2 = paddle(Point(3*constants.MAX_X//4, constants.MAX_Y//2), constants.GREEN)

    cast = Cast()
    cast.add_actor("paddles", paddle1)
    cast.add_actor("paddles", paddle2) 
    cast.add_actor("scores", Score()) 

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    sound_service = SoundService(constants.ROOT_DIR)
    
    script = Script()
    script.add_action("input", ControlPlayer2Action(keyboard_service))
    script.add_action("input", ControlPlayer1Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("output", PlaySoundsAction(sound_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()