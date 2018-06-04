#!/home/taoyan/anaconda3/bin/python3
# -*- coding: UTF-8 -*-
# filename:max_number.py
# author by:taoyan
while True:
    try:
        N=int(input("请输入需要对比大小数字的个数： "))
    except ValueError:
        print("您输入的不是整数，请重新输入！")
        continue
    print("请输入需要对比的数字： ")
    num=[]
    for i in range(1,N+1):
        temp=int(input("请输入第%d个数字: " %i))
        num.append(temp)    
    print("您输入的数字为:",num)
    print("最大值为:", max(num))
    break
    