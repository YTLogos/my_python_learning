#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:leapyear.py
# author by:taoyan


'''
判断年份是不是闰年，首先是看能不能被4整除，再看是否能被100整除，最后看是否能被400整除
'''

while True:
    try:
        year=int(input("请输入一个年份： "))
    except ValueError:
        print("年份是正整数，您输入的不符合要求，请重新输入！")
        continue
    if (year % 4)==0:
        if(year % 100)==0:
            if(year % 400)==0:
                print("{0}是闰年！".format(year))
            else:
                print("{0}不是闰年！".format(year))
        else:
            print("{0}不是闰年！".format(year))
    else:
        print("{0}不是闰年！".format(year))
    break