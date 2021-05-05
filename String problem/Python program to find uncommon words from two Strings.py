# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:01:15 2021

@author: Nishith
"""

def Uncommon(A,B):
    x=A.split()
    y=B.split()
    z=''
    for i in x:
        if i not in y:
            z=z+" "+i
    for j in y:
        if j not in x:
            z=z+" "+j
    print("Uncommon words: ",z)

A="Hi there I am Siri"
B="Hello There I am Cortona"
Uncommon(A,B)