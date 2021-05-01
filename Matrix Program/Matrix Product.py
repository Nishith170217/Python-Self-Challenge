# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:47:49 2021

@author: Nishith
"""

from itertools import chain
def prod(val):
    mul=1
    for ele in val:
        mul*=ele
    return mul
    
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
m=prod(chain(*A))
print(m)