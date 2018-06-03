#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:test_area.py
# author by:taoyan

import random
i=1
a=random.randint(0,100)
b=int(input("请输入一个0～100之间的数字\n然后查看是否与电脑随机生成的数字相同："))
while a!=b:
    if a>b:
        print("这是你第%d次输入的数字，很抱歉你输入的数字小于电脑生成的随机数"%i)
        b=int(input("请再次输入0~100之间的数字："))
    else:
        print("这是你第%d次输入的数字，很抱歉，你输入的数字大于电脑生成的随机数"%i)
        b=int(input("请再次输入0~100之间的数字："))
    i=i+1

else:
    print("恭喜你，你第%d次输入的数字%d与电脑的随机数字%d一样"%(i,b,a))
