"""
Test script for the Astar and the Uniform=Cost-Search Algorithm

author: shang wang 
student id: 1277417
email: swang27@tufts.edu

"""
import time
import Astar_algorithm
# from Uniform_cost_search import uniform_cost_search
from Settings import *

def Astar(init_state):
    """
    A_star for flip pancake problem
    """
    print("-"*15+"\nA* Algorithm\n"+"-"*15)
    # SETTINGS[COST] = cost_type.UNIFORM_STEP_COST
    # SETTINGS[HEURISTIC] = heuristic_type.GAP_DIST
    SETTINGS[GOAL] = np.flip( np.arange(1,len(init_state)+1, dtype=np.int)).tolist()
    return Astar_algorithm.run(init_state)
    
def UCS(init_state):
    """
    UCS for flip pancake problem
    """
    print("-"*15+"\nUCS Algorithm\n"+"-"*15)
    # SETTINGS[COST] = cost_type.UNIFORM_STEP_COST
    SETTINGS[HEURISTIC] = heuristic_type.NONE
    SETTINGS[GOAL] = np.flip( np.arange(1,len(init_state)+1, dtype=np.int)).tolist()
    return Astar_algorithm.run(init_state)

def state_string(state):
    s = ""
    for ele in state:
        s += "% 4d"%ele
    return s

def print_result(result):
    (sol, j, cost, n_frontier, t) = result
    indent = 2
    prompt = ">> "
    print("\n" + " "*indent + prompt + "solution: ")
    if sol is False:
        print(" "*(indent+3) + "No solution found!") 
    else:
        print(" "*(indent+3) + "state:  ", state_string(sol[0][0]))
        for ele in sol[1:]:
            print(" "*(indent+3) + "|-action " + " "*(4*(ele[1]+1) - 2)+ "^")
            print(" "*(indent+3) + "state:  ", state_string(ele[0]))

        
    print(" "*(indent) + prompt +  "total iteration: %s" % j)
    print(" "*(indent) + prompt +  "backward cost: %s" % cost)
    print(" "*(indent) + prompt +  "number of nodes in frontier: %s" % n_frontier)
    print(" "*(indent) + prompt +  "time elapsed(s): %s" % t)



if __name__ == "__main__":
    print('\n=========start!=========\n')
    
    # overwrite the SETTINGS[INIT_STATE] for array with any length
    # SETTINGS[INIT_STATE] = [3,7,5,1,4,2,8,9,6,10]
    # SETTINGS[INIT_STATE] = [3,5,1,4,2]
    # SETTINGS[INIT_STATE] = [3,7,5,1,4,2,6]
    # SETTINGS[INIT_STATE] = [1,2,3,4,5,10,8,7,6,9]
    SETTINGS[INIT_STATE] = [10,8,7,6,9,1,2,3,4,5]
    # SETTINGS[INIT_STATE] = [8,2,6,1,4,3,7,5,10,9]
    # SETTINGS[INIT_STATE] = [6, 3, 4, 2, 1, 5, 7, 8, 10, 9]
    
    SETTINGS[COST] = cost_type.UNIFORM_STEP_COST
    # SETTINGS[COST] = cost_type.STEP_FLIP_NUMBER_COST
    
    SETTINGS[HEURISTIC] = heuristic_type.GAP_DIST
    
    res_astar = Astar(SETTINGS[INIT_STATE])
    print_result(res_astar)
    res_ucs = UCS(SETTINGS[INIT_STATE])
    print_result(res_ucs)