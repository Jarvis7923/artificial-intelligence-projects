#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:24:29 2019

@author: glen
"""
'''
    整体灵感就是
    1 求出每个数字为0的位置可以填的数，并将其位置和能填的数分别以key和value的方式
      存储到字典里面
    2 将字典里的数据按照所能填写的数据的多少进行排序，先在能填的数少的里面选取一个
      进行填写
    3 将填写的过程记录到列表里面，这个地方暂时想到的就是用列表记录填写过程
    4 更新1、2步，若出现某一步可填写的数据为空，说明之前某一步的选择有问题，回溯回
      去，更换数值，然后回到步骤1
    5 当所有的数都填完后，退出循环
'''
 
 

import numpy as np
import time
time1 = time.time()

def nine(data):
    nine_block = np.zeros([3,3,3,3], dtype = int)
    for i in range(3):
        for j in range(3):
            nine_block[i,j] = data[3*i:3*(i+1),3*j:3*(j+1)]
    return nine_block
 
def num_set(data, nine_block):
    pick_set = {}
    for i in range(9):
        for j in range(9):
            if data[i,j] == 0:
                pick_set[str(i)+str(j)] = set(np.array(range(10))) - (set(data[i,:]) | set(data[:,j]) | set(nine_block[i//3,j//3].ravel()))
    return pick_set
 
 
def try_insert(data):    
 
    insert_step = []
    while True:
        
        pick_set = num_set(data, nine(data))
        if len(pick_set) == 0: break
        pick_sort = sorted(pick_set.items(), key = lambda x:len(x[1]))#pick_sort（可选值）
        item_min = pick_sort[0]#item_min(优先选择值)
        key = item_min[0]
        value = list(item_min[1])#提取key和value of item_min
        insert_step.append((key, value))#通过insert step 插入
        if len(value) != 0:
            data[int(key[0]), int(key[1])] = value[0]#插入值
        else:
            insert_step.pop()
            for i in range(len(insert_step)):
                huishuo = insert_step.pop()
                key = huishuo[0]
                insert_num = huishuo[1]
                if len(insert_num) == 1:
                    data[int(key[0]), int(key[1])] = 0
                else:
                    data[int(key[0]), int(key[1])] = insert_num[1]
                    insert_step.append((key, insert_num[1:]))
                    break
    tiem2 = time.time()
    print('\nFinished! using time:', tiem2-time1, 's')
    print(data)    
   
if __name__ == '__main__':
    data =  [[6, 0, 8, 7, 0, 2, 1, 0, 0],
             [4, 0, 0, 0, 1, 0, 0, 0, 2],
             [0, 2, 5, 4, 0, 0, 0, 0, 0],
             [7, 0, 1, 0, 8, 0, 4, 0, 5],
             [0, 8, 0, 0, 0, 0, 0, 7, 0],
             [5, 0, 9, 0, 6, 0, 3, 0, 1],
             [0, 0, 0, 0, 0, 6, 7, 5, 0],
             [2, 0, 0, 0, 9, 0, 0, 0, 8],
             [0, 0, 6, 8, 0, 5, 2, 0, 3]]
    data = np.array(data).reshape((9, 9))
    print(data)
    try_insert(data)

