# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:52:52 2021

@author: Nishith
"""

def sort_list(list1, list2):

	zipped_pairs = zip(list2, list1)

	z = [x for c, x in sorted(zipped_pairs)]
	
	return z

x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))
