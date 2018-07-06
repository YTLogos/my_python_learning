# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:21:24 2018

@author: taoyan
"""

from collections import Counter
test=open("rosalind_ini6.txt","r")
chr=test.read().split()
word_counts=Counter(chr)
for key, value in word_counts.items():
    print(key, value)

test.close()