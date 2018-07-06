# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:30:47 2018

@author: taoyan
"""

#方法1（结果与方法2不同，提交结果也出错）

from scipy.misc import comb
def Mendel_P(population):
    data=population.read().split(" ")
    k=int(data[0])
    m=int(data[1])
    n=int(data[2])
    t=k+m+n
    rr=comb(n,2)/comb(t,2)
    hh=comb(n,2)/comb(t,2)
    hr=comb(n,1)*comb(m,1)/comb(t,2)
    prob=1-(rr+hh*1/4+hr*1/2)
    print("{:0.5f}".format(prob))

if __name__=="__main__":
    population=open("rosalind_iprb.txt", "r")
    Mendel_P(population)
    population.close()
 
    
#方法2
  
def count_prob(population):
    data=population.read().split(" ")
    k=int(data[0])
    m=int(data[1])
    n=int(data[2])
    t = k+m+n #the sum of population
    c = t*(t-1)/2.0 #comb(2,s)
    prob = 1 - (n*(n-1)/2+0.25*m*(m-1)/2+m*n*0.5)/c
    print("{:0.5f}".format(prob))
    
if __name__=="__main__":
    population=open("rosalind_iprb.txt", "r") 
    count_prob(population)
    population.close()

   