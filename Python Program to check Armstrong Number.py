# -*- coding: utf-8 -*-
"""
Spyder Editor
abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153
This is a temporary script file.
"""

def armstrong(num):
   sum  =  0
   order=len(str(num))
   temp  =  num 
   while  temp  >  0: 
       digit  =  temp  %  10 
       sum  +=  digit  **  order
       temp  //=  10

   if  num  ==  sum: 
       print("armstrong")
   else:
       print("Not armstrong")

armstrong(1634)