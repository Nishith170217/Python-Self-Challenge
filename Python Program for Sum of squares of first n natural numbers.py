# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 17:46:36 2021

@author: Nishith

Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.
"""
n=input("Please enter a number: ")
sum=0
n=eval(n)
for i in range(1,n+1):
    sum=sum+i*i
print(sum)
