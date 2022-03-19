with open('rosalind_revc.txt','r') as t:
    a=t.read().strip('\n')[::-1]
    d={'A':'T','C':'G','T':'A','G':'C'}
    com=[]
    for i in a:
        com.append(d[i])
    print(''.join(com))

#solution by Ben Usman(#need to open file to execute)
    st= t.read().strip('\n')
    st= st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    print(st)
    #convert to lowercase(avoid overlap) -> change to uppercase -> reverse[::-1]












