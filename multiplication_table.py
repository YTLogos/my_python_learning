#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:multiplication_table.py
# author by:taoyan

#九九乘法表十分简单

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}\t".format(i,j,i*j), end="")
    print()

'''
下面是参考别人的方法：
class multiplication_table():
    def paint(self, n=9):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("{1}*{0}={2}\t".format(i,j,i*j), end="")
            print()
table=multiplication_table()
table.paint

'''