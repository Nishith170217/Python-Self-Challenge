# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:15:05 2021

@author: Nishith
"""

def rotate(st,n):
    L1=st[0:n]
    L2=st[n:]
    R1=st[0:len(st)-n]
    R2=st[len(st)-n:]
    
    print("Left Rotation: ",L2+L1)
    print("Right Rotation: ",R2+R1)

st="NishithRanjanBiswas"
rotate(st,2)