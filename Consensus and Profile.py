with open('rosalind_cons.txt','r') as t:
    t=t.read().split('\n')
    T=''.join(t).split('>')
    T.remove('')
    length=len(T[1])-13
    def each(j):
        b = []
        for i in T:
            a=list(map(i[j+13].count,'ACGT'))
            b.append(a)
            c=[sum(x) for x in zip(*b)]
        return(c)
    rank=list(map(each,range(0,length)))
    var=[]
    A=[]
    C=[]
    G=[]
    T=[]
    d={0:'A',1:'C',2:'G',3:'T'}
    final=''
    for i in rank:
        var.append(i.index(max(i)))
        A.append(i[0])
        C.append(i[1])
        G.append(i[2])
        T.append(i[3])
    for i in var:
        final+=d[i]
    print(final)
    print('A:',' '.join(str(e) for e in A))
    print('C:', ' '.join(str(e) for e in C))
    print('G:', ' '.join(str(e) for e in G))
    print('T:', ' '.join(str(e) for e in T))

#solution by Darkstar
strands = [x.strip() for x in t.readlines()]
matrix = zip(*strands)
profile_matrix = map(lambda x: dict((base, x.count(base)) for base in "ACGT"), matrix)
consensus = [max(x,key = x.get) for x in profile_matrix]
print("".join(consensus);)

for base in "ACGT":
    print(base+":",)
    for x in profile_matrix:
        print x[base],
    print("")




