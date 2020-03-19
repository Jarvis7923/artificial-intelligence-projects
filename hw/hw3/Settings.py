"""

Defined the type of the puzzle and per-established order as enum. Global settings for different test cases.

author: shang wang 
student id: 1277417
email: swang27@tufts.edu

"""

from enum import Enum

class puzzle_type(Enum):
    """
    types of puzzeles
        easy_puzzle
        evil_puzzle
    """
    easy_puzzle = 0
    evil_puzzle = 1

class order_type(Enum):
    """
    pre-established order
        row_first
        random
    """
    row_first = 0
    random = 1

SETTINGS = {}
PUZZLE = "puzzle"
ORDER = "order"
ANIME = "anime"
INTERVAL = "interval"

SETTINGS[PUZZLE] = puzzle_type.easy_puzzle 
SETTINGS[ORDER] = order_type.row_first
SETTINGS[ANIME] = True
SETTINGS[INTERVAL] = 0.0

