# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:06:49 2021

@author: Nishith
"""

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

Z = [[0,0,0],
     [0,0,0],
     [0,0,0]]
 
for i in range (len(X)):
    for j in range(len(X[0])):
        Z[i][j]=X[i][j]+Y[i][j]
         
for k in Z:
    print(k)