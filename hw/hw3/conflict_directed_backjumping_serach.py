"""

The recursion implementation of the Conflict-Directed Backjumping search for the sudoku problem.

Since the interleaving strategy - forward checking - does not help in the backjumping search, it does not appear in this implementation at all.

Other intellegent technics in variable and value ordering:

    1. Minimum remaining value(MRV) heuristic in choosing variables to assign
    2. Degree heuristic as tie breaker in MRV process
    3. Least-constraining value heuristic in the value domain of a variable

Although the backjumping could lead to a faster convergence of the algorithm, it might cause failure at the same time according to our observation. The order of the variable as well as the domain of this variable matter a ton in the backjumping implementation.


author: shang wang 
student id: 1277417
email: swang27@tufts.edu

"""

import time

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

    title = "Conflict-Directed Backjumping Search Algorithm"
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
            else:
                if len(assigned_var)-1 > result[1]:
                    remove_assignment(var, assigned_var, grid)
                    return result
                else:
                    remove_assignment(var, assigned_var, grid)
                    grid.update_conflict_set(assigned_var)
    return False, conflict_directed_backjump(grid.states[var[0]][var[1]], grid)

def conflict_directed_backjump(src, grid, explored_var = []):
    """
    recursively searching for a variable with available assignments in the conflict set and returns to the step in the current assigend variable list `assigned var`. 

    Arguments:
    ---------
        src: the current variable running out of all the choices
        grid: the sudoku puzzle grid.
        explored var: list of the index of explored varibles 
                      along the current backjumping preocess

    Returns
    ---------
        step in the current assigend variable list `assigned var`. 
    """
    explored_var = list(set(explored_var + [src.index]))
    step, (i,j), _  = src.conflict_set.pop()
    dst, l  = grid.states[i][j], []
    for (s,index, v) in dst.conflict_set:
        if index in explored_var:  l.append((s, index, v))
    dst.conflict_set = list(set(dst.conflict_set)- set(l))
    if dst.avail_assignment:  
        return step
    dst.conflict_set = merge_conflict_set(src, dst)
    return conflict_directed_backjump(dst, grid, explored_var)  


def merge_conflict_set(src_cell, dst_cell):
    """
    merge the two conflict set and sorted with the order of current `assigned var`.

    Arguments:
    ---------
        src cell: the current variable running out all the choices
        dst cell: the first variable recorded in the conflict set of `src cell` 

    Returns
    ---------
        a sorted conflict set without repeated elements
    """
    return sorted(list(set(src_cell.conflict_set + dst_cell.conflict_set) - set([dst_cell.index])))

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
        the index of the variable with the least amount of available choices in the current situation
    """
    avail_var = sorted(list(set(grid.variables)-set(assigned_var)))
    l = []
    for (i,j) in avail_var:
        l.append(len(grid.states[i][j].avail_assignment))
    return avail_var[l.index(min(l))]

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
    #         if value in grid.states[i][j].avail_assignment:
    #             l[value] += 1
    # l = {k: v for k, v in sorted(l.items(), key=lambda item: item[1])}
    # res = list(l.keys())
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
    update the the conflict set of the all the affected variables. 

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
    grid.update_cell_conflict_set(index, len(assigned_var)-1)
    

