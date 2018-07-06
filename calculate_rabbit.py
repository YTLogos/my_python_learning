# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:16:30 2018

@author: taoyan
"""

data=open("rosalind_fib.txt","r")
num=data.read().strip("\n").split(" ")
n=int(num[0])
k=int(num[1])
a=1
b=1
c=0
for i in range(3,n+1):
    c=a*k+b
    a=b
    b=c
print("The total number of rabbit pairs that will be:",c,"after",n,"month")
data.close()
   
def fibona_rabbit(n,k):
    a,b,c=1,1,0
    for i in range(3,n+1):
       c=a*k+b
       a=b
       b=c
    print("The total number of rabbit pairs that will be:",c,"after",n,"month")

if __name__=="__main__":
    file=open("rosalind_fib.txt","r")
    num=file.read().strip("\n").split(" ")
    n=int(num[0])
    k=int(num[1])
    fibona_rabbit(n,k)
    











 