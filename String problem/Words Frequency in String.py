# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:27:17 2021

@author: Nishith
"""

from collections import Counter
st="siri siri amr siri o amr siri"
c=Counter(st.split())
print("The words frequency is: ",str(dict(c)))