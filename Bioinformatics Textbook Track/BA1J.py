import itertools
with open('rosalind_ba1j.txt','r') as t:
    t=t.read().strip().splitlines()
    text,k,d=t[0],int(t[1].split(' ')[0]),int(t[1].split(' ')[1])
    text_rev=text[::-1].translate(text[::-1].maketrans('ATCG','TAGC'))
    kmers=list(map(''.join,itertools.product('ACTG',repeat=k)))
    def hamm(str1,str2):
        dist=dict.fromkeys(kmers,0)
        for kmer in kmers:
            for i in range(len(str1)-k+1):
                count=sum(1 for i,j in zip(kmer,str1[i:i+k]) if i!=j)
                if count<=d:
                    dist[kmer]+=1
        for kmer in kmers:
            for i in range(len(str2)-k+1):
                count=sum(1 for i,j in zip(kmer,str2[i:i+k]) if i!=j)
                if count<=d:
                    dist[kmer]+=1
        return dist
    dist=hamm(text,text_rev)
    for i in dist:
            if dist[i]==max(dist.values()):
                print(i,end=" ")
























































































