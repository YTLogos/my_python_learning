# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:30:23 2018

@author: taoyan
"""

seq=open("rosalind_revc.txt", "r")
chr=seq.read().strip("\n")
chr_rev=chr[::-1]
rever_com=[]
for i in chr_rev:
    if i=="A":
        i="T"
        rever_com.append(i)
    elif i=="T":
        i="A"
        rever_com.append(i)
    elif i=="C":
        i="G"
        rever_com.append(i)
    elif i=="G":
        i="C"
        rever_com.append(i)

print("".join(rever_com))
seq.close()   
#方法2，利用字典

seq=open("rosalind_revc.txt", "r")
chr=seq.read().strip("\n")
chr_rev=chr[::-1]
rever_com=[]
complement={"A":"T","T":"A","C":"G","G":"C"}
for i in chr_rev:
    rever_com.append(complement[i])
print("".join(rever_com))
seq.close()


#方法3，传参
from sys import argv

response = ""
translate = {"A":"T","T":"A","G":"C","C":"G"}
for nuc in open(argv[1]).read():
    response = translate[nuc] + response
print (response)


#方法4
def complementingDNA(dnaString):
    dnaList=list(dnaString)
    pattern={"A":"T","T":"A","C":"G","G":"C"}
    complementList=[pattern[x] if x in pattern else x for x in dnaList]
    complementList.reverse()
    reversedComplement=("").join(complementList)
    print(reversedComplement)

if __name__=="__main__":
    file=open("rosalind_revc.txt","r")
    dnaString=file.read().strip("\n")
    complementingDNA(dnaString)
    





