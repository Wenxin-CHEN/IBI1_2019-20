# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 07:03:52 2020

@author: 陈文心
"""
#count the number of A/T/C/G in sequence
#creat a dictionary with keys 'A/T/C/G'
frequency={'A':0,'T':0,'C':0,'G':0}
sequence="ATGCTTCAGAAAGGTCTTAGG"
frequency['A']=sequence.count('A')
frequency['T']=sequence.count('T')
frequency['C']=sequence.count('C')
frequency['G']=sequence.count('G')
#sizes of pie chart can be taken from dictionary
import matplotlib.pyplot as plt
labels=('T','C','G','A')
sizes=[frequency['T'],frequency['C'],frequency['G'],frequency['A']]
#define the color,size,labels etc. of pie chart
colors=['yellowgreen','cyan','lightskyblue','lightcoral']
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()