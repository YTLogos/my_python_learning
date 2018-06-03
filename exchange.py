#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:exchange.py
# author by:taoyan

# 用户输入
x=input("请输入x的值： ")
y=input("请输入y的值： ")
#创建临时变量用以交换
temp=x
x=y
y=temp
print("交换后的x的值为：{}".format(x))
print("交换后的y的值为：{}".format(y))

#还有一种更简洁的方法,可以不使用临时变量

'''
x,y=y,x
print("交换后的x的值为：{}".format(x))
print("交换后的y的值为：{}".format(y))
'''


