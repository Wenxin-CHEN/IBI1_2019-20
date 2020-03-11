# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:15:06 2020

@author: 陈文心
"""
#fetch 2**x<a,a=a-2**x until a=0
#x ranges from 14 to 0
#b records each eligible x
a=c=2019
b=""
x=14
while a!=0:
    if 2**x<=a:
        a-=2**x
        b+="2^"+str(x)+"+"
        x=x-1
    else:
        x=x-1
print(str(c)+"is"+b)
            
            