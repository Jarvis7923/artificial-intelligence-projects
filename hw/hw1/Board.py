"""
define the shared dictionary BOARD and its keys
"""

def clean_request(mode):
    """
    for testing different clean mode:

        mode 1: is SPOT, which means SPOT is true and GENERAL is false
        mode 2: is GENERAL, similarly
    """
    global BOARD
    if mode == 1:
        BOARD[SPOT] = True
        BOARD[GENERAL] = False
    elif mode == 2:
        BOARD[GENERAL] = True
        BOARD[SPOT] = False

BOARD = {}

BATTERY_LEVEL = 'battery_level' 
DUSTY_SPOT = 'dusty_spot'
SPOT = 'spot'
GENERAL = 'general'
HOME_PATH = 'home_path'
TIME = 'time'

BOARD[BATTERY_LEVEL] = 100
BOARD[DUSTY_SPOT] = False
BOARD[SPOT] = False
BOARD[GENERAL] = False
BOARD[HOME_PATH] = ''
BOARD[TIME] = 1