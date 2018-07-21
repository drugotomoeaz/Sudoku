# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:28:49 2018

@author: Pandora
"""

from suList import suList, weightList
from sqList import sqSortedList
from random import random,choices,sample

class Sudoku(object):
    def __init__(self):
        self.weights = weightList
        self.suList = suList
        self.numbers = []
        self.indexes = list(range(81))
        self.squares = sqSortedList
        
    
    def squareClean(self, i):
        '''
        Clean all duplicated numbers in the same square
        i - index of suList
        self.squares - stores indexes of the numbers in the squares
        Returns nothing
        '''
        for item in self.squares:
            if i in item:
                for key in item[item.index(i):]:
                    #will raise an error if the number is deleted already; fix it
                    try:
                        del self.weights[key][suList[key].index(self.numbers[i])]
                        suList[key].remove(self.numbers[i])
                    except:
                        pass
                break

    def rowClean(self, i):
        '''
        Clean all duplicated numbers at the same row
        i - index of suList
        Returns nothing
        '''        
        for x in range(i + 1, i+(9 - i%9)):
            try:
#                self.suList[x][self.numbers[i] - 1] = 0
                del self.weights[x][suList[x].index(self.numbers[i])]
                suList[x].remove(self.numbers[i])
            except:
                pass
        
    def colClean(self, i):
        '''
        Clean all duplicated numbers at the same column
        i - index of suList
        Returns nothing
        '''
        for x in self.indexes[i + 9::9]:
            try:
#                self.suList[x][self.suList[i] - 1] = 0
                del self.weights[x][suList[x].index(self.numbers[i])]
                suList[x].remove(self.numbers[i])
            except:
                pass
    
    def upWeight(self, i):
        for square in self.squares[2::3]:
            if i in square[:-3]:
                for x in range(((i//9 + 1)*9), ((i//9 + 1)*9) + 6):
                    if self.numbers[i] in self.suList[x]:
                        self.weights[x][self.suList[x].index(self.numbers[i])] += 2
                    
                
        
        
    
    def suGen(self):
        i = 0
        while i <= 80:
            number = choices(self.suList[i], self.weights[i])
            self.numbers.append(number[0])
            #remove that number from other lines
            #for number at the same row
            self.rowClean(i)
            #for number at same column, delete it
            self.colClean(i)
            #for numbers in the square, delete it
            self.squareClean(i)
            self.upWeight(i)
            
            i += 1
            



p = Sudoku()
p.suGen()
print(len(p.numbers))
print(p.numbers)
print(p.weights)








                    