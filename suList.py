# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:05:56 2018

@author: Pandora
"""
suList = []
for i in range(81):
    suList.append([1,2,3,4,5,6,7,8,9])
    
weightList = []
for i in range(81):
    weightList.append([1,1,1,1,1,1,1,1,1])


    
#suList = [[1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#          [1, 2, 3, 4, 5, 6, 7, 8, 9]]