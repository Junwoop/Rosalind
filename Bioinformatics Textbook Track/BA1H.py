with open('rosalind_ba1h.txt','r') as t:
    t=t.read().strip().splitlines()
    motif,text,d=t[0],t[1],int(t[2])
    k=len(motif)
    for i in range(len(text)-k+1):
        count=sum(1 for a,b in zip(motif,text[i:i+k]) if a!=b)
        if count<=d:
            print(i,end=" ")
















































































