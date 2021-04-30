# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:56:29 2021

@author: Nishith
"""

def Repeat(lst):
	l = len(lst)
	repeated = []
	for i in range(l):
		k = i + 1
		for j in range(k, l):
			if lst[i] == lst[j] and lst[i] not in repeated:
				repeated.append(lst[i])
	return repeated

lst = [10, 20, 30, 20, 20, 30, 40,
		50, -20, 60, 60, -20, -20]
print (Repeat(lst))
	
