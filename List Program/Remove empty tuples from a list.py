# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:51:25 2021

@author: Nishith
"""
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
tuples=[ele for ele in tuples if ele!=()]
print(tuples)