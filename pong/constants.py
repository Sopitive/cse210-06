""" 
A module for constants used by the game 
"""


from game.shared.color import Color
import os


COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 8
FONT_SIZE = 15
CAPTION = "paddle"
#paddle_LENGTH = 8
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))