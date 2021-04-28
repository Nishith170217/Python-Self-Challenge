# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:16:15 2021

@author: Nishith
"""

def ReminderArray(arr,n):
    mul=1
    for i in arr:
        mul=mul*i
        r=mul%n
    return r

arr=[100, 10, 5, 25, 35, 14]
print(ReminderArray(arr,11))