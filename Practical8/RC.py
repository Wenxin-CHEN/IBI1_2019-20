# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 07:35:20 2020

@author: 陈文心
"""

seq='ATGCGACTACGATCGAGGGCCAT'
reseq=''
for n in seq:
    if n=='A':
        reseq+='T'
    elif n=='T':
        reseq+='A'
    elif n=='C':
        reseq+='G'
    else:
        reseq+='C'
print(reseq)
        