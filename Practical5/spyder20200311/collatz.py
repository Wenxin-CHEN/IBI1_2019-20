# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:17:49 2020

@author: 陈文心
"""
#if n is not equal to 1. if n is even, n=n/2, if n is odd n=n*3+1
#if n is equal to 1, stop the loop
n=45
print(n)
while n!=1:
    if n%2==0:
        n=n/2
        print(n)
    else:
       n=n*3+1
       print(n)