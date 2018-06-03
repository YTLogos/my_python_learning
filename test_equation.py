#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:test_equation.py
# author by:taoyan

# 导入复数数学模块模块cmath
import cmath
import math
#用户输入数字
a=float(input("输入数字a: "))
b=float(input("输入数字b: "))
c=float(input("输入数字c: "))

d=b**2-4*a*c
print("d=b**2-4*a*c= ",d)

if d==0:
    x=-b/2*a
    print("x的值为{}".format(x))
elif d>0:
    sol1=(-b + math.sqrt(d)) / (2 * a)
    sol2=(-b + math.sqrt(d)) / (2 * a)
    print("x1的值为{0},x2的值为{1}".format(sol1,sol2))
else:
    sol1=(-b-cmath.sqrt(d))/(2*a)
    sol2=(-b+cmath.sqrt(d))/(2*a)
    print("x1的值为{0},x2的值为{1}".format(sol1,sol2))
