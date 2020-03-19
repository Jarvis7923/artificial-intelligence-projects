"""
The basic settings for the Astar 

author: shang wang
email: swang27@tufts.edu

"""

import numpy as np 
from enum import Enum


class heuristic_type(Enum):
    """
    the type of heuristic functions

    Enumerables
    ------
        EUCLIDEAN_DIST: euclidean distance between the states and the goal states
        GAP_DIST: the gap distance of the states. ref. Malte Helmert,et al. Landmark Heuristics for the Pancake Problem 
    """
    NONE = 0
    GAP_DIST = 1
    EUCLIDEAN_DIST  = 2
    


class cost_type(Enum):
    """
    The cost function of the problem
    
    Enumerables
    ------
        UNIFORM_STEP_COST: each step has a uniform cost 1
        STEP_FLIP_NUMBER_COST: each step has a uniform cost 1 plus the how many pancakes are fliped and divide by 2
    """
    UNIFORM_STEP_COST = 0
    STEP_FLIP_NUMBER_COST = 1


SETTINGS = {}

# keys for the dict SETTINGS 
SEED = 'seed'
INIT_STATE = 'init_state'
GOAL = 'goal'
HEURISTIC = "heuristic"
COST = "cost"


# The random seed used to reproduce the experiments
SETTINGS[SEED] = 4
np.random.seed(SETTINGS[SEED])

# numbers of pancakes of numbers of 
n_arr = 7

# the initial state 
SETTINGS[INIT_STATE] = (np.random.choice(n_arr,n_arr,False) + 1).tolist()

# goal state depend on the init state
SETTINGS[GOAL] = np.flip( np.arange(1,len(SETTINGS[INIT_STATE])+1, dtype=np.int)).tolist()

# types of heuristic function used in Astar
SETTINGS[HEURISTIC] = heuristic_type.NONE

# types of cost function
SETTINGS[COST] = cost_type.UNIFORM_STEP_COST

# overwrite the SETTINGS[INIT_STATE] for array with any length
# SETTINGS[INIT_STATE] = [3,7,5,1,4,2,8,9,6,10]
# SETTINGS[INIT_STATE] = [3,5,1,4,2]
# SETTINGS[INIT_STATE] = [3,7,5,1,4,2,6]
# SETTINGS[INIT_STATE] = [1,2,3,4,5,6,8,7,10,9]
# SETTINGS[INIT_STATE] = [8,2,6,1,4,3,7,5,10,9]
# SETTINGS[INIT_STATE] = [6, 3, 4, 2, 1, 5, 7, 8, 10, 9]

