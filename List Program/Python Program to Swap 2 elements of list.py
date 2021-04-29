# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:40:36 2021

@author: Nishith
"""

def Swap2(list,elem1,elem2):
    temp=list[elem1-1]
    list[elem1-1]=list[elem2-1]
    list[elem2-1]=temp
    return list

list=[23,4,55,66,41,3]
pos1=input("Enter 1st position: ")
pos2=input("Enter 2nd position: ")
print("New List: ",Swap2(list,int(pos1),int(pos2)))    