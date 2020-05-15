# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:45:08 2020

@author: 陈文心
"""
#define a function to find the number of childnodes using recursion
def numberofchildnodes(no):
    global terms
    count=0
    #go through all parents of terms to find  parent of terms which is equal to this term 
    for term in terms:
        is_a=term.getElementsByTagName('is_a')
        for parent in is_a:
            if parent.childNodes[0].data==no:
                count+=1
                #count child's children
                nextno=term.getElementsByTagName('id')[0].childNodes[0].data
                count+=numberofchildnodes(nextno)
    return count
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse("go_obo.xml")
import pandas as pd
#get the root element of the document
root=DOMTree.documentElement
#get a collection of term nodes
terms=root.getElementsByTagName('term')
id_list=[]
name_list=[]
def_list=[]
nun_childnodes=[]
#go through all terms and find those with autophagosome
for term in terms:
    go_def=term.getElementsByTagName('def')[0]
    go_id=term.getElementsByTagName('id')[0]
    go_name=term.getElementsByTagName('name')[0]
    defstr=go_def.getElementsByTagName('defstr')[0].childNodes[0].data
    
    #if autophagesome is in defstr, add the text of name/id/def
    if defstr.find('autophagosome')>-1 or defstr.find('Autophagosome')>-1:
        id_list.append(go_id.childNodes[0].data)
        name_list.append(go_name.childNodes[0].data)
        def_list.append(defstr)
        nun_childnodes.append(numberofchildnodes(term))
#output the excel using dictionary
df1={'id':id_list,'name':name_list,'definition':def_list,'childnodes':nun_childnodes}
df1=pd.DataFrame(df1,columns=['id','name','definition','childnodes'])
df1.to_excel(r'D:\autophagosome.xlsx')
        
    