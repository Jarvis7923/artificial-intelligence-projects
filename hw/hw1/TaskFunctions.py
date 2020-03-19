"""
define all the functions appeared in the task node
"""

import numpy as np
import random
from Type import *
from Board import *
# from Node import *

def task_test(node):
   """
   the test task function, return node status depends on a random number f
   """
   print("task")
   f = np.random.rand(1)[0]
   print("f = %s"%f)
   if f < 0.5:
      print("Success!")
      node.state = Results.SUCCESS
   elif f > 0.9:
      print("Running!")
      node.state = Results.RUNNING
   else:
      print("FAIL!")
      node.state = Results.FAIL

def do_nothing(node):
   """
   corresponding to the DO NOTHING node; return SUCCESS
   """
   node.state = Results.SUCCESS
   node.func_info = "[do nothing!]"

def find_home(node):
   """
   corresponding to the FIND HOME node: write HOME_PATH to the BOARD
   and return SUCCESS
   """
   hp = "home path is at somewhere around the corner!"
   BOARD[HOME_PATH] = hp
   node.func_info = "[find home!] " + hp
   node.state = Results.SUCCESS

def go_home(node):
   """
   corresponding to the GO HOME node: read HOME_PATH from the BOARD
   and return SUCCESS
   """
   hp = BOARD[HOME_PATH]
   if hp is not None:
      node.func_info = "[go home]  proceeding "+ hp
      node.state = Results.SUCCESS
   else:
      node.func_info = "[go home]  did not find home path"
      node.state = Results.FAIL

def dock(node):
   """
   corresponding to the DOCK node; return SUCCESS
   """
   node.func_info = "[dock!]"
   node.state = Results.SUCCESS

def clean_spot(node):
   """
   corresponding to the CLEAN SPOT node; return SUCCESS
   """
   node.func_info = "[clean spot!]"
   node.state = Results.SUCCESS

def done_spot(node):
   """
   corresponding to the DONE SPOT node: set the variable SPOT in BOARD to False
   and return SUCCESS
   """
   BOARD[SPOT]= False
   node.func_info = "[done spot!]"
   node.state = Results.SUCCESS

def done_general(node):
   """
   corresponding to the DONE GENERAL node: set the variable GENERAL in BOARD to False
   and return SUCCESS
   """
   BOARD[GENERAL] = False
   node.func_info = "[done general!]"
   node.state = Results.SUCCESS

def clean(node):
   """
   corresponding to the CLEAN node: 
   return FAIL 
   """
   node.func_info = "[clean!]"
   node.state = Results.FAIL


