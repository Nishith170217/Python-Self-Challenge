# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 09:43:49 2021

@author: Nishith
"""

def arryRotation(arr,d,l):
    arr[:]=arr[d:l]+arr[0:d]
    return arr

arr=[1,2,4,5,7,22]
l=len(arr)
print(arryRotation(arr,4,l))