# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:37:22 2021

@author: Nishith
"""

my_list = ['1', '2', '3', '4',
           '5','6', 'love',
               '8','9', '10']
def devide_chunks(my_list,n):
    for i in range(0,len(my_list),n):
        yield my_list[i:i+n]
        
n=3
print(list(devide_chunks(my_list,n)))