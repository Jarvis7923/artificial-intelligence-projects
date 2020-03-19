
"""

The definition of useful class for solving the sudoku as a constraint-satisfaction problem 
    
    class: 
        cell
        puzzel_grid
    
    func:
        get_order

author: shang wang 
student id: 1277417
email: swang27@tufts.edu

"""

import copy
import random
import time

from Settings import *

if SETTINGS[ANIME]:
    try:
        import curses
    except:
        import platform
        sysstr = platform.system()
        if(sysstr =="Windows"):
            import os
            print("installing `windows-curses` for animation. (yes or no)", end="")
            s = input()
            if (s is 'yes') or (s is 'Yes') or (s is 'YES') :
                os.system('pip install windows-curses')
                import curses
            elif (s is 'no') or (s is 'No') or (s is 'N') :
                raise Exception("Curses is required for showing animation of the project. Change SETTINGS[ANIME] to False to close the animation ")
        else:
            raise Exception("Can not import the module `curses`. Change SETTINGS[ANIME] to False to close the animation")


class cell:
    """
    a cell object is one cell of the puzzle grid. 

    Arguments
    ---------
        index: the index of the cell in the grid

    Properties
    ----------
        index: the index of the cell in the grid
        possible_assignment: the domain of the cell variable if the cell is not immutable
        assignment: the current assignment of the cell, 0 if it's not been assigned
        immutable: (private set) True if the cell is assigned to a fixed value, False if it's a variable
        constrainted_index_set: the index of cells in the same row, col or region as the current cell.
        conflict_set: list of tuple, each element is like: (step, index, assignment) 
        avail_assignment: 

    Public Methods
    -----------
        as_immutable: change the cell to be immutable and give a fixed value
        remove_assignment: set the assignment to 0 if the cell is a variable

    """
    def __init__(self, index):
        self.__immutable = False
        self.index = index
        self.possible_assignment = list(range(1,10))
        self.conflict_set = []
        self.assignment = 0
        self.constrainted_index_set = self.__get_constrainted_index_set()
    
    def __get_constrainted_index_set(self):
        """
        removed the duplicates and the index of the current cell
        """
        (_i,_j) = self.index
        s = []
        for m in range(9):
            s.append((_i,m))
            s.append((m,_j))
        for i in range(3):
            for j in range(3):
                s.append(((_i//3)*3 + i,(_j//3)*3 + j))
        return list(set(s)- set([self.index]))
    
    @property
    def immutable(self):
        return self.__immutable
    
    @property
    def avail_assignment(self):
        if self.immutable: return []
        else:
            conflict_value = [item[2] for item in self.conflict_set]
            return list(set(self.possible_assignment) - set(conflict_value)- set([self.assignment]))

    def as_immutable(self, value):
        self.__immutable = True
        self.assignment = value
        self.possible_assignment = []
 
    def remove_assignment(self):
        if not self.__immutable:
            self.assignment = 0
        else:
            raise Exception("imutable cell !!!")

class puzzle_grid:
    """
    The object of puzzle grid. The states of which is a 9x9 2D list full of cells object. The immutable cells are the cells with given value. The remaining cells are the variables requiring assignment. 

    Properties
    --------

        states: 9x9 2-D list of cells
        available slots: list of index of all the assigned cells 

    Public methods
    ---------
    
        assign value: try assigning a value to a cell while considering the constaints
        conflicting assign value: try assigning a value to a cell while considering the constaints as well as the conflict sets
        show assigment: visualize the grid 
        show index: visualize the index of each cell of the grid

    """
    def __init__(self, title, time_interval, anime):
        self.__title = title
        self.__attempt = 0
        self.__time_interval = time_interval
        self.__anime = anime
        self.__time = time.time()
        self.__init_board_states()
        self.__init_possible_assignment()

    def __init_board_states(self):
        l,s  = [], []
        for i in range(9):
            row = []
            for j in range(9):  
                s.append((i,j))
                row.append(cell((i, j)))
            l.append(row)

        if SETTINGS[PUZZLE] is puzzle_type.easy_puzzle:
            p = self.__easy_puzzle()
        elif SETTINGS[PUZZLE] is puzzle_type.evil_puzzle:
            p = self.__evil_puzzle()
        else:
            raise Exception("puzzle type error")
        
        for item in p:
            s.remove(item[0])
            i,j = item[0]
            l[i][j].as_immutable(item[1])
            
        self.states = l
        self.variables = s

    def __easy_puzzle(self):
        """
        the configuration of the easy puzzle
        """
        value = [
            [(0,0),6],[(0,2),8],[(0,3),7],[(0,5),2],[(0,6),1],
            [(1,0),4],[(1,4),1],[(1,8),2],
            [(2,1),2],[(2,2),5],[(2,3),4],
            [(3,0),7],[(3,2),1],[(3,4),8],[(3,6),4],[(3,8),5],
            [(4,1),8],[(4,7),7],
            [(5,0),5],[(5,2),9],[(5,4),6],[(5,6),3],[(5,8),1],
            [(6,5),6],[(6,6),7],[(6,7),5],
            [(7,0),2],[(7,4),9],[(7,8),8],[(8,2),6],
            [(8,3),8],[(8,5),5],[(8,6),2],[(8,8),3]
        ]
        return value

    def __evil_puzzle(self):
        """
        the configuration of the evil puzzle
        """
        value = [
            [(0,1),7],[(0,4),4],[(0,5),2],
            [(1,5),8],[(1,6),6],[(1,7),1],
            [(2,0),3],[(2,1),9],[(2,8),7],
            [(3,5),4],[(3,8),9],
            [(4,2),3],[(4,6),7],
            [(5,0),5],[(5,3),1],
            [(6,0),8],[(6,7),7],[(6,8),6],
            [(7,1),5],[(7,2),4],[(7,3),8],
            [(8,3),6],[(8,4),1],[(8,7),5]
        ]
        return value

    def __init_possible_assignment(self):
        """
        Initialize the domain(possible assignment) of each variable(cell) based on the immuatable values in the puzzle grid as well as the constraints. 
        """
        for item in self.variables:
            (_i,_j) = item
            for item in self.states[_i][_j].constrainted_index_set:
                (i,j) = item
                if not self.states[i][j].immutable:
                    continue
                if self.states[i][j].assignment in self.states[_i][_j].possible_assignment:
                    self.states[_i][_j].possible_assignment.remove(self.states[i][j].assignment)
    
    def update_conflict_set(self, assigned_var):
        """
        Update the conflict set of all the assignable cells based on `order`. The update will stop once encountering one cell in `order` has not been assigned.

        Arguments:
        ----------
            order: the list of order for the search problem, a list of index. eg. [(row1,col1), (row2,col2), ... ] 

        """
        for index in self.variables:
            (i,j) = index
            self.states[i][j].conflict_set = []

        for i in range(len(assigned_var)):
            self.update_cell_conflict_set(assigned_var[i], i)
    
    def update_cell_conflict_set(self, index, step = 0):
        """
        Update the conflict set of all the cells in the puzzle grid based on assignment of the cell at `index` of the grid. The element in the conflict set of a cell is like: (step, index = (ros,col), assigment). 

        Arguments:
            index: the index of the cell used for updating the conflict set.
            step: at which step in order does this conflict happen

        """
        (_i,_j) = index
        for (i,j) in self.states[_i][_j].constrainted_index_set:
            if self.states[i][j].immutable:
                continue
            self.states[i][j].conflict_set.append((step, self.states[_i][_j].index, self.states[_i][_j].assignment))

    def show_explored_nodes(self):
        """
        Display the explored nodes during the process.
        """
        self.attempt += 1
        print("\r >> nodes explored = %s"%self.attempt, end="")


    def show_result(self):
        """
        Display the result of the searching algorithm.
        """
        try:
            curses.endwin()
        except:
            pass
        s = "\n\n" + self.__title + "\n[#i]: immutable cells, \n[ _]: unassigned cells\n" + "-"*37 + "\n" 
        nrow = 0
        for row in self.states:
            s += '|'
            ncol = 0
            for item in row:
                if item.assignment == 0:
                    s += " _ "
                else:
                    if item.immutable:
                        s += "#%s "%item.assignment
                    else:
                        s += "{:2} ".format(item.assignment)
                ncol += 1
                if ncol%3 == 0: s += "|  |"  
            s = s[:-1]
            s +=  "\n"
            nrow += 1
            if nrow%3 == 0: s += "-"*37 + "\n"
        s += "\n >> total nodes explored:  %s"%self.__attempt
        s += "\n >> time elapsed: {:4f} (s) ".format(time.time()-self.__time)
        print(s)


    def display_grid(self, cur_index):
        """
        Display the info of the current assignment.
        """
        self.__attempt += 1
        if not self.__anime:
            return
        screen = curses.initscr()
        s = "\n" + self.__title + "\n"
        s +="[#i]: immutable cells, \n[ _]: unassigned cells\n" + "-"*37 + "\n" 
        nrow = 0
        for row in self.states:
            s += '|'
            ncol = 0
            for item in row:
                if item.index == cur_index:
                    s += "->%s"%item.assignment
                else:
                    if item.assignment == 0:
                        s += " _ "
                    else:
                        if item.immutable:
                            s += "#%s "%item.assignment
                        else:
                            s += "{:2} ".format(item.assignment)
                ncol += 1
                if ncol%3 == 0: s += "|  |"  
            
            s = s[:-1]
            s +=  "\n"
            nrow += 1
            if nrow%3 == 0: s += "-"*37 + "\n"
        s+= ">>  node explored: %s"%self.__attempt
        screen.clear()
        screen.addstr(0, 0, s)
        screen.refresh()
        time.sleep(self.__time_interval)


