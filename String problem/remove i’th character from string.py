# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:20:07 2021

@author: Nishith
"""

def replaceChar(st):
    newSt=st.replace('s','',1) #Removing 1st s
    return newSt

def removeChar(st):
    newSt=""
    for i in range(len(st)):
        if(i!=2):
            newSt=newSt+st[i]
    return newSt

st="Nishith Ranjan Biswas"
print(replaceChar(st))
print(removeChar(st))