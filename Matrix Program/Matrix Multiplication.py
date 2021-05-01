# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:37:15 2021

@author: Nishith
"""

import numpy as np
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
z=np.dot(A,B)
print(z)