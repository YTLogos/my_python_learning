#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:lcm.py
# author by:taoyan

#定义函数
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while True:
        if((greater % x==0) and (greater % y == 0)):
            lcm=greater
            break
        greater +=1
    return lcm
while True:
    try:
        num1=int(input("请输入第一个数字： "))
        num2=int(input("请输入第二个数字： "))
    except ValueError:
        print("您的输入有误，请重新输入！")
        continue
    lcm=lcm(num1,num2)
    print("{0}和{1}的最小公倍数为{2}" .format(num1,num2,lcm))
    break

'''
上面这种方法运行速度非常慢，效率非常低，可以通过以下思路减小运算量：
1、当最大值为最小公倍数时，返回最大值    
2、当最大值不为最小公倍数时，最小公倍数为最大值的倍数
'''
'''
def lcm1(x,y):
    if y>x:
        x,y=y,x
    if x % y==0:
        return x
    m=2
    while x*m % y !=0:
        m +=1
    return x*m
while True:
    try:
        num1=int(input("请输入第一个数字： "))
        num2=int(input("请输入第二个数字： "))
    except ValueError:
        print("您的输入有误，请重新输入！")
        continue
    lcm=lcm1(num1,num2)
    print("{0}和{1}的最小公倍数为{2}" .format(num1,num2,lcm))
    break
'''

