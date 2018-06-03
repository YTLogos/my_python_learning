#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:isnumber.py
# author by:taoyan

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        pass
    
    try:
        import unicodedata #unicodedata模块提供访问unicode字符数据库
        unicodedata.numeric(n)
        return True
    except (ValueError,ValueError):
        pass

    return False