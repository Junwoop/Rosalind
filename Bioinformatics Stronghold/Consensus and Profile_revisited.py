with open('rosalind_cons.txt','r') as t:
    t=t.read().split('\n')
    t=(''.join(t).split('>'))
    t.remove('')
    string=[x[13:] for x in t]#slicing 'Rosalind_xxxx'
    #original string = ['123','456','789']
    matrix=zip(*string)
    #matrix(transposed)=[(1,4,7),(2,5,8),(3,6,9)]
    profile_matrix=list(map(lambda x: dict((base,x.count(base)) for base in 'ACGT'),matrix))
    #lambda x: make function with x:
    #function = make dictionary {Base(ACGT),x.count(Base} /and x is matrix
    #map() applies function to every element in matrix, a row in this case
    #row=first base of all strings.
    #output={A:n C:n T:n G:n} for each row
    consensus=[max(x,key=x.get) for x in profile_matrix]
    print(''.join(consensus))
    for base in 'ACGT':
        print(base,':',end='') #end='' prints in horizontal line
        for i in profile_matrix:#after printing one base, for base-
            print(i[base],end='')
        print('') #this causes linebreak after base output






