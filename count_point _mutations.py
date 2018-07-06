# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 10:57:37 2018

@author: taoyan
"""
def count_point_mutation(seq):
    line1=list(seq.readline().strip("\n"))
    line2=list(seq.readline().strip("\n"))
    count=0
    for i in range(len(line1)):
        if line1[i]!=line2[i]:
            count+=1
    print(count)
    seq.close()

if __name__=="__main__":
    seq=open("rosalind_hamm.txt","r")
    count_point_mutation(seq)
