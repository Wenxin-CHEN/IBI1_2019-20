# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:41:18 2020

@author: 陈文心
"""

filename=input('input a filename as a new fasta file:')
newfile=open(filename,'w')
import re
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
f=a.read()
seq_mito=re.findall(r'(>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?)>',f)
#delete the unnecessary part
for gene in seq_mito:
    simplify_seq_mito=re.sub(r'>.*?(gene:.*? ).*?]',r'\1',gene)
#delete the '\n' and '>'
    newone=simplify_seq_mito.replace('\n','')
    length=len(newone)-11
    b=">"+'gene length:'+str(length)+' '+newone+"\n"
    reseq=''
    for n in b:
        if n=='A':
            reseq+='T'
        elif n=='T':
            reseq+='A'
        elif n=='C':
            reseq+='G'
        elif n=='G':
            reseq+='C'
        else:
            reseq+=n
    newfile.write(reseq)
newfile.close()
print(open(filename).read())