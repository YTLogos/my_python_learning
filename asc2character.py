#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:asc2character.py
# author by:taoyan

# 获取用户输入字符
char=input("请输入一个字符：")

#获取用户输入ASCII码，并转化为整型
num=int(input("请输入一个ASCII码："))

print(char,"的ASCII码为",ord(char))
print(num,"对应的字符为", chr(num))
