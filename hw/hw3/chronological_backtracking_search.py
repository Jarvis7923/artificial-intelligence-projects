"""

The recursion implementation of the chronological backtracking search for the sudoku problem.

The order of which are pre-established in two ways according to the config in `Settings.py`.



author: shang wang 
student id: 1277417
email: swang27@tufts.edu

"""
from csp import *

def run(time_interval = SETTINGS[INTERVAL], anime = SETTINGS[ANIME]):
    """
    initialize the grid and establish the order beforehand

    Arguments
    -------
        time interval: the sleeping time in search each node. for the animation.
        anime: true for showing the animation; false for diabling the animation

    Arguments
    -------
        time interval: the sleeping time in search each node. for the animation.
        anime: true for showing the animation; false for diabling the animation


    Returns
    -------
        (flag, result): 
            flag: True:Succeed , False:Fail
            result: puzzel grid object: Succeed, last step: Fail 
    """

    title = "Chronological backtracking Search Algorithm"
    grid = puzzle_grid(title, time_interval, anime)
    return recursive_backtracking(order=get_order(grid), step=0, grid=grid)

def recursive_backtracking(order, step, grid):
    """
    recursively bactracking the search tree. 
    
    Arguments
    -----------

        b: puzzel grid object
        order: the pre-established order
        step: the current step of in the order

    Returns
    -------
        (flag, result): 
            flag: True: Succeed , False : Fail
            result: puzzel grid object: Succeed, last step: Fail 

    """
    if step == len(order): 
        grid.show_result()
        return True, grid
    
    grid.display_grid( order[step] )
    (i,j) = order[step]
    for value in grid.states[i][j].possible_assignment:
        if check_consistency((i,j), value, grid):
            grid.states[i][j].assignment = value
            result =  recursive_backtracking(order, step + 1, grid)
            if result[0]: 
                return result
            grid.states[i][j].remove_assignment()
    return False, 

def get_order(grid):
    """
    Generate an order in advance of the search. An order is a list of index(row, col). The length of the list is the number of the variables(available slots) in the puzzle grid. The order is affected by the config in `Settings.py`.

    Arguments:
    --------
        gird: the puzzle grid object
    
    Returns:
    --------
        order: the order of searching. 
    """
    order = grid.variables
    if SETTINGS[ORDER] == order_type.row_first:
        order.sort()
        return order
    elif SETTINGS[ORDER] == order_type.random:
        random.shuffle(order) 
        return order
    else:
        raise Exception("order type error")

def check_consistency(index, value, grid):
    """
    check the consistency with all the constraints if assigning `value` to the variable with index = `index`

    Arguments
    --------
        index: the cell need to be assigned
        value: the value to be assigned to the variable
        grid: the sudoku puzzle grid.
    
    Returns
    -------
        flag: True if succeed; False if fails
    """
    for (i,j) in grid.states[index[0]][index[1]].constrainted_index_set:
        if value == grid.states[i][j].assignment:  return False
    return True


