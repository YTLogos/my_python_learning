#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:test_area.py
# author by:taoyan
while(True):
    triangle=input("请输入三角形三边(如6，8，10): ")
    sides=[float(side) for side in triangle.split(",")]
    a,b,c=sides
    if a+b<c or a+c<b or b+c<a:
        print("输入的三边无法构成三角形，请重新输入：")
    else:
        l=(a+b+c)/2
        s=(l*(l-a)*(l-b)*(l-c))**0.5
        print("三角形({0[0]},{0[1]},{0[2]})的面积为:{1:.2f}" .format(sides,s))
        break
