
"""

Test script for the sudoku problem

author: shang wang 
student id: 1277417
email: swang27@tufts.edu

"""


import time
import sys

from Settings import *

# Override the settings in `Settings.py`
SETTINGS[ANIME] = False
SETTINGS[INTERVAL] = 0.0

# for chronological backtracking search
SETTINGS[PUZZLE] = puzzle_type.evil_puzzle
SETTINGS[ORDER] = order_type.row_first

import conflict_directed_backjumping_serach as cdb_search
import chronological_backtracking_search as cb_search
import varying_order_backtracking_search as vob_search

if __name__ == "__main__":

    cb_search.run()
    input("\npress ENTER to continue...")
    print("\33[1A \33[K \33[95m =============================== \33[0m") 

    vob_search.run()
    input("\npress ENTER to continue...")
    print("\33[1A \33[K \33[95m =============================== \33[0m") 
    
    cdb_search.run()
    print(" \n \33[95m =============================== \33[0m") 



 

































