#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:is_prime.py
# author by:taoyan

'''
一个大于1的自然数，除了1和它本身外，不能被其他自然数(质数)整除，换句话说就是该数除了1和它本身意外不再有其它因数
一般判断思路是：
在一般领域，对于正整数n，如果用2到√n之间的所有整数去除，均无法整除，则n为质数（合数）
'''
#说先根据判断思路定义一个函数

from math import sqrt
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i==0:
            return False
    return True

number=int(input("请输入一个整数："))
while is_prime(number):
        print("{0}是质数!".format(number))
        break
else:
    print("{0}不是质数!".format(number))


'''
还有一些其它的做法，但是有点繁琐，效率不高，这里也可以参考一下：

#用户输入数字
num=int(input("请输入一个数字： "))
#质数大于1
if num>1:
    #查看因子
    for i in range(2,num):
        if num % i ==0:
            print("{0}不是质数！".format(num))
            break
    else:
        print("{0}是质数！".format(num))
else:
    print("{0}不是质数！".format(num))'

'''

'''
下面这种做法也是利用平方根来减少运算量

#导入模块math
import math
#用户输入数字
num=int(input("请输入一个数字： "))
#质数大于1
if num>1:
    #找到平方根，减少计算量
    square_num=math.floor(num**0.5)
    #查找因子
    for i in range(2,(square_num+1)):
        if (num % i)==0:
            print("{0}不是质数，是合数！".format(num))
            break
    else:
             print("{0}是质数！".format(num))
#如果输入的数字小于或等于1，不是质数
else:
    print("{0}不是质数，也不是合数！".format(num))

'''
