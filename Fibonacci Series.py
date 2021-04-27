
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:54:49 2021
Fn = Fn-1 + Fn-2

@author: Nishith
"""

def Fibonacci(n):
    a=0
    b=1
    print(0,1,end=" ")
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(b,end=" ")

Fibonacci(20)
    