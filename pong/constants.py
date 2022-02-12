"""
A module for constants used by the game
"""

from game.shared.color import Color
import os


COLUMNS = 40
ROWS = 20
CELL_SIZE = 8
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 45
FONT_SIZE = 15
CAPTION = "paddle"

WINNING_SCORE = 11

BALL_SPEED = 10
BALL_RADIUS = 6

PADDLE_WIDTH = 5
PADDLE_HEIGHT = 50
PADDLE_SPEED = 10

WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLACK = Color(0, 0, 0)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))