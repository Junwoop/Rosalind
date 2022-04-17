import itertools
with open('rosalind_ba1k.txt','r') as t:
    t=t.read().strip().splitlines()
    text,k=t[0],int(t[1])
    kmers=dict.fromkeys((map(''.join,itertools.product('ACGT',repeat=k))),0)
    for i in kmers:
        for j in range(len(text)-k+1):
            if i==text[j:j+k]:
                kmers[i]+=1
    array=map(str,list(kmers.values()))
    print(' '.join(array))



























































































