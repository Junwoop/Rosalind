with open('input.txt','r') as t:
    t=''.join(t.read().strip().split())
    t=t.split('>')
    t.remove('')
    string=[]
    for i in t:
        string.append(i[11:])

    exons=[]
    DNA = string[0]
    for i in string[1:]:
        exons.append(DNA[0:DNA.index(i)])
        DNA=DNA[DNA.index(i)+len(i):]
    exons.append(DNA)
    spliced=''.join(exons)






