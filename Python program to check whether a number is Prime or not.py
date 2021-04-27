# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:20:24 2021

@author: Nishith
Prime Check
"""
def checkPrime(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")

checkPrime(7)
