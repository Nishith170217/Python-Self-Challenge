# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:35:03 2021

@author: Nishith
"""

def Palindrome(st):
    return st==st[::-1]

st="Nishith"
print(st[::-1])
ans=Palindrome(st)
if ans:
    print("Palindrome")
else:
    print("Not palindrome")