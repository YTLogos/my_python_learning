# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 19:21:28 2018

@author: taoyan
"""
#方法1
sequence=open("rosalind_dna.txt","rt")
A=0
C=0
T=0
G=0
seq=sequence.readlines()
seq=list(str(seq))
for i in seq:
    if i=="A":
        A+=1
    if i=="T":
        T+=1
    if i=="C":
        C+=1
    if i=="G":
        G+=1
print(A,C,G,T)

sequence.close()
#方法2


seq=''
ntcounts=[]
with open("rosalind_dna.txt") as f:
    for line in f:
        line=line.rstrip()
        seq+=line.upper()

for nt in ["A","C","G","T"]:
    ntcounts.append(seq.count(nt))
#join()用于将序列中的元素以指定的字符连接生成一个新的字符串
#map()会根据提供的函数对指定的序列做映射
print ('\t'.join(map(str, ntcounts)))

f.close()

#方法3

with open("rosalind_dna.txt") as f:
    for line in f:
        seq=list(str(line.rstrip()))
        count={}
        for a in seq:
            count[a]=seq.count(a)
print(count)


#方法4
ntcounts={c:0 for c in "ATCG"}
for line in open("rosalind_dna.txt"):
    for c in line.rstrip():
        ntcounts[c]+=1
print(ntcounts)

#方法5
from collections import Counter
print (Counter(open("rosalind_dna.txt").read().rstrip()))



