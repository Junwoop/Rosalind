import itertools
with open('rosalind_perm.txt','r') as t:
    t=int(t.read())
    rng=[]
    for i in range(1,t+1):
        rng.append(i)
    text=''.join(map(str,rng))
    result=[*map(' '.join, itertools.permutations(text,len(text)))]
    print(len(result))
    for i in result:
        print(i)


















