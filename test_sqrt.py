#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:test_sqrt.py
# author by:taoyan

# 导入复数数学模块模块cmath

import cmath

# 用户输入数字
num=float(input("请输入一个数字："))

#判断是非负数还是负数
if num>=0:
    num_sqrt=num**0.5
    print("%0.3f的平方根为%0.3f" %(num,num_sqrt))
else:
    num_sqrt=cmath.sqrt(num)
    print("{0}的平方根为{1:0.3f}+{2:0.3f}j" .format(num,num_sqrt.real,num_sqrt.imag))
