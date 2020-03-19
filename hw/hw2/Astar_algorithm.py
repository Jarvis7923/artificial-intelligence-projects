
"""
The implementation of the Astar Algorithm for the flip pancake problem

author: shang wang 
student id: 1277417
email: swang27@tufts.edu

"""
import numpy as np
import time
# from multiprocessing import Pool

from Settings import *

########################################################################
#                       implementation of Astar                        #

def run(init_state):
    """
    The Astar implementation, 
    
    Arguments
    -------
       initial state: a suffled array of [1,2,3,...], its length depends on the config in SETTINGS

    Returns
    --------
    a tuple of information in the process:
    
        sol: the final solution, a list of states
        iter: the total iterations
        cost: the cost of the solution
        the final num of nodes in frontier
        time spent in the algorithm
    """
    start = time.time()
    front = frontier(node(init_state)) # put the first node into the frontier
    print("heuristic function: " + SETTINGS[HEURISTIC].name)
    print("cost function: " + SETTINGS[COST].name)
    iter = 0
    while (True):
        # if the frontier has no zero element, return fail
        if front.length == 0: 
            end = time.time()
            return (False, iter, None, 0, end-start)
        n = front.top_node # extract the node with lowest cost
        if n.state == SETTINGS[GOAL]: 
            end = time.time()
            return (n.backtrack(), iter, n.total_cost, front.length, end-start) # goal test
        for i in range(len(n.state)-1):
            front.add(node(state=flip(n.state, i), parent=n, action=i))
        iter += 1
        if iter % 50 == 0: print("\rprogress: %s"%iter, end="")
    

def flip(arr, index):
    """
    split the arr into arr[0, 1, ..., index-1] and arr[index, index+1,...]  
    reverse the second part and returns the combined array of the two subarrays 
    """
    return np.r_[arr[:index], np.flip(arr[index:])].astype(np.int).tolist()

#                       implementation of Astar                        #
########################################################################


########################################################################
#                   implementation of cost functions                   #
#                       1. uniform step cost                           # 
#                       2. step flip number cost                       #     

def cost(state, parent_state, action):
    """
    determine the cost function of the problem:
    pass the argument state parent state and action to the cost function
    
    Returns:
    --------
        function name of the cost function
    """
    fun = uniform_step_cost
    if SETTINGS[COST] ==  cost_type.UNIFORM_STEP_COST:
        fun = uniform_step_cost
    elif SETTINGS[COST] ==  cost_type.STEP_FLIP_NUMBER_COST:
        fun = step_flip_number_cost
    else:
        raise Exception("Not supported heuristic function")
    return fun(state, parent_state, action) 

def uniform_step_cost(state, parent_state, action):
    """
    uniform cost: returns 1 for any given argument
    """
    return 1

def step_flip_number_cost(state, parent_state, action):
    """
    step cost 1 plus numbers of pancakes required to be filped
    and multiplied by some coefficient
    """
    return 1 + (len(state)-action)/(len(state)*5)

#                   implementation of cost functions                   #
########################################################################


########################################################################
#                 implementation of heuristic functions                #   
#                       1. gap cost                                    #  
#                       2. euclidean dist                              #  
#                       3. empty heuristic                             #  

def heuristic_value(state):
    """
    determine the heuristic function of the problem:
    pass the argument state parent state and action to the hueristic function
    
    Returns:
    --------
        function name of the heuristic function
    """
    if SETTINGS[HEURISTIC] ==  heuristic_type.EUCLIDEAN_DIST:
        fun = euclidean_dist
    elif SETTINGS[HEURISTIC] == heuristic_type.GAP_DIST:
        fun = gap_dist
    elif SETTINGS[HEURISTIC] == heuristic_type.NONE:
        fun = empty_heuristic
    else:
        raise Exception("Not supported heuristic function")
    return fun(state, SETTINGS[GOAL]) 

def empty_heuristic(state, goal):
    """
    returns zero heuristic value every time
    """
    return 0

def euclidean_dist(state, goal):
    """
    returns euclidean distance between the current state and the goal state 
    """
    return np.linalg.norm(state - goal)

def gap_dist(state, goal):
    """
    the gap heuristic function from the reference
    """
    return np.sum(np.where(np.abs(state - np.r_[state[1:], state[-1]]) > 1, 1, 0)).tolist()

#                 implementation of heuristic functions                #   
########################################################################

########################################################################
#                         Additional class                             #   
#                          1. node class                               #  
#                          2. frontier                                 #  

class node:
    """
    node object for the Astar search tree

    Arguments
    --------
        state: the current state of the node, which is the array of numbers indicates the sequence of the pancakes
        parent: the parent node of the current node
        action: how to get the current state from the parent state, i.e. parent [0,2,1], action 1 means flip the subarray from index 1
    
    Private Methods
    ---------
        get_backward_cost(): get the cost of the problem
        get_forward_cost(): get the heuristic value of the problem 

    Public Methods
    --------
        backtrack: recursively track the parent state, and generate the solution
    """
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.backward_cost = self.__get_backward_cost()
        self.forward_cost = self.__get_forward_cost()
        self.total_cost = self.backward_cost + self.forward_cost

    def __get_backward_cost(self):
        if self.parent is not None:
            return cost(self.state, self.parent.state, self.action) + self.parent.backward_cost
        else:
            return 0

    def __get_forward_cost(self):
        return heuristic_value(self.state) 

    def backtrack(self):
        if self.parent is None:
            return [(self.state,self.action)] 
        else:
            sol = self.parent.backtrack()
            sol = sol + [(self.state, self.action)] 
        return sol
        
class frontier:
    """
    frontier object for restoring and adding the visited node

    Properties
    -------
        length: length of the frontier, number of visted nodes
        top_node: extract the node with minimun cost meanwhile remove it from the node list 
    
    Methods
    -------
        add: add a node to the frontier, check the repeated node and remove the node with higher total cost  
    """
    def __init__(self, node):
        self.__node_list = [node]
        # self.__node_cost_list = [node.total_cost]
    
    @property
    def length(self):
        return len(self.__node_list)

    @property
    def top_node(self):
        node_cost_list = list(map(lambda x: x.total_cost, self.__node_list))
        i = np.argmin(node_cost_list) 
        return self.__node_list.pop(i)

    def add(self, node):
        for item in self.__node_list:
            if item.state == node.state :
                if item.total_cost > node.total_cost:
                    self.__node_list.remove(item)
                    # self.__node_list = [node] + self.__node_list
                    self.__node_list.append(node)
                return
        self.__node_list = [node] + self.__node_list
        # self.__node_list.append(node)
        
#                         Additional class                             #   
########################################################################



