"""
For comparison, this is recursion implementation of the a DFS with improvements in variable and value ordering:

    1. Minimum remaining value(MRV) heuristic in choosing variables to assign

TODO: 
    2. Degree heuristic as tie breaker in MRV process
    3. Least-constraining value heuristic in the value domain of a variable

The algorithm can find a solution way more faster than the chronological search with pre-established order of variable assigning and a litter slower with respect to the version integrated with Conflict-Directed backjumping.  

author: shang wang 
student id: 1277417
email: swang27@tufts.edu

"""
from csp import *

def run(time_interval = SETTINGS[INTERVAL], anime = SETTINGS[ANIME]):
    """
    initialize the grid and run the recursive backjumping search algorithm.
    
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
    title = "Varying Order Backtracking Search Algorithm"
    return recursive_searching(assigned_var = [], grid = puzzle_grid(title, time_interval, anime))
 

def recursive_searching(assigned_var, grid):
    """
    recursively search the sudoku problem. The algorithm will expand child nodes with respect to the possible assignments of the parent node.  

    Arguments
    -------
        assigned var : a list of the index(eg. tuple(row, col) ) of 
                       assigned variables. 
        grid: the constraint-satisfaction problem, namely, the sudoku
              puzzle grid.
    
    Returns
    -------
        (flag, result): 
            flag: True:Succeed , False:Fail
            result: puzzel grid object: Succeed, last step: Fail 
    """

    if len(assigned_var) == len(grid.variables):  
        grid.show_result()
        return True, grid
    
    cur_index = 0 if len(assigned_var) == 0 else assigned_var[-1]
    grid.display_grid(cur_index)

    var = select_unassigned_variable(assigned_var, grid)
    for value in order_domain_value(var, assigned_var, grid):
        if check_consistency(var, value, grid):
            assign_value(var, value, assigned_var, grid)
            result =  recursive_searching(assigned_var, grid)
            if result[0]: return result
            remove_assignment(var, assigned_var, grid)
    return False,

def select_unassigned_variable(assigned_var, grid):
    """
    select a unassigned variable from all the unassigned variables guided by MRV heuristc.

    TODO: degree heuristic as tie breaker 

    Arguments
    --------
        assigned var : a list of the index(eg. tuple(row, col) ) of the
                       assigned variables. 
        grid: the sudoku puzzle grid.
    
    Returns
    -------
        the index of the variable with the largest amount of unattainable choices in the current situation
    """
    avail_var = sorted(list(set(grid.variables)-set(assigned_var)))
    l = []
    for (i, j) in avail_var:
        l.append(get_cell_constraints_number((i, j), grid))
    return avail_var[l.index(max(l))]


def get_cell_constraints_number(index, grid):
    """
    get the number of unavailable choices of a variable with index = `index` 

    Arguments
    --------
        index: the cell need to be assigned
        grid: the sudoku puzzle grid.
    
    Returns
    -------
       amount of unattainable choices of the variable with `index`
    """
    l = []
    for (i, j) in grid.states[index[0]][index[1]].constrainted_index_set:
        if grid.states[i][j].assignment:
            l.append(grid.states[i][j].assignment)
    return len(list(set(l)))

def check_consistency(index, value, grid):
    for (i,j) in grid.states[index[0]][index[1]].constrainted_index_set:
        if value == grid.states[i][j].assignment:  return False
    return True

def order_domain_value(index, assigned_var, grid):
    """
    generate the order of the domain value of a variable with `index`. 
    this could be done through the least-constraining value heuristic.
    
    TODO: a faster way to implement least-constraining value heuristic.

    Arguments
    --------
        index: the index of variable needed to be assigned
        assigned var : a list of the index(eg. tuple(row, col) ) of the
                       assigned variables. 
        grid: the sudoku puzzle grid.
    
    """
    return grid.states[index[0]][index[1]].possible_assignment
    # l = {}
    # for value in grid.states[index[0]][index[1]].possible_assignment:
    #     l[value] = 0
    #     for (i,j) in grid.states[index[0]][index[1]].constrainted_index_set:
    #         if not grid.states[index[0]][index[1]].immutable:
    #             if value in grid.states[i][j].avail_assignment:
    #                l[value] += 1
    # l = {k: v for k, v in sorted(l.items(), key=lambda item: item[1])}
    # res = list(l.keys())
    # # res.reverse()
    # return res

def remove_assignment(index, assigned_var, grid):
    """
    remove the value of the variable with `index` and delete this assignemnt in the assigmed variable list. 

    Arguments
    --------
        index: the cell need to be assigned
        assigned var : a list of the index(eg. tuple(row, col) ) of 
                       assigned variables. 
        grid: the sudoku puzzle grid.

    """
    grid.states[index[0]][index[1]].remove_assignment()
    assigned_var.remove(index)

def assign_value(index, value, assigned_var, grid):
    """
    Assign `value` to the variable with `index`. 
    Append the 'index' to assigned variable list `assigned var`

    Arguments
    --------
        index: the cell need to be assigned
        value: the value to be assigned to the cell
        assigned var : a list of the index(eg. tuple(row, col) ) of 
                       assigned variables. 
        grid: the sudoku puzzle grid.
    """
    grid.states[index[0]][index[1]].assignment = value
    assigned_var.append(index)
    
