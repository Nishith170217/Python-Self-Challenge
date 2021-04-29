# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:39:33 2021

@author: Nishith
"""

start=4
end=60
lst= [11, 22, 33, 1, 44,35 ,2, 4,222,78]
for n in lst:
    if(n%2!=0 and n>=start and n<=end ):
        print(n, end=" ")