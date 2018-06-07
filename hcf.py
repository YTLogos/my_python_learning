#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:hcf.py
# author by:taoyan


#获取两个数的最大公约数
#先定义一个函数

def hcf(x,y):
    '''先比较两个数'''
    if x > y:
        samller=y
    else:
        samller=x
    for i in range(1,samller+1):
        if(x%i==0) and (y%i==0):
            hcf=i
    return hcf

while True:
    try:
        num1=int(input("请输入第一个数字："))
        num2=int(input("请输入第二个数字："))
    except ValueError:
        print("您的输入有误，请重新输入！")
        continue
    h=hcf(num1,num2)
    print("{0}和{1}的最大公约数是{2}".format(num1,num2,h))
    break
        
'''
下面是其他人的解题方法
按以下思路减少循环次数，降低运算量：
1.当最小值为最大公约数时，直接返回
2.当最小值不为最大公约数时，最大公约数不会大于最小值的1/2
3.求最大公约数时按从大到小的顺序循环递减
'''
'''
def hcf(a,b):
    if b>a and b%a==0:
        return a
    else:
        for i in range(a//2+1,1,-1):
            if a%i==0 and b%i==0:
                return i
        return 0
while True:
    try:
        a=int(input("请输入第一个数字： "))
        b=int(input("请输入第二个数字： "))
    except ValueError:
        print("您的输入有误，请重新输入")
        continue
    h=hcf(a,b)
    print("{0}和{1}的最大公约数为{2}".format(a,b,h))
    break
'''

'''
第二个例子，这个方法非常快非常简洁

def hcf(a,b):
    return a if b==0 else hcf(b,a%b)

while True:
    try:
        a=int(input("请输入第一个数字： "))
        b=int(input("请输入第二个数字： "))
    except ValueError:
        print("您的输入有误，请重新输入！")
        continue
    h=hcf(a,b)
    print("{0}和{1}的最大公约数为{2}".format(a,b,h))
    break
'''
'''
第三个例子：利用的是当最小值不为最大公约数时，最大公约数不会大于最小值的1/2

while True:
    try:
        a=int(input("请输入第一个数字： "))
        b=int(input("请输入第二个数字： "))
    except ValueError:
        print("您的输入有误，请重新输入！")
        continue
    for i in range(min(a,b)+1,1,-1):
        if a%i==0 and b%i==0:
            hcf=i
            break
    print("{0}和{1}的最大公约数为{2}".format(a,b,hcf))
    break
'''

第四个例子利用的是欧几里得算法
两个数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数，第二个例子也用到了

def hcf(a,b):
    if a==0:
        a,b=b,a
    else:
        while b !=0:
            a,b=b,a%b
        return a

while True:
    try:
        a=int(input("请输入第一个数字： "))
        b=int(input("请输入第二个数字： "))
    except ValueError:
        print("您的输入有误，请重新输入！")
        continue
    h=hcf(a,b)
    print("{0}和{1}的最大公约数为{2}".format(a,b,h))
    break
    

