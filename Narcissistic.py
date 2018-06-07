#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:Narcissistic.py
# author by:taoyan

#用户输入
num=int(input("请输入一个数字： "))
#初始化变量 sum
sum=0
n=len(str(num))
temp=num
while temp>0:
    digit=temp % 10
    sum=sum+digit**n
    temp=temp // 10
if sum==num:
    print("{0}是阿姆斯特朗数".format(num))
else:
    print("{0}不是阿姆斯特朗数".format(num))


输出指定区间内的阿姆斯特朗数
#用户输入
lower=int(input("请输入最小值： "))
upper=int(input("请输入最大值： "))

for num in range(lower,upper+1):
    sum=0
    n=len(str(num))
    temp=num
    while temp>0:
        digit=temp % 10
        sum+=digit**n
        temp//=10
    if sum==num:
        print(num,end=" ")
