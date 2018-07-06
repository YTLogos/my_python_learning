#Specify the name list's path
f1 = open('Brawrky_geneid.txt','r')
#Specify the fa file's path
f2 = open('Brawrky_geneid_change.txt','r')
# specify the output file's path
f3 = open('Brawrky_rename_pep.fasta','w')
dic = {}
for line in f1:
    li = line.strip().split('\t')
    dic[li[0]]=li[1]
#Edit the fa file
head = ''
seq = ''
for line in f2:
    if line[0] == '>' and seq == '':
        head = dic[line.strip()[1:]]        
    if line[0] != '>':
        seq = seq + line
    if line[0] == '>' and seq != '':
        f3.write('>'+head+'\n')
        f3.write(seq)
        head = dic[line.strip()[1:]]
        seq = ''
        
f3.write('>'+head+'\n')
f3.write(seq)   


f1.close()
f2.close()
f3.close()
