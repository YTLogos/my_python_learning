# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:14:23 2018

@author: taoyan
"""

code={}
data=open("rna_code_table.txt","r")
for line in data:
    line=line.strip("\n")
    line=line.split(" ")
    while '' in line:
        line.remove('')
    for i in range(0, len(line)-1,2):
        name=line[i]
        t=line[i+1]
        code[name]=t
#结果中的Stop不需要，不然提交结果出错
output=[]
seq=open("seq_prot.txt","r")
seq=seq.read().replace('\n','')
for i in range(0, len(seq)-3,3):
    c=seq[i:i+3]
    p=code[c]
    output.append(p)
for j in output:
    if j!='Stop':
        print(j,end="")
    
    

#根据上面的思路封装成函数
#首先生成密码子字典
#原始的密码子(rna_code_table.txt)如下：

"""
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
"""

def get_codon():
    codon={}
    try:
        rna_code=open("rna_code_table.txt","r")
        code=rna_code.read().strip().split()
        for i in range(0, len(code)-1,2):
            (k,v)=code[i:i+2]
            codon[k]=v
        return codon
    except FileExistsError or FileNotFoundError:
        print("Could not read rna_code_table file!")
    finally:
        rna_code.close()
            
def read_seq_file():
    try:
        seq=open("test.txt", "r")
        data=seq.read().replace('\n','')
    except FileExistsError or FileNotFoundError:
        print("Could not open seq file!")
    finally:
        seq.close()
    return data

def save_file(result):
    try:
        output=open("dna2prot_result.txt","w")
        output.write(result)
    except FileExistsError or FileNotFoundError:
        print("Could not save the result file!")
    finally:
        output.close()
        
def translate_codon(seq):
    codon=get_codon()
    protein=''
    start_codon=seq.find("AUG")
    for i in range(start_codon, len(seq)-1,3):
        code=seq[i:i+3]
        if codon[code]=="Stop":
            break
        protein=protein+codon[code]
    return protein

def main():
    seq=read_seq_file()
    result=translate_codon(seq)
    save_file(result)
    
if __name__=="__main__":
    main()
    








