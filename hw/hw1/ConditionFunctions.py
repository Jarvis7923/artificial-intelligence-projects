"""
define all the functions appeared in the condition node
"""

import numpy as np
from Type import *
from Board import *

def battery_check(node):
   """
   check the battery level from BOARD, return Results.SUCCESS if the battery level is lower than the checkpoint.
   args = checkpoint of the battery level
   """
   if node.args is None:
      raise Exception("No argument is passed from board")
   else:
      battery = BOARD[BATTERY_LEVEL]
      setpoint = node.args
      node.func_info = "BATTERY < %s ? %s"%(setpoint, battery)
   if battery < setpoint:
      node.state = Results.SUCCESS
   else:
      node.state = Results.FAIL

def spot_check(node):
   """
   check the SPOT in the BOARD. Return Results.SUCCESS if SPOT is True
   """
   node.func_info = "SPOT MODE ?"
   s = BOARD[SPOT]
   if s:
      node.state = Results.SUCCESS
   else:
      node.state = Results.FAIL

def general_check(node):
   """
   check the GENERAL in the BOARD. Return Results.SUCCESS if GENERAL is True
   """
   node.func_info = "GENERAL MODE ?"
   g = BOARD[GENERAL]
   if g:
      node.state = Results.SUCCESS
   else:
      node.state = Results.FAIL

def dusty_check(node):
   """
   check the DUSTY_SPOT in the BOARD. Return Results.SUCCESS if DUSTY_SPOT is True
   """
   node.func_info = "DUSTY SPOT ?"
   d = BOARD[DUSTY_SPOT]
   if d:
      node.state = Results.SUCCESS
   else:
      node.state = Results.FAIL


