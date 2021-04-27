# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:06:30 2021

@author: Nishith
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.

"""

def Prime(n1,n2):
    for i in range(n1, n2+1):
        if i>1:
            for j in range(2,int(i/2)+1):
                if(i % j==0):
                    break
            else:
                print(i,end=" ")
            
Prime(3,100)