# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:15:33 2018

@author: taoyan
"""

file=open("rosalind_ini5.txt","r")
set=[]
for line in file:
    set.append(line.strip("\n"))
    
for i in range(1,len(set)+1):
    if i%2==0:
        print(set[i-1],end="\n")
        
file.close()