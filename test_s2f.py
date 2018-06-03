#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:test_area.py
# author by:taoyan

w=int(input("摄氏度转为华氏温度请按1\n华氏温度转为摄氏度请按2\n现在输入您的选项："))
while w!=1 and w!=2:
    w=int(input("您的输入有误，请再次输入您的选项："))

if w==1:
    celsius=float(input("请输入摄氏度："))
    fahrenheit=((celsius*1.8)+32)
    print("%.2f摄氏度转为华氏温度为：%.2f" %(celsius,fahrenheit))
else:
    fahrenheit = float(input('输入华氏度:'))
    celsius = (fahrenheit - 32)/1.8
    print("%.2f华氏温度转为摄氏度为：%.2f" %(fahrenheit,celsius))
