#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:calendar_generation.py
# author by:taoyan

import calendar
year=int(input("输入年份： "))
month=int(input("输入月份： "))
print(calendar.month(year, month))