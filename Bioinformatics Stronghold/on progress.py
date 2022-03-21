with open('input.txt','r') as t:
    t=t.read().split('\n')
    length=len(t[1])
    for i in t[1::2]:
        a=list(map(i[0].count,'ACGT'))




