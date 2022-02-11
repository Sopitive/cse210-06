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
BALL_SPEED = 5
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))