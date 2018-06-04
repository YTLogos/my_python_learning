#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:Fibonacci.py
# author by:taoyan

#用户输入数据
n1=0
n2=1
while True:
    try:
        n=int(input("您需要输出几项？： "))
    except ValueError:
        print("您的输入有误，请重新输入！")
        continue
    if n<=0:
        print("请输入一个正整数！")
        continue
    elif n==1:
        print("斐波那契数列：")
        print(n1)
    else:
        print("斐波那契数列: ")
        print(n1,",",n2, end=", ")
        for i in range(3,n+1):
            nth=n1+n2
            print(nth, end=", ")
            n1=n2
            n2=nth
    break

