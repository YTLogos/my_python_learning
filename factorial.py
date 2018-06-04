#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:factorial.py
# author by:taoyan

#用户输入数字
factorial=1
while True:
    try:
        num=int(input("请输入一个数字： "))
    except ValueError:
        print("您的输入有误，请重新输入！")
        continue
    if num<0:
        print("抱歉，负数没有阶乘！")
    elif num==0:
        print("0的阶乘是1")
        break
    else:
        for i in range(1,num+1):
            factorial=factorial*i
        print("%d的阶乘为%d" %(num,factorial))
        break

'''
第二种方法是：利用模块functools中的reduce函数

from functools import reduce
while True:
    try:
        n=int(input("请输入一个整数："))
    except ValueError:
        print("您的输入有误，请重新输入")
        continue
    if n<0:
        print("抱歉，您输入的是负数，没有阶乘，请重新输入！")
    elif n==0:
        print("{0}的阶乘为1".format(n))
        break
    else:
        sum=reduce(lambda x,y:x*y, range(1,n+1))
        print("%d的阶乘为%d" %(n,sum))
        break

'''

第三种方法是利用模块math中的阶乘函数factorial

from math import factorial
while True:
    try:
        n=int(input("请输入一个整数："))
    except ValueError:
        print("您的输入有误，请重新输入")
        continue
    if n<0:
        print("抱歉，您输入的是负数，没有阶乘，请重新输入！")
    elif n==0:
        print("{0}的阶乘为1".format(n))
        break
    else:
        sum=factorial(n)
        print("%d的阶乘为%d" %(n,sum))
        break