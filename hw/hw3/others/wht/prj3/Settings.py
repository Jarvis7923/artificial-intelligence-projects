import random
from enum import Enum
from Cell import *

class PuzzleType(Enum):
    """
    It defines whether the type of the puzzle is easy or evil
    """
    easy = 0
    evil = 1

class Order:
    def __init__(self, board):
        """
        This class defines the predefined order of the assignment sequence.
        
        It explores row by row.
        """
        self.__assignOrder = []
        for row in board.board :
            for item in row :
                if not item.fixed :
                    self.__assignOrder.append(item.index)
        
    @property
    def assignOrder(self):
        """
        Get the predefined order
        """
        return self.__assignOrder

class DynamicOrder:
    """
    This class defines the structure of dynamic order. It includes:
      1. __order: the order of the assignment
      2. __totalNumber: the total number of the cell to be assigned
    """
    def __init__(self,board):
        self.__order = []
        self.__totalNumber = 0
        for row in board.board :
            for item in row :
                if not item.fixed :
                    self.__totalNumber += 1
    
    def addOrder(self,index):
        """
        Add the current index to the dynamic order
        """
        self.__order.append(index)
    
    @property
    def totalNumber(self):
        """
        Get the total number of the cells to be assigned
        """
        return self.__totalNumber

    @property
    def order(self):
        """
        Get the assign order
        """
        return self.__order

    def changeOrder(self,location):
        """
        Get the order from the beginning to the location. It is used in backjumping algorithm when it jumps back
        """
        self.__order = self.__order[:location]