#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:judge.py
# author by:taoyan

while True:
    try:
        num=float(input("请输入一个数字： "))
        if num==0:
            print("输入的数字为零")
        elif num>0:
            print("输入的数字是正数")
        else:
            print("输入的数字是负数")
        break
    except ValueError:
        print("输入无效，请再次输入")