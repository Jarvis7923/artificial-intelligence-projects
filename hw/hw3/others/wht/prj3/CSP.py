from Board import *
from Settings import *
import copy

###################### BackJumping Search ######################

def BackJumpingSearch(type):
    """
    This is the implementation of conflict-directed backjumping search algorithm.
    
    It takes the type of the board (easy or evil) to initialize the board.

    And the order it explore is dynamically observed by least the available assignment of each cell.
    """
    # Initialize the empty board with the puzzle type
    emptyBoard = Board(type)
    order = Order(emptyBoard)
    # Initialize the dynamic order
    dynamicOrder = DynamicOrder(emptyBoard)
    # Set the conflict area for each cell
    emptyBoard.setConflictAreas(order.assignOrder)
    # Add the possible value for each cell in the empty board
    emptyBoard.setPossibleValue(order.assignOrder)
    # Assign the empty board to a board for calculation
    board = copy.deepcopy(emptyBoard)
    # iteration step
    step = 0
    # Iteration
    return RecursiveBackJumping(step,board,dynamicOrder)

def RecursiveBackJumping(step,board,order):
    """
    This is the function for recursion in conflict-directed backjumping

    The parameters it takes are listed as below:
      1. step: the current explored step
      2. board: the current state of the board
      3. order: the dynamic order of the assignment

    This function would return:
    1. The flag denoting whether it has found the solution or not
    2. The step it should jump to or the full board (solution)
    """
    # Show the board
    board.show()
    # If it finds the solution, return true and the board
    if step is order.totalNumber :
        return True, board
    # Get the position with the minimum available 
    position = board.getCellOfMiniPos()
    # Add that position into order
    order.addOrder(position)
    # Get the current cell to assign value
    curCell = board.getCell(position)
    # Find the available value to assign
    for val in curCell.possibleVal :
        if board.conflictCheckAndAdd(position, step, val) :
            # If it successfully finds a value, recursively finds the value for the next cell
            flag, result = RecursiveBackJumping(step+1,board,order)
            # If recursion success, returns to the former caller
            if flag:
                return flag, result
            # If it fails and has not come to the jumped caller, returns to the former caller
            if step > result:
                return flag, result
            # If it reaches the eaxct jumped step, restore the board before the cell is assigned then try another value
            board.restoreBoard(step,order)
            curCell.changeValue(0)
    # If it can not find a value to assign, it goes to find the exact step it should be
    step = ConflictBackJumping(step,position,board,order)
    # Return false and the step
    return False, step


def ConflictBackJumping(step,position,board,order):
    """
    This function is to find the exact step to jump back.

    The parameters it takes are listed as below:
      1. step: the current step where nothing available can be assigned
      2. position: the current position of the cell
      3. board: the current state of the board
      4. order: the current list of assignment order
    """
    # Get the cell which causes the conflict
    currentCell = board.getCell(position)
    # Add current step into a list which stores the used steps
    usedSteps = [step]
    # Pop from the conflict list of current cell
    lastCell = currentCell
    lastConflictSet = lastCell.conflictSet.pop()
    # Get the step of the new cell
    step = lastConflictSet.step
    currentCell = board.getCell(lastConflictSet.index)
    # Check whether there is other available value to assign
    while not currentCell.getAvailableValue():
        # If not, then add the current step into the list which stores the used steps
        usedSteps.append(step)
        usedSteps = list(set(usedSteps))
        # Merge the conflict list
        currentCell.conflictSet = mergeConflict(currentCell.conflictSet,lastCell.conflictSet)
        # Pop from the conflict list of the cell
        lastCell = currentCell
        lastConflictSet = lastCell.conflictSet.pop()
        # Get the step and the corresponding cell
        step = lastConflictSet.step
        currentCell = board.getCell(lastConflictSet.index)
        # delete those already explored in the list of used steps
        tmp = copy.deepcopy(currentCell.conflictSet)
        for item in tmp:
            if item.step in usedSteps:
                currentCell.conflictSet.remove(item)
    # Clear the value after current step and return the step
    for stp in range(step,len(order.order)):
        index = order.order[stp]
        board.getCell(index).changeValue(0)
    return step

def mergeConflict(curConflictSet, lastConflictSet):
    """
    This function is used to merge the conflict set of the current cell and the last cell and rearrange them in order
    """
    mergeList = list(set(curConflictSet + lastConflictSet))
    mergeList.sort(key=takeConflictKey)
    return mergeList
    

###################### Backtracking Search ######################
        
def BacktrackingSearch(type):
    """
    This is the implementation of chronological backtracking search algorithm.
    
    It takes the type of the board (easy or evil) to initialize the board.

    And the order it explore is predefined.
    """
    # Initialize the empty board with the puzzle type
    emptyBoard = Board(type)
    # Get the order of the cells to be assigned
    order = Order(emptyBoard)
    # Set the conflict area for each cell
    emptyBoard.setConflictAreas(order.assignOrder)
    # Add the possible value for each cell in the empty board
    emptyBoard.setPossibleValue(order.assignOrder)
    # Assign the empty board to a board for calculation
    board = copy.deepcopy(emptyBoard)
    # iteration step
    step = 0
    # Iteration
    return RecursiveBacktracking(step,board,order)

def RecursiveBacktracking(step,board,order):
    """
    This is the function for recursion in chronological backtracking

    The parameters it takes are listed as below:
      1. step: the current explored step
      2. board: the current state of the board
      3. order: the predefined order of the assignment

    This function would return:
    1. The flag denoting failure or the solution board
    """
    # show the board
    board.show()
    # If it finds the solution, return true and the board
    if step is len(order.assignOrder) :
        return board
    # Get the position of the cell to be assigned in the order list
    position = order.assignOrder[step]
    # Get the current cell to assign value
    curCell = board.getCell(position)
    # Find the available value to assign
    for val in curCell.possibleVal :
        if board.conflictCheck(position, val) :
            # Change the value of current cell
            curCell.changeValue(val)
            # If it successfully finds a value, recursively finds the value for the next cell
            result = RecursiveBacktracking(step+1,board,order)
            # If the result is not false, returns to the former caller
            if result is not False :
                return result
            # If the result is false, change the value back to zero
            curCell.changeValue(0)
    # If it can not find a value to assign, it returns false to the former caller
    return False
