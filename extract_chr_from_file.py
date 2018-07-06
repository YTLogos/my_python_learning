# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 19:46:13 2018

@author: taoyan
"""
test=open("rosalind_ini3.txt","r")
chr=test.readline().strip("\n.")
num=test.readline().split(" ")
slice1=int(num[0])
slice2=int(num[1])+1
slice3=int(num[2])
slice4=int(num[3])+1
print("first:",chr[slice1:slice2])
print("second:",chr[slice3:slice4])


