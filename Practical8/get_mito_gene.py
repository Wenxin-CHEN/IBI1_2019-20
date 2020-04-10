# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 07:46:38 2020

@author: 陈文心
"""
import re
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
newfile=open('mito_gene.fa',"w")
f=a.read()
seq_mito=re.findall(r'(>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?)>',f)
l1=[]
for gene in seq_mito:
#delete the unnecessary part
    simplify_seq_mito=re.sub(r'>.*?(gene:.*? ).*?]',r'\1',gene)
#delete the '\n' and '>'
    newone=simplify_seq_mito.replace('\n','')
    length=len(newone)-11
    a=">"+'gene length:'+str(length)+' '+newone+"\n"
    l1.append(a)
    newfile.write(a)
newfile.close()
print(open('mito_gene.fa').read())