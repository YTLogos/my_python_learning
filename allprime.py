#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:allprime.py
# author by:taoyan

'''
这个题目跟上次那个判断质数的题目差不多，先给定一个范围，遍历，判断是不是质数，如果是的话输出
'''

from math import sqrt
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i==0:
            return False
    return True
#用户输入区间
lower=int(input("请输入区间的最小值： "))
upper=int(input("请输入区间的最大值： "))
for num in range(lower,upper+1):
    if is_prime(num):
        print(num)