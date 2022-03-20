with open('rosalind_gc.txt','r') as t:
    a=t.readlines()
    b=[]
    for i in a:
        b.append(i.strip()) #stripping \n from each elements.
    b=''.join(b) #join all elements
    b=b.split('>')#divide string by '>'
    b.remove('')#remove ''
    Max = 0
    Maxname = ''#assign Max and Maxname outside of 'for'block. if it is in the block, it will reset for every i.
    for i in b:
        name=i[:13]
        total=len(i[13:])
        GC=i.count('G')+i.count('C')
        per=GC/total*100
        if Max<per:
            Max=per
            Maxname=name
    print(Maxname)
    print(Max)

#below is code written by LudditeCyborg
with open('rosalind_gc.txt', 'r') as file:
    re = ''.join(file.read().split('\n')).split('>') #\n goes away when splitted by it
    re.remove('')
    d = {}
    for i in re:
        x = i[13:].count('C') + i[13:].count('G')
        d[i[:13]] = x * 100 / (len(i[13:]))
    print(max(d, key=d.get), max(d.values()))
    #d.get = value by the key input
    #max used to print the key with largetst value, max(iterable, key=conditions)
    #max(d.values()) = print largest among values of d























