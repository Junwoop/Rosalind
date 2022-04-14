import itertools
with open('rosalind_ba1i.txt','r') as t:
    t=t.read().strip().splitlines()
    string,k,d=t[0],int(t[1].split()[0]),int(t[1].split()[1])
    kmers,motif=[],{}
    for i in range(len(string)-k+1):
        kmers.append(string[i:i+k])
    motif=dict.fromkeys(map(''.join,itertools.product('ACTG',repeat=k)),0)

##need to generate all possible kmers##
#https://github.com/andreyrozumnyi/rosalind/blob/master/Chapter%201/BA1I.py

    for i in motif:
        for j in range(len(kmers)):
            count=sum(1 for a,b in zip(i,kmers[j]) if a!=b)
            if count<=d:
               motif[i]+=1
    for i in motif:
        if motif[i]==max(motif.values()):
            print(i, end=' ')











































































