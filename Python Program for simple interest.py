# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 18:14:24 2021

@author: Nishith

Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate

EXAMPLE1:
Input : P = 10000
        R = 5
        T = 5
Output :2500
"""

def Interest(p,t,r):
    SI=p*t*r*0.01;
    print(SI)
    
Interest(10000,5,5)