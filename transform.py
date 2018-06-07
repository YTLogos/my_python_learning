#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:transform.py
# author by:taoyan

#获取用户输入

while True:
    try:
        dec=int(input("请输入数字： "))
    except ValueError:
        print("您的输入有误，请重新输入！")
        continue
    print("十进制数为：",dec)
    print("转换为二进制数为： ",bin(dec))
    print("转换为八进制数为： ",oct(dec))
    print("转换为十六进制数为：",hex(dec) )
    break