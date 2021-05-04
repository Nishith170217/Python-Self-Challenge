# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:27:14 2021

@author: Nishith
"""

def CheckSubString(st,sb):
    if(st.find(sb)== -1):
        print("Not found")
    else:
        print("Found")
st="kukur is the name of popol"
sb="popol1"
CheckSubString(st,sb)