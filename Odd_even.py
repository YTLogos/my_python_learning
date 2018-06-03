#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:Odd_even.py
# author by:taoyan
'''
判断一个数是奇数还是偶数
如果是偶数的话除于2余数为0
奇数的话余数为1
'''

while True:
    try:
        num=int(input("请输入一个整数： "))
    except ValueError:   #不是纯数字或者不是整数需要重新输入
        print("输入的不是整数！")
        continue
    if num%2==0:
        print("{0}是偶数！".format(num))
    else:
        print("{0}是奇数！".format(num))
    break
