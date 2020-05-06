# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:31:01 2020

@author: 陈文心
"""
#read BLOSUM62 matrix
import pandas as pd
matrix=pd.read_csv('BLOSUM62matrix.csv')
sum=0
identity=0
protein='ARNDCQEGHILKMFPSTWYVBZX'
seq_human='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
seq_mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
seq_randon='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
#for each amino acid, find score and add to variable 'sum'
for i in range(len(seq_human)):
    row=protein.index(seq_human[i])+1
    column=protein.index(seq_mouse[i])+1
#use iloc to locate score of two chosen amino acids in the blosum62matrix
    sum+=matrix.iloc[row,column]
#compare words at the same position of two sequences, if they are same, identity which
#represents the number of identical words should plus 1
    if seq_human[i]==seq_mouse[i]:
        identity+=1
print(seq_mouse+''+' '+str(sum))
percentage=identity/len(seq_human)*100
print(str(percentage)+'%')

        