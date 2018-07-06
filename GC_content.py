# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 16:46:04 2018

@author: taoyan
"""    
def parse_fasta(s):
    results = {}
    strings = s.strip().split('>')
    # Python split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
 
    for s in strings:
        if len(s) == 0:
            continue
            # 如果字符串长度为0，就跳出循环。
 
        parts = s.split()
        label = parts[0]
        bases = ''.join(parts[1:])
 
        results[label] = bases
 
    return results           
        
def gc_content(s):
    n=len(s)
    m=0
    
    for c in s:
        if c=="G" or c=="C":
            m+=1
    return 100*(float(m)/n)

if __name__=="__main__":
    sequence=open("rosalind_gc.txt","r").read()
    results=parse_fasta(sequence)
    results=dict([(k, gc_content(v)) for k,v in results.items()])
    
    highest_k=None
    highest_v=0
    for k,v in results.items():
        if v>highest_v:
            highest_k=k
            highest_v=v
    print(highest_k)
    print("{:0.6f}".format(highest_v))
     
    
#方法2
def gc_content_calculate(sequence):
    name=[]
    seq=[]
    data=''
    for line in sequence:
        line=line.strip()
        for i in line:
            if i==">":
                name.append(line[1:])
                if data:
                    seq.append(data)
                    data=''
                break
            else:
                line=line.upper()
            if all(k==k.upper() for k in line):
                data=data+line
    seq.append(data)
    GC_list=[]
    for seq in seq:
        i=0
        for k in seq:
            if k=="G" or k=="C":
                i+=1
        GC_content=float(i)/len(seq)*100
        GC_list.append(GC_content)
    m=max(GC_list)
    print(name[GC_list.index(m)])
    print("{:0.6f}".format(m))
    
if __name__=="__main__":
    sequence=open("rosalind_gc.txt","r")
    sequence=sequence.readlines()
    gc_content_calculate(sequence)
                
                
                
            
        