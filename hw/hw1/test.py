import numpy as np
import time

from Type import *
from Node import *
from TaskFunctions import *
from ConditionFunctions import *
from Board import *
from BehaviorTree import *

if __name__ == "__main__":
    
    BOARD[BATTERY_LEVEL] = 100
    BOARD[DUSTY_SPOT] = True
    BOARD[HOME_PATH] = ''
    clean_request(2)

    iteration = 1
    """
    The battery level in the BOARD will decrease by some small amount each ineration
    """
    while True:
        print("\n==== RUNNING ITERATIONS %s ===="%i)
        start = time.time()

        tree['n0'].run()
        
        end = time.time()
        interval = end - start
        time.sleep(1 - interval)
        
        BOARD[BATTERY_LEVEL] -= 1
        if BOARD[BATTERY_LEVEL] < 0:
            break
        iteration = iteration + 1

