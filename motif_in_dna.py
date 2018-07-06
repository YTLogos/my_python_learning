# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:07:09 2018

@author: taoyan
"""
   
def read_file():
    try:
        data=open("rosalind_subs.txt", "r")
        seq=data.readline().strip()
        target=data.readline().strip()
    except FileExistsError or FileNotFoundError:
        print("Could not open file!")
    finally:
        data.close()
    return seq,target

def motif_find_position(seq,target):
    n=[]
    for i in range(0,len(seq)):
        if seq[i:len(target)+i]==target:
            n.append(i)
    return n

def save_file(result):
    try:
        output=open("motif_in_seq.txt","w")
        for i in result:
            i=str(i)
            output.write(i+" ")
    except FileExistsError or FileNotFoundError:
        print("Could not save the result file!")
    finally:
        output.close()
def main():
    seq,target=read_file()
    result=motif_find_position(seq,target)
    save_file(result)
    
if __name__=="__main__":
    main()
    
    