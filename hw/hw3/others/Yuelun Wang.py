#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 20 13:27:12 2019

@author: Yuelun Wang
"""
import numpy as np
def print_grid(arr):
    data = np.array(arr).reshape((9, 9))
    print(data)

# find all the positions that have no value, if all positions have value, return False
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                # print("empty: row="+str(row)+" col="+str(col))
                return True
    return False


# if this num have appeared in the rows of this arr
def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


#  if this num have appeared in the cols of this arr
def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


# if this num have appeared in the 3*3 matrix
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[row+i][col+j] == num:
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)


def solve_sudoku(arr):
    l = [0, 0]
    # find positions that have no value 
    if not find_empty_location(arr, l):
        return True
    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if check_location_is_safe(arr, row, col, num):
            arr[row][col] = num
            #print_grid(arr)
            if solve_sudoku(arr):
                return True
            #if currant num makes the whole problem has solution,
            #so currant value is invalidated, set this position to 0
            arr[row][col] = 0

    return False



if __name__ == "__main__":

    grid =  [[6, 0, 8, 7, 0, 2, 1, 0, 0],
             [4, 0, 0, 0, 1, 0, 0, 0, 2],
             [0, 2, 5, 4, 0, 0, 0, 0, 0],
             [7, 0, 1, 0, 8, 0, 4, 0, 5],
             [0, 8, 0, 0, 0, 0, 0, 7, 0],
             [5, 0, 9, 0, 6, 0, 3, 0, 1],
             [0, 0, 0, 0, 0, 6, 7, 5, 0],
             [2, 0, 0, 0, 9, 0, 0, 0, 8],
             [0, 0, 6, 8, 0, 5, 2, 0, 3]]
    if solve_sudoku(grid):
        print_grid(grid)
    else:
        print("No solution exists\n")
