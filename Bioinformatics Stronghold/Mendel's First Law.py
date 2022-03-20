with open('rosalind_iprb.txt','r') as t:
    r=list(map(int,t.read().split()))
    k,m,n=r[0],r[1],r[2]
    tot=(k+m+n)
    rec=(n/tot)*((n-1)/(tot-1))    #all second parents must have denominators (tot-1) since one is already chosen
    hetrec=(m/tot*n/(tot-1))*2
    hethet=((m/tot)*(m-1)/(tot-1))
    recprob=rec+hetrec*1/2+hethet*1/4 #computed probability of having recessive allele
    print(1-recprob)
























