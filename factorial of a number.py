# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:52:45 2021

@author: Nishith
"""

def FindFactorial(n):
    f=1
    i=1
    for i in range(1,n+1):
        f=f*i
    print(f)
    
    
FindFactorial(5)