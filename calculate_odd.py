# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:52:38 2018

@author: taoyan
"""

odd=0
test=open("rosalind_ini4.txt","r")
seq=test.readline().split(" ")
num1=int(seq[0])
num2=int(seq[1])
for i in range(num1,num2):
    if i%2==1:
        odd=odd+i
print("sum=",odd)
test.close()