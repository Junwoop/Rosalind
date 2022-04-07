with open('rosalind_ba1c.txt','r') as t:
    dic={'A':'T','C':'G','T':'A','G':'C'}
    res=[]
    for i in t.read().strip()[::-1]:
        res.append(dic[i])
    print(''.join(res))
    # print(t.read().strip()[::-1].translate(str.maketrans('ACGT','TGCA')))
    ## one line solution by James Ashmore       #can skip import string












































