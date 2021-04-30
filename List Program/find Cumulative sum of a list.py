# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:16:17 2021

@author: Nishith
"""

def CumulativeSum(lst):
    ln=len(lst)
    new=[]
    j=0
    for i in range(ln):
        j=j+lst[i]
        new.append(j)
    return new

lst = [10, 20, 30, 40, 50] 
print(CumulativeSum(lst))       