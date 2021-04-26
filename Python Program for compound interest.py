# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 18:17:39 2021

@author: Nishith

Formula to calculate compound interest annually is given by:

A = P(1 + R/100) t
Compound Interest = A – P
Where,
A is amount
P is principle amount
R is the rate and
T is the time span

Input : Principle (amount): 1200
        Time: 2
        Rate: 5.4
Output : Compound Interest = 1333.099243
"""

def CompoundInterest(p,t,r):
    intr=p*pow((1+r/100),t)
    print(intr-p)
    
P=10000
t=10.25
r=5
    
CompoundInterest(P,t,r)