# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:37:02 2021

@author: Nishith
"""

def SwapElem(oldList):
    l=len(oldList)
    temp=oldList[0]
    oldList[0]=oldList[l-1]
    oldList[l-1]=temp
    return oldList

List=[2,3,4,5,11]
print(SwapElem(List))