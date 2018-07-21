# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 13:03:28 2018

@author: Pandora
"""

sqList = []

for x in range(27):
    sqList.append([])
    
for i in range(81):
    sqList[i // 3].append(i)
#print(sqList)

newsqList = []
for i in range(3):
    newsqList.append(sqList[i:9:3])
    newsqList.append(sqList[i + 9:18:3])
    newsqList.append(sqList[i + 18::3])
#print(newsqList)

newsqList.sort()
#newsqList = [[[0, 1, 2], [9, 10, 11], [18, 19, 20]],
#             [[3, 4, 5], [12, 13, 14], [21, 22, 23]],
#             [[6, 7, 8], [15, 16, 17], [24, 25, 26]],
#             [[27, 28, 29], [36, 37, 38], [45, 46, 47]],
#             [[30, 31, 32], [39, 40, 41], [48, 49, 50]],
#             [[33, 34, 35], [42, 43, 44], [51, 52, 53]],
#             [[54, 55, 56], [63, 64, 65], [72, 73, 74]],
#             [[57, 58, 59], [66, 67, 68], [75, 76, 77]],
#             [[60, 61, 62], [69, 70, 71], [78, 79, 80]]]

sqSortedList = []
for item in newsqList:
    sqSortedList.append([])
    for element in item:
        for number in element:
            sqSortedList[newsqList.index(item)].append(number)
        
#print(sqSortedList)
#
#sqSortedList = [[0, 1, 2, 9, 10, 11, 18, 19, 20], 
#                [3, 4, 5, 12, 13, 14, 21, 22, 23], 
#                [6, 7, 8, 15, 16, 17, 24, 25, 26], 
#                [27, 28, 29, 36, 37, 38, 45, 46, 47], 
#                [30, 31, 32, 39, 40, 41, 48, 49, 50], 
#                [33, 34, 35, 42, 43, 44, 51, 52, 53], 
#                [54, 55, 56, 63, 64, 65, 72, 73, 74], 
#                [57, 58, 59, 66, 67, 68, 75, 76, 77], 
#                [60, 61, 62, 69, 70, 71, 78, 79, 80]]
    