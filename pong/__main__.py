"""
A module that begins the game
"""
import constants
import math
import random

from game.casting.cast import Cast
from game.casting.paddle import Paddle
from game.casting.actor import Actor
from game.casting.ball import Ball
from game.casting.score import Score

from game.scripting.play_sounds_action import PlaySoundsAction
from game.scripting.control_player1_action import ControlPlayer1Action
from game.scripting.control_player2_action import ControlPlayer2Action
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.game_over_action import GameOverAction

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
    paddle1 = Paddle(Point(10, constants.MAX_Y//2 - constants.PADDLE_HEIGHT), constants.RED)
    paddle2 = Paddle(Point(constants.MAX_X - 20, constants.MAX_Y//2 - constants.PADDLE_HEIGHT), constants.GREEN)

    angle_choices = [random.uniform(15,60), random.uniform(120,165), random.uniform(195, 240), random.uniform(300,345)]
    angle = random.choice(angle_choices)
    x = math.cos(math.radians(angle))
    y = math.sin(math.radians(angle))

    ball = Ball()
    ball.set_color(constants.WHITE)
    ball.set_position(Point(constants.MAX_X // 2, random.randrange(10, constants.MAX_Y - 10)))
    ball.set_radius(constants.BALL_RADIUS)
    vel = Point(x,y).scale(constants.BALL_SPEED)
    ball.set_velocity(vel)

    cast = Cast()
    cast.add_actor("paddles", paddle1)
    cast.add_actor("paddles", paddle2)
    cast.add_actor("ball", ball)

    score_left = Score()
    score_right = Score()
    cast.add_actor("scores", score_left)
    cast.add_actor("scores", score_right)

    keyboard_service = KeyboardService()
    video_service = VideoService()
    sound_service = SoundService(constants.ROOT_DIR)
    sound_service.add_sound("edges", "edges.wav")
    sound_service.add_sound("paddles", "paddles.wav")
    sound_service.add_sound("lost", "lost.wav")

    script = Script()
    handle_collisions_action = HandleCollisionsAction()
    script.add_action("input", ControlPlayer2Action(keyboard_service))
    script.add_action("input", ControlPlayer1Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", handle_collisions_action)
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("output", PlaySoundsAction(sound_service, handle_collisions_action))

    score_left.set_position(Point(constants.MAX_X // 2 - 30, 10))
    score_left.set_text("0")

    score_right.set_position(Point(constants.MAX_X // 2 + 30, 10))
    score_right.set_text("0")

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
