from Cell import *
from Settings import *
from itertools import chain
import numpy as np
import curses
import time

class Board :
    """
    This class defines the state of the board. It includes:

      1. board: the two dimension list of cells
      2. iterations: the number of the attempts it has been tried.
    """
    def __init__(self, type):
        """
        Initialize the board with type (easy or evil)
        """
        # Initialize the board with empty cell
        self.board = []
        self.iterations = 0
        for i in range(9) :
            row = []
            for j in range(9) :
                tmp = Cells((i,j),False)
                row.append(tmp)
            self.board.append(row)
        # Filled the board with fixed value
        if type is PuzzleType.easy :
            self.initEasyBoard()
        elif type is PuzzleType.evil :
            self.initEvilBoard()
        else :
            raise Exception("Undefined puzzle type!")
    
    def initEasyBoard(self):
        """
        Initialize the easy board
        """
        self.changeCell((0,0),6)
        self.changeCell((0,2),8)
        self.changeCell((0,3),7)
        self.changeCell((0,5),2)
        self.changeCell((0,6),1)
        self.changeCell((1,0),4)
        self.changeCell((1,4),1)
        self.changeCell((1,8),2)
        self.changeCell((2,1),2)
        self.changeCell((2,2),5)
        self.changeCell((2,3),4)
        self.changeCell((3,0),7)
        self.changeCell((3,2),1)
        self.changeCell((3,4),8)
        self.changeCell((3,6),4)
        self.changeCell((3,8),5)
        self.changeCell((4,1),8)
        self.changeCell((4,7),7)
        self.changeCell((5,0),5)
        self.changeCell((5,2),9)
        self.changeCell((5,4),6)
        self.changeCell((5,6),3)
        self.changeCell((5,8),1)
        self.changeCell((6,5),6)
        self.changeCell((6,6),7)
        self.changeCell((6,7),5)
        self.changeCell((7,0),2)
        self.changeCell((7,4),9)
        self.changeCell((7,8),8)
        self.changeCell((8,2),6)
        self.changeCell((8,3),8)
        self.changeCell((8,5),5)
        self.changeCell((8,6),2)
        self.changeCell((8,8),3)


    def initEvilBoard(self):
        """
        Initialize the evil board
        """
        self.changeCell((0,1),7)
        self.changeCell((0,4),4)
        self.changeCell((0,5),2)
        self.changeCell((1,5),8)
        self.changeCell((1,6),6)
        self.changeCell((1,7),1)
        self.changeCell((2,0),3)
        self.changeCell((2,1),9)
        self.changeCell((2,8),7)
        self.changeCell((3,5),4)
        self.changeCell((3,8),9)
        self.changeCell((4,2),3)
        self.changeCell((4,6),7)
        self.changeCell((5,0),5)
        self.changeCell((5,3),1)
        self.changeCell((6,0),8)
        self.changeCell((6,7),7)
        self.changeCell((6,8),6)
        self.changeCell((7,1),5)
        self.changeCell((7,2),4)
        self.changeCell((7,3),8)
        self.changeCell((8,3),6)
        self.changeCell((8,4),1)
        self.changeCell((8,7),5)

    def setConflictAreas(self,order):
        """
        Set the conflict area for each cell
        
        The value in the conflict area of the cell can not be the same as the value in the cell
        """
        for item in order :
            assert not self.getCell(item).fixed
            self.getCell(item).setConflictArea(self.setForPosition(item))

    def setForPosition(self,position):
        """
        Get the conflict area of each cell
        """
        (row,col) = position
        x1 = row//3 * 3
        x2 = (row//3 + 1) * 3
        y1 = col//3 * 3
        y2 = (col//3 + 1) * 3
        # Get the regions of the 3 * 3 area
        regions = list(chain.from_iterable([item[y1:y2] for item in self.board[x1:x2]]))
        return list(set([item.index for item in self.board[row]] + [item[col].index for item in self.board] + [item.index for item in regions]))

    def changeCell(self, position, value):
        """
        Change the value of the cell in position
        """
        (row,col) = position
        self.board[row][col] = Cells(position,True,value)

    def setPossibleValue(self, order):
        """
        Set the possible values to the cells
        """
        for item in order :
            assert not self.getCell(item).fixed
            self.getCell(item).setPossibleVal(list(set(list(range(1,10)))-set(self.getNumbers(item))))

    def getNumbers(self, position):
        """
        Get the numbers that can not be assigned to a cell
        """
        checkLocation = self.getCell(position).ConflictArea
        numbers = []
        for item in checkLocation:
            numbers.append(self.getCell(item).value)
        numbers = list(set(numbers))
        return list(filter(lambda a: a != 0, numbers))

    def show(self):
        """
        Show the board 
        """
        screen = curses.initscr()
        string = ""
        self.iterations += 1
        for i in range(len(self.board)) :
            string += "|"
            if i%3 is 0:
                string += "-"*29 + "|" + "\n"
                string += "|"
            for j in range(len(self.board)) :                    
                val = self.getCell((i,j)).value
                if val is 0 :
                    string += "   " 
                else :
                    string += " %s "%val
                if j%3 is 2:
                    string += "|"
            string += "\n"
        string += "|" + "-"*29 + "|" + "\n" 
        string += "\n[Number of iteartions: %s]\n"%self.iterations
        screen.clear()
        screen.addstr(0, 0, string)
        screen.refresh()


    def getCell(self, position):
        """
        Get the cell in the position of the board
        """
        return self.board[position[0]][position[1]]

    def update(self, position, step):
        """
        Update the conflict set of the cell

        It is used in the backjumping search algorithm
        """
        currentCell = self.getCell(position)
        currentVal = currentCell.value
        affectedArea = list(set(currentCell.ConflictArea)-set([currentCell.index]))
        for pos in affectedArea :
            if not self.getCell(pos).fixed :
                self.getCell(pos).addConflictSet(step,position,currentVal)

    def conflictCheckAndAdd(self, position, step, value):
        """
        Check the whether there is an availavle value for the current cell

        If yes, change the value of the cell and update the conflict set of all the cells in its conflict area

        It is used in the backjumping search algorithm
        """
        conflictValue = [conflictSet.value for conflictSet in self.getCell(position).conflictSet]
        if value in conflictValue or (not self.conflictCheck(position,value)):
            return False
        self.getCell(position).changeValue(value)
        self.update(position,step)
        return True

    def restoreBoard(self,step,order):
        """
        Restore the board to the state of the step according to the order

        It is used in the backjumping search algorithm
        """
        for row in self.board :
            for item in row :
                if not item.fixed :
                    item.conflictSet = []
        for s in range(step):
            loc = order.order[s]
            self.update(loc,s)
        order.changeOrder(step+1)

    def conflictCheck(self, position, value):
        """
        Check the whether there is an availavle value for the current cell

        If yes, return true, otherwise it returns false
        """
        currentCell = self.getCell(position)
        affectedArea = list(set(currentCell.ConflictArea)-set([currentCell.index]))
        for pos in affectedArea :
            if not self.getCell(pos).fixed and self.getCell(pos).value is value :
                return False
        return True
    
    def getCellOfMiniPos(self):
        """
        Get the position of the cell which has the minimum available value taken conflict set into consideration
        """
        cellList =[]
        #  [cells for cells in self.board if cells.value is 0]
        for row in self.board :
            for item in row :
                if item.value is 0 :
                    cellList.append(item)
        cellPossible = list(map(lambda x: len(list(set(x.possibleVal)-set([item.value for item in x.conflictSet]))),cellList))
        index = np.argmin(cellPossible)
        return cellList[index].index
