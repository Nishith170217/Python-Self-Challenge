# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:01:51 2021

@author: Nishith
"""
def sentenceWordReverse(st):
    words=st.split(" ")
    rvs=" ".join(reversed(words))
    return rvs
st="Hi I am Nishith"
print(sentenceWordReverse(st))
    