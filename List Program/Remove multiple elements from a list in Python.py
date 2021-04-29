# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:34:19 2021

@author: Nishith
"""

lst=[1,3,4,5,6,64,53,2]
uw={2,4,6,64}

lst=[elem for elem in lst if elem not in uw]
print(lst)


#list1.remove(elem)