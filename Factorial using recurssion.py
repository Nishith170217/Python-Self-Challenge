# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 18:03:30 2021

@author: Nishith
"""
def Factorial(n):
    return 1 if(n==0 or n==1) else n*Factorial(n-1);
print("Factorial is :", Factorial(6))
