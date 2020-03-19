from ConflictSet import *

class Cells:
    """
    This class defines the relative information of the cell.

    The properties include:
      1. index: the index of the cell in the board
      2. __fixed: whether the value in the cell can be changed
      3. value: the current value of the cell
      4. possibleVal: the possible values of the cell. They are given at the initialization of the board.
      5. conflictSet: the conflict set of the current cell. It is used in backjumping search.
      6. __conflictArea: the area which confines the value of the cell. It is given at the initialization of the board.
    """
    def __init__(self, index, fixed, value = 0):
        """
        The initialization of the cell. Note that the value can not be zero if the cell is fixed.
        """
        self.index = index
        self.__fixed = fixed
        self.value = value
        self.possibleVal = []
        self.conflictSet = []
        self.__conflictArea = []
        if self.__fixed and self.value == 0 :
            raise Exception("Illeagal assignment!")

    @property
    def fixed(self):
        """
        Show the cell is fixed or not
        """
        return self.__fixed

    def setConflictArea(self,area):
        """
        Set conflict area of the cell
        """
        self.__conflictArea = area

    @property
    def ConflictArea(self):
        """
        Get the conflict area of the cell
        """
        return self.__conflictArea

    def setPossibleVal(self, valueList):
        """
        Set the possibleVal with given valueList
        """
        self.possibleVal += valueList
    
    def changeValue(self, value):
        """
        Change the value of the cell
        """
        self.value = value

    def addConflictSet(self, step, index, value):
        """
        Add conflict set to the current cell
        """
        self.conflictSet.append(Conflict(step, index, value))

    def getAvailableValue(self):
        """
        Get the available value of the cell with conflict set in consideration. It is used in backjumping algorithm
        """
        conflictVal = [item.value for item in self.conflictSet]
        if self.value is not 0:
            return list(set(self.possibleVal)-set(conflictVal)-set([self.value]))
        return list(set(self.possibleVal)-set(conflictVal))