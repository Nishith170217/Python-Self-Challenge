# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 12:58:29 2021

@author: Nishith
"""

def sumOfDigit(lst):
    new=[]
    for elem in lst:
        sum=0
        for digit in str(elem):
            sum+=int(digit)
        new.append(sum)
    return new
            

lst=[12,33,44,34]
print(sumOfDigit(lst))