# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:45:00 2018

@author: taoyan
"""

chr=open("rosalind_rna.txt","r")
dna=chr.read()
rna=[]
for i in dna:
    if i=="T":
        i="U"
        rna.append(i)
    else:
        rna.append(i)
for i in rna:
    print(i,end="")