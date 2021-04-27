# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 17:53:25 2021

@author: Nishith
"""

n=input("Please enter a number: ")
sum=0
n=eval(n)
for i in range(1,n+1):
    sum=sum+i*i*i
print(sum)
