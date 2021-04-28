# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:20:18 2021

@author: Nishith
"""


def Findlargest(arr,n):

	max = arr[0]
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max

arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = Findlargest(arr,n)
print ("Largest in given array is",Ans)


