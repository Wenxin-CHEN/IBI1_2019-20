# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:40:35 2020

@author: 陈文心
"""
import sys
#read four numbers and change them into interger which are stored in list
four_number_input=input('please input four intergers between 1 and 23:(use comma to separate them)')
list1=four_number_input.split(',')
#change the input string to int    
list1=[int(x)for x in list1]
for i in list1:
    if i<1 or i>23:
        print('please input intergers between 1 and 23')
        sys.exit(0)
#try all numbers and symbols to test if the result can be 24, using 'for in + if'
#'one, two, three and four'are used to store extracted numbers
#if one is extracted from list 1, the following extracted number can only be chosen from list2 which deletes one
list2=[]
list3=[]
symbols=['+','-','*','/']
result='No Answer'  
class FindException(Exception) :
      pass
try:
    for i in range(4):
        one=list1[i]
        list2=list1[0:i]+list1[i+1:]
        for j in range(3):
            two=list2[j]
            list3=list2[0:j]+list2[j+1:]
            for k in range(2):
                three=list3[k]
                list4=list3[0:k]+list3[k+1:]
                four=list4[0]
#symbols can be used repeatedly
                for s1 in symbols:
                    for s2 in symbols:
                        for s3 in symbols:
                            express='(({0}{1}{2}){3}{4}){5}{6}'.format(one,s1,two,s2,three,s3,four)
                            if eval(express)==24:
                                raise FindException
#if express=24 exists, an error will be raised and the result will be changed. The error will be arrested by except and the 'for-in-loop' won't continue
#if all are trversed and no express is equal to 24, 'no answer' will be printed                            
except FindException:
    result='Yes'
    print('(({0}{1}{2}){3}{4}){5}{6}=24'.format(one,s1,two,s2,three,s3,four))
finally:
    print(result)
    print('time'+' '+str((i+1)*(j+1)*(k+1)*(symbols.index(s1)+1)*(symbols.index(s2)+1)*(symbols.index(s3)+1)))
    