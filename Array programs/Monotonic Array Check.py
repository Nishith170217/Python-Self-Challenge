# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:19:44 2021

@author: Nishith
"""

def isMonotonic(arr):

	return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or
			all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))

arr = [6, 5, 4, 4]

print(isMonotonic(arr))
