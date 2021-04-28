# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:16:35 2021

@author: Nishith
"""

def SumOfArray(arr):
    s=0
    for i in arr:
        s=s+i
    return s

arr=[2,4,5,6]
print(SumOfArray(arr))