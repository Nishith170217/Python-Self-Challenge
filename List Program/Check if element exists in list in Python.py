# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:48:47 2021

@author: Nishith
"""

def LisElemcheck(list,elem):
    for i in list:
        if(i == elem) :
            print (elem," Exists.")
            break
        else:
            print(elem," doesn't exists.")
            break
list=['mango','jackfruit','guava','banana','apple','orrange']
elem='mano'
print(LisElemcheck(list,elem))

                